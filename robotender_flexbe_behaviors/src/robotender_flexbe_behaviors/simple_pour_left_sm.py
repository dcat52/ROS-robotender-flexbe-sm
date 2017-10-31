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
from robotender_kinova_flexbe_states.finger_position_state import FingerPositionState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Oct 20 2017
@author: Davis Catherman, Shannon Enders
'''
class SimplePourLeftSM(Behavior):
	'''
	Start at center -> prep pour -> pour -> post pour -> center -> release cup
	'''


	def __init__(self):
		super(SimplePourLeftSM, self).__init__()
		self.name = 'Simple Pour Left'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1250 y:404, x:625 y:387
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.center = [4.824961332294557, 4.986228519472087, 2.016893253088309, 9.056585287421564, 1.7655888505129436, 2.5387597755555658]
		_state_machine.userdata.prep_pour = [4.761117371482087, 4.435244724700612, 1.6085220010066865, 3.2511244744831167, 1.706054283818386, 2.4325377312649925]
		_state_machine.userdata.pour = [4.761121632539831, 4.435244724700612, 1.6085220010066865, 3.2511244744831167, 1.706051886973405, 4.577594147074765]
		_state_machine.userdata.post_pour = [4.761117371482087, 4.435244724700612, 1.6085220010066865, 3.2511244744831167, 1.706054283818386, 2.4325377312649925]
		_state_machine.userdata.joint_names = ["m1n6s200_joint_1", "m1n6s200_joint_2", "m1n6s200_joint_3", "m1n6s200_joint_4", "m1n6s200_joint_5", "m1n6s200_joint_6"]
		_state_machine.userdata.OPEN = [0,0]
		_state_machine.userdata.CLOSE = [5000,5000]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:67 y:41
			OperatableStateMachine.add('center1',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'Grasp', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:325 y:162
			OperatableStateMachine.add('prep pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prep_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:619 y:171
			OperatableStateMachine.add('pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'post pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:897 y:158
			OperatableStateMachine.add('post pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'center2', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'post_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1036 y:338
			OperatableStateMachine.add('release',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'finished', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})

			# x:1097 y:190
			OperatableStateMachine.add('center2',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'release', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:58 y:171
			OperatableStateMachine.add('Grasp',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'prep pour', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
