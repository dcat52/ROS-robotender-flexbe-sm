#!/usr/bin/env python

import rospy

from flexbe_core import EventState, Logger

from flexbe_core.proxy import ProxyActionClient

from flexbe_core.proxy import ProxySubscriberCached

from sensor_msgs.msg import JointState 

from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal, Constraints, JointConstraint, MoveItErrorCodes

'''
created on: 10-19-2017

@author: davis catherman
@author: shannon enders
'''

class FeedbackJointStateToMoveit(EventState):
        '''
        State to send a joint state configuration to MoveIt to plan and move.

        -- move_group           string              Name of the move group to be used for planning.

        -- action_topic         string              Topic on which MoveIt is listening for action calls.

        -- robot_name           string              Optional name of the robot to be used.
                                                                If left empty, the first one found will be used
                                                                (only required if multiple robots are specified in the same file).

        -- position_topic       string              Topic on which to validate the arm has reached the goal.

        -- delta                float               Value to check to see if each joint is moving.

        ># joint_names          string[]            Names of the target joints.
                                                                        Same order as their corresponding names in joint_values.

        ># joint_values         float[]             Target configuration of the joints.
                                                                        Same order as their corresponding names in joint_names.

        <= reached                                  Target joint configuration has been reached.

        <= failed                          Failed to find a reach/plan the given joint configuration.

        '''


        def __init__(self, move_group="arm", action_topic="/move_group", robot_name="m1n6s200",
                position_topic='/m1n6s200_driver/joint_states', delta=1E-4):
                '''
                Constructor
                '''
                super(FeedbackJointStateToMoveit, self).__init__(input_keys=['joint_values', 'joint_names'],
                                                        outcomes=['reached', 'failed'])


                self._position_topic = position_topic
                self._delta = delta
                self._move_group      = move_group
                self._action_topic    = action_topic
                self._robot_name   = robot_name

        def execute(self, userdata):
                '''
                Execute this state
                '''
                if self._planning_failed:
                        return 'failed'
                if self._control_failed:
                        return 'failed'
                if self._success:
                        return 'reached'

                if self._client.has_result(self._action_topic):
                        result = self._client.get_result(self._action_topic)

                        if result.error_code.val == MoveItErrorCodes.CONTROL_FAILED:
                                Logger.logwarn('Control failed for move action of group: %s (error code: %s)' % (self._move_group, str(result.error_code)))
                                self._control_failed = True
                                return 'failed'
                        elif result.error_code.val != MoveItErrorCodes.SUCCESS:
                                Logger.logwarn('Move action failed with result error code: %s' % str(result.error_code))
                                self._planning_failed = True
                                return 'failed'
                        else:
                                if len(self._last_position) != 0 and len(self._current_position) != 0:

                                        temp_success = True

                                        # Check to see within error delta,
                                        # this checks to see if still moving
                                        for index in range(len(self._last_position)):

                                                actual_delta = self._last_position[index] - self._current_position[index]
                                                if actual_delta > self._delta:
                                                        temp_success = False

                                        if temp_success == True:
                                                self._success = True
                                                return 'reached'
                
                if self._sub.has_msg(self._position_topic):

                        msg = self._sub.get_last_msg(self._position_topic)

                        self._last_position = self._current_position
                        self._current_position = list(msg.position)

                        self._sub.remove_last_msg(self._position_topic)

        def on_enter(self, userdata):
                self._planning_failed = False
                self._control_failed  = False
                self._success         = False
                self._joint_config    = userdata.joint_values
                self._joint_names     = userdata.joint_names

                self._sub             = ProxySubscriberCached({self._position_topic: JointState})
                self._current_position= []

                self._client = ProxyActionClient({self._action_topic: MoveGroupAction})

                # Action Initialization
                action_goal = MoveGroupGoal()
                action_goal.request.group_name = self._move_group
                action_goal.request.allowed_planning_time = 1.0
                goal_constraints = Constraints()
                for i in range(len(self._joint_names)):
                        goal_constraints.joint_constraints.append(JointConstraint(
                                joint_name=self._joint_names[i],
                                position=self._joint_config[i],
                                weight=1.0))
                action_goal.request.goal_constraints.append(goal_constraints)

                try:
                        self._client.send_goal(self._action_topic, action_goal)
                except Exception as e:
                        Logger.logwarn('Failed to send action goal for group: %s\n%s' % (self._move_group, str(e)))
                        self._planning_failed = True

        def on_stop(self):
                try:
                        if self._client.is_available(self._action_topic) \
                        and not self._client.has_result(self._action_topic):
                                self._client.cancel(self._action_topic)
                except:
                        # client already closed
                        pass

        def on_pause(self):
                self._client.cancel(self._action_topic)

        def on_resume(self, userdata):
                self.on_enter(userdata)
