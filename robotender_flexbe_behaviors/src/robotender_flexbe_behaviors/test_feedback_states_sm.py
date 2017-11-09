#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robotender_kinova_flexbe_states.feedback_srdf_state_to_moveit import FeedbackSrdfStateToMoveit
from robotender_kinova_flexbe_states.feedback_joint_state_to_moveit import FeedbackJointStateToMoveit
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Oct 18 2017
@author: Davis Catherman, Shannon Enders
'''
class testfeedbackstatesSM(Behavior):
	'''
	test feedback moveit states for full autonomoy of the robotender
	'''


	def __init__(self):
		super(testfeedbackstatesSM, self).__init__()
		self.name = 'test feedback states'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1132 y:61, x:520 y:383
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_names_test = ["m1n6s200_joint_1", "m1n6s200_joint_2", "m1n6s200_joint_3", "m1n6s200_joint_4", "m1n6s200_joint_5", "m1n6s200_joint_6"]
		_state_machine.userdata.joint_values_test = [5.851354801687673, 4.864461337582612, 1.0885434600152142, 2.0525195574127895, 4.140473804709629, 1.3734302573574513]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:111 y:45
			OperatableStateMachine.add('home',
										FeedbackSrdfStateToMoveit(config_name="Home", move_group="arm", action_topic='/move_group', robot_name="m1n6s200", position_topic='/m1n6s200_driver/joint_states', delta=1E-7),
										transitions={'reached': 'Testing ', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off})

			# x:457 y:49
			OperatableStateMachine.add('Testing ',
										FeedbackJointStateToMoveit(move_group="arm", action_topic="/move_group", robot_name="m1n6s200", position_topic="/m1n6s200_driver/joint_states", delta=1E-7),
										transitions={'reached': 'go home2', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'joint_values': 'joint_values_test', 'joint_names': 'joint_names_test'})

			# x:803 y:55
			OperatableStateMachine.add('go home2',
										SrdfStateToMoveit(config_name="Home", move_group="arm", action_topic='/move_group', robot_name="m1n6s200"),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
