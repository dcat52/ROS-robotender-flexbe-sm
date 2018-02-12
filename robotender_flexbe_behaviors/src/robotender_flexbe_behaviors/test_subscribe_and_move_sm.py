#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.decision_state import DecisionState
from robotender_kinova_flexbe_states.feedback_joint_state_to_moveit import FeedbackJointStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Feb 05 2018
@author: Davis,Shannon
'''
class testsubscribeandmoveSM(Behavior):
	'''
	test subscribe and move
	'''


	def __init__(self):
		super(testsubscribeandmoveSM, self).__init__()
		self.name = 'test subscribe and move'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:832 y:94, x:692 y:405
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_values_left = [4.824961332294557, 4.986228519472087, 2.016893253088309, 9.056585287421564, 1.7655888505129436, 2.5387597755555658]
		_state_machine.userdata.joint_values_right = [4.761117371482087, 4.435244724700612, 1.6085220010066865, 3.2511244744831167, 1.706054283818386, 2.4325377312649925]
		_state_machine.userdata.joint_names = ["m1n6s200_joint_1", "m1n6s200_joint_2", "m1n6s200_joint_3", "m1n6s200_joint_4", "m1n6s200_joint_5", "m1n6s200_joint_6"]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:106 y:117
			OperatableStateMachine.add('sub',
										SubscriberState(topic='/robotender', blocking=True, clear=False),
										transitions={'received': 'decide', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:280 y:116
			OperatableStateMachine.add('decide',
										DecisionState(outcomes=['go_left','go_right'], conditions=lambda x: "go_right" if x.data=="R" else "go_left"),
										transitions={'go_left': 'left', 'go_right': 'right'},
										autonomy={'go_left': Autonomy.Off, 'go_right': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:460 y:22
			OperatableStateMachine.add('left',
										FeedbackJointStateToMoveit(move_group="arm", action_topic="/move_group", robot_name="m1n6s200", position_topic='/m1n6s200_driver/joint_states', delta=1E-4),
										transitions={'reached': 'sub', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'joint_values': 'joint_values_left', 'joint_names': 'joint_names'})

			# x:452 y:234
			OperatableStateMachine.add('right',
										FeedbackJointStateToMoveit(move_group="arm", action_topic="/move_group", robot_name="m1n6s200", position_topic='/m1n6s200_driver/joint_states', delta=1E-4),
										transitions={'reached': 'sub', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'joint_values': 'joint_values_right', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	# [/MANUAL_FUNC]
