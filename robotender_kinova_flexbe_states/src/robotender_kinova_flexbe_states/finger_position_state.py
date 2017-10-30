#!/usr/bin/env python

import rospy

import actionlib

from flexbe_core import EventState, Logger

from flexbe_core.proxy import ProxyActionClient

from flexbe_core.proxy import ProxySubscriberCached

from moveit_msgs.msg import MoveGroupAction, MoveGroupGoal, Constraints, JointConstraint, MoveItErrorCodes

from kinova_msgs.msg import SetFingersPositionAction, FingerPosition, SetFingersPositionGoal

'''
created on: 10-19-2017
@author: davis catherman
@author: shannon enders
'''

class FingerPositionState(EventState):
        '''
        State to send a joint state configuration to MoveIt to plan and move.

        -- position_topic       string              Name of topic for joint states.

        -- action_topic         string              Topic on which MoveIt is listening for action calls.

        -- robot_name           string              Optional name of the robot to be used.
                                                                If left empty, the first one found will be used
                                                                (only required if multiple robots are specified in the same file).

        ># finger_names          string[]            Names of the target fingers.
                                                                        Same order as their corresponding names in finger_values.

        ># finger_values         float[]             Target configuration of the fingers.
                                                                        Same order as their corresponding names in finger_names.

        '''


        def __init__(self, result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"):
                '''
                Constructor
                '''
                super(FingerPositionState, self).__init__(input_keys=['finger_values'],
                                                        outcomes=['reached', 'failed'])


                self._result_topic  = result_topic
                self._action_topic    = action_topic
                self._robot_name   = robot_name

        def execute(self, userdata):
                '''
                Execute this state
                '''

                self.send_goal()

                if self._failed:
                        return 'failed'
                if self._success:
                        return 'reached'

        def on_enter(self, userdata):
                self._failed          = False
                self._success         = False
                self._finger_config   = userdata.finger_values

                #self._sub             = ProxySubscriberCached({self._result_topic: JointState})

                #self._client = ProxyActionClient({self._action_topic: MoveGroupAction})

        def on_stop(self):
                try:
                        pass
                except:
                        # client already closed
                        pass

        def on_pause(self):
                #self._client.cancel(self._action_topic)
                try:
                        pass
                except:
                        pass

        def on_resume(self, userdata):
                self.on_enter(userdata)


        def send_goal(self):
            """Send a gripper goal to the action server."""

            client = actionlib.SimpleActionClient(self._action_topic, SetFingersPositionAction)
            client.wait_for_server()

            goal = SetFingersPositionGoal()

            goal.fingers.finger1 = float(self._finger_config[0])
            goal.fingers.finger2 = float(self._finger_config[1])

            client.send_goal(goal)

            if client.wait_for_result(rospy.Duration(5.0)):
                self._success = True
                return client.get_result()