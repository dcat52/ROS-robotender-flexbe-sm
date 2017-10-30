#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
from flexbe_manipulation_states.moveit_to_joints_state import MoveitToJointsState
from flexbe_manipulation_states.get_joint_values_state import GetJointValuesState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Sep 06 2017
@author: Davis Catherman, Shannon Enders
'''
class Move_To_Retrieved_PostionSM(Behavior):
	'''
	Workflow: Go_Home --> Get_Joint_Values --> Go_Retract --> Go_To_Retrieved_Values
	'''


	def __init__(self):
		super(Move_To_Retrieved_PostionSM, self).__init__()
		self.name = 'Move_To_Retrieved_Postion'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1108 y:307, x:1120 y:6
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:111 y:81
			OperatableStateMachine.add('Go_Home_Position',
										SrdfStateToMoveit(config_name="Home", move_group="arm", action_topic='/move_group', robot_name="m1n6s200"),
										transitions={'reached': 'Get_Joint_Values', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values2', 'joint_names': 'joint_names'})

			# x:561 y:79
			OperatableStateMachine.add('Go_Retract_Position',
										SrdfStateToMoveit(config_name="Retract", move_group="arm", action_topic='/move_group', robot_name="m1n6s200"),
										transitions={'reached': 'Move_to_Retrieved_Joint_Values', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values2', 'joint_names': 'joint_names'})

			# x:771 y:209
			OperatableStateMachine.add('Move_to_Retrieved_Joint_Values',
										MoveitToJointsState(move_group="arm", joint_names=["m1n6s200_joint_1","m1n6s200_joint_2","m1n6s200_joint_3","m1n6s200_joint_4","m1n6s200_joint_5","m1n6s200_joint_6","m1n6s200_joint_finger_1","m1n6s200_joint_finger_2"], action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'joint_values'})

			# x:343 y:208
			OperatableStateMachine.add('Get_Joint_Values',
										GetJointValuesState(joints=["m1n6s200_joint_1","m1n6s200_joint_2","m1n6s200_joint_3","m1n6s200_joint_4","m1n6s200_joint_5","m1n6s200_joint_6","m1n6s200_joint_finger_1","m1n6s200_joint_finger_2"], topic_name="/m1n6s200_driver/joint_states"),
										transitions={'retrieved': 'Go_Retract_Position'},
										autonomy={'retrieved': Autonomy.Off},
										remapping={'joint_values': 'joint_values'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	# [/MANUAL_FUNC]
