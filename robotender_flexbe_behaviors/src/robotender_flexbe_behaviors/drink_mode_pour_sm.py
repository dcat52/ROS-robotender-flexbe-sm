#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robotender_kinova_flexbe_states.feedback_joint_state_to_moveit import FeedbackJointStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Nov 03 2017
@author: Davis Catherman, Shannon Enders
'''
class drinkmodepourSM(Behavior):
	'''
	drink mode pour with hard-coded positions
	'''


	def __init__(self):
		super(drinkmodepourSM, self).__init__()
		self.name = 'drink mode pour'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1228 y:87, x:486 y:352
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_names = ['m1n6s200_joint_1', 'm1n6s200_joint_2', 'm1n6s200_joint_3', 'm1n6s200_joint_4', 'm1n6s200_joint_5', 'm1n6s200_joint_6']
		_state_machine.userdata.pre_pour = [5.126004529284896, 4.489626207843922, 1.7224576250785655, 3.7321632727008596, 1.7839496151743317, 8.499195258647903]
		_state_machine.userdata.pour = [4.960468827512186, 4.2515385411264015, 1.6518825246109206, 3.919642356591386, 1.4049057588069342, 10.712974546387171]
		_state_machine.userdata.mid_pour = [5.013071052731214, 4.230059347986586, 1.6150925520481298, 3.96125265072722, 1.2587368307973903, 10.195214485162762]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:50 y:29
			OperatableStateMachine.add('pre pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'mid pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pre_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:686 y:58
			OperatableStateMachine.add('pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'post pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:349 y:41
			OperatableStateMachine.add('mid pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'mid_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:944 y:64
			OperatableStateMachine.add('post pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pre_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
