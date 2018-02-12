#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.get_joint_values_state import GetJointValuesState
from flexbe_states.log_key_state import LogKeyState
from flexbe_manipulation_states.moveit_to_joints_dyn_state import MoveitToJointsDynState
from flexbe_manipulation_states.srdf_state_to_moveit import SrdfStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Sep 13 2017
@author: Davis Catherman, Shannon Enders
'''
class logvaluesSM(Behavior):
	'''
	log values
	'''


	def __init__(self):
		super(logvaluesSM, self).__init__()
		self.name = 'log values'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:942 y:70, x:835 y:318
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.JV = [5.034934007384111, 4.749860722186541, 2.0863536874817012, 3.548160146665105, -4.830528404237258, -3.8607153900995290]
		_state_machine.userdata.JN = ["m1n6s200_joint_1", "m1n6s200_joint_2", "m1n6s200_joint_3", "m1n6s200_joint_4", "m1n6s200_joint_5", "m1n6s200_joint_6"]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:142 y:64
			OperatableStateMachine.add('Get_Values',
										GetJointValuesState(joints=["m1n6s200_joint_1", "m1n6s200_joint_2", "m1n6s200_joint_3", "m1n6s200_joint_4", "m1n6s200_joint_5", "m1n6s200_joint_6"], topic_name="/m1n6s200_driver/joint_states"),
										transitions={'retrieved': 'Log_Values'},
										autonomy={'retrieved': Autonomy.Off},
										remapping={'joint_values': 'joint_values'})

			# x:394 y:102
			OperatableStateMachine.add('Log_Values',
										LogKeyState(text='%d', severity=Logger.REPORT_HINT),
										transitions={'done': 'Go_Home'},
										autonomy={'done': Autonomy.Off},
										remapping={'data': 'joint_values'})

			# x:677 y:64
			OperatableStateMachine.add('Set_Specific_Vals',
										MoveitToJointsDynState(move_group="arm", action_topic='/move_group'),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'JV', 'joint_names': 'JN'})

			# x:505 y:209
			OperatableStateMachine.add('Go_Home',
										SrdfStateToMoveit(config_name="Home", move_group="arm", action_topic='/move_group', robot_name="m1n6s200"),
										transitions={'reached': 'Set_Specific_Vals', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
