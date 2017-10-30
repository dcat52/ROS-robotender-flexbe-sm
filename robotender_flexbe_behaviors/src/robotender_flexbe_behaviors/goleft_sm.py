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
from flexbe_manipulation_states.joint_state_to_moveit import JointStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Oct 05 2017
@author: davisshannon
'''
class goLeftSM(Behavior):
	'''
	cup left
	'''


	def __init__(self):
		super(goLeftSM, self).__init__()
		self.name = 'goLeft'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1204 y:222, x:498 y:264
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_values1 = [3.6101066052, 4.75188046356, 1.07972986155, 1.21694317802, 2.24516011381, 1.83854561594]
		_state_machine.userdata.joint_values2 = [4.874892939572453, 4.363024855943735, 1.1921655267125706, 2.7607065555383334, 1.8676212097766047, 8.829414450644498]
		_state_machine.userdata.joint_values3 = [5.851354801687673, 4.864461337582612, 1.0885434600152142, 2.0525195574127895, 4.140473804709629, 1.3734302573574513, 0.16385561330951914, 0.16508762491930343]
		_state_machine.userdata.joint_values_preppourL = [4.761117371482087, 4.435244724700612, 1.6085220010066865, 3.2511244744831167, 1.706054283818386, 2.4325377312649925]
		_state_machine.userdata.joint_values_pourL = [4.761121632539831, 4.435244724700612, 1.6085220010066865, 3.2511244744831167, 1.706051886973405, 4.577594147074765]
		_state_machine.userdata.joint_values2_IN = [4.857230855223047, 4.862187530643903, 1.8024411410452421, 2.7714042073210727, 1.7851791966496213, 8.812876220275106]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:56 y:94
			OperatableStateMachine.add('srdf home',
										SrdfStateToMoveit(config_name="Home", move_group="arm", action_topic='/move_group', robot_name="m1n6s200"),
										transitions={'reached': 'staticCenter', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:631 y:100
			OperatableStateMachine.add('staticLEFT',
										JointStateToMoveit(),
										transitions={'reached': 'staticRight', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values1', 'joint_names': 'joint_names'})

			# x:53 y:281
			OperatableStateMachine.add('staticCenter',
										JointStateToMoveit(),
										transitions={'reached': 'staticCenterIN', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values2', 'joint_names': 'joint_names'})

			# x:1005 y:195
			OperatableStateMachine.add('staticRight',
										JointStateToMoveit(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values3', 'joint_names': 'joint_names'})

			# x:310 y:426
			OperatableStateMachine.add('PrepPourLeftCup',
										JointStateToMoveit(),
										transitions={'reached': 'PourLeftCup', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values_preppourL', 'joint_names': 'joint_names'})

			# x:567 y:445
			OperatableStateMachine.add('PourLeftCup',
										JointStateToMoveit(),
										transitions={'reached': 'AfterPour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values_pourL', 'joint_names': 'joint_names'})

			# x:772 y:472
			OperatableStateMachine.add('AfterPour',
										JointStateToMoveit(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values_preppourL', 'joint_names': 'joint_names'})

			# x:55 y:491
			OperatableStateMachine.add('staticCenterIN',
										JointStateToMoveit(),
										transitions={'reached': 'PrepPourLeftCup', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values2_IN', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
