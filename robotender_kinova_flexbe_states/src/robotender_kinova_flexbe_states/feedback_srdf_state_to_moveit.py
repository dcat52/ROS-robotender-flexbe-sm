#!/usr/bin/env python

import rospy
import xml.etree.ElementTree as ET
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

class FeedbackSrdfStateToMoveit(EventState):
        '''
        State to look up a pre-defined joint configuration from the SRDF file loaded in the parameter server (/robot_description_semantic)
        and send it to MoveIt to plan and move.

        -- config_name          string              Name of the joint configuration of interest.

        -- move_group           string              Name of the move group to be used for planning.

        -- action_topic         string              Topic on which MoveIt is listening for action calls.

        -- robot_name           string              Optional name of the robot to be used.
                                                                If left empty, the first one found will be used
                                                                (only required if multiple robots are specified in the same file).

        -- position_topic       string              Topic on which to validate the arm has reached the goal.

        -- delta                float               Value to check to see if each joint is moving.

        <= reached                                  Target joint configuration has been reached.

        <= failed                                   Failed to plan / move / reach.

        '''

        def __init__(self, config_name='Home', move_group='arm', action_topic='/move_group', robot_name='m1n6s200',
            position_topic='/m1n6s200_driver/joint_states', delta=1E-4):
                '''
                Constructor
                '''
                super(FeedbackSrdfStateToMoveit, self).__init__(outcomes=['reached', 'failed'])

                self._position_topic = position_topic
                self._delta = delta
                self._config_name  = config_name
                self._move_group   = move_group
                self._robot_name   = robot_name
                self._action_topic = action_topic
                self._client       = ProxyActionClient({self._action_topic: MoveGroupAction})

                self._planning_failed = False
                self._control_failed = False
                self._success = False

                self._srdf_param = None
                if rospy.has_param("/robot_description_semantic"):
                        self._srdf_param = rospy.get_param("/robot_description_semantic")
                else:
                        Logger.logerror('Unable to get parameter: /robot_description_semantic')

                self._param_error = False
                self._srdf = None


        def execute(self, userdata):
                if self._param_error:
                        return 'failed'
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
                                        for index in range(len(self._current_position)):

                                                actual_delta = self._last_position[index] - self._current_position[index]
                                                if actual_delta > self._delta:
                                                        temp_success = False

                                        if temp_success == True:
                                                self._success = True
                                                return 'reached'
                
                if self._sub.has_msg(self._position_topic):

                        msg = self._sub.get_last_msg(self._position_topic)

                        #print msg.position

                        self._last_position = self._current_position
                        self._current_position = list(msg.position)
                        #print self._current_position

                        #for x in self._current_position:
                        #        print "\t", x

                        self._sub.remove_last_msg(self._position_topic)

                        #print self._joint_config     


        def on_enter(self, userdata):
                self._param_error     = False
                self._planning_failed = False
                self._control_failed  = False
                self._success         = False

                #self._position_topic  = "/m1n6s200_driver/joint_states"
                #self._delta           = 0.0000001
                self._sub             = ProxySubscriberCached({self._position_topic: JointState})
                self._current_position= []

                #Parameter check
                if self._srdf_param is None:
                        self._param_error = True
                        return

                try:
                        self._srdf = ET.fromstring(self._srdf_param)
                except Exception as e:
                        Logger.logwarn('Unable to parse given SRDF parameter: /robot_description_semantic')
                        self._param_error = True

                if not self._param_error:

                        robot = None
                        for r in self._srdf.iter('robot'):
                                if self._robot_name == '' or self._robot_name == r.attrib['name']:
                                        robot = r
                                        break
                        if robot is None:
                                Logger.logwarn('Did not find robot name in SRDF: %s' % self._robot_name)
                                return 'param_error'

                        config = None
                        for c in robot.iter('group_state'):
                                if (self._move_group == '' or self._move_group == c.attrib['group']) \
                                and c.attrib['name'] == self._config_name:
                                        config = c
                                        self._move_group = c.attrib['group']  # Set move group name in case it was not defined
                                        break
                        if config is None:
                                Logger.logwarn('Did not find config name in SRDF: %s' % self._config_name)
                                return 'param_error'

                        try:
                                self._joint_config = [float(j.attrib['value']) for j in config.iter('joint')]
                                self._joint_names  = [str(j.attrib['name']) for j in config.iter('joint')]
                        except Exception as e:
                                Logger.logwarn('Unable to parse joint values from SRDF:\n%s' % str(e))
                                return 'param_error'


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
                                userdata.action_topic = self._action_topic  # Save action topic to output key
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
