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
Created on Fri Nov 03 2017
@author: Davis Catherman
'''
class mixerdemoSM(Behavior):
	'''
	mixer for use with food coloring as demo.

Requires 3 cups.
	'''


	def __init__(self):
		super(mixerdemoSM, self).__init__()
		self.name = 'mixer demo'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1201 y:538, x:404 y:334
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_names = ['m1n6s200_joint_1', 'm1n6s200_joint_2', 'm1n6s200_joint_3', 'm1n6s200_joint_4', 'm1n6s200_joint_5', 'm1n6s200_joint_6']
		_state_machine.userdata.joint_values = [5.013071052731214, 4.230059347986586, 1.6150925520481298, 3.96125265072722, 1.2587368307973903, 10.195214485162762]
		_state_machine.userdata.left_lift = [5.065078327762718, 4.076029034755237, 0.9997600608585886, 3.7334871300787382, 1.8222228353062417, 8.792189850191805]
		_state_machine.userdata.left_cup = [4.789882174416034, 4.891706540798559, 1.8607510531125273, 3.4168710986141604, 1.8134044431467171, 8.788656900689706]
		_state_machine.userdata.CLOSE = [6400,6400]
		_state_machine.userdata.prepost_pour = [4.87152191026463, 4.381388416924268, 1.4040867036136804, 3.1928864677652644, 1.7481033337438106, 8.741622280045599]
		_state_machine.userdata.mid_pour = [4.773423306247126, 4.387238050258627, 1.375200194217918, 3.1306545183606196, 1.5138697937558532, 7.627375919980731]
		_state_machine.userdata.finish_pour = [4.778883319114006, 4.319199078097064, 1.3984297499841885, 2.961141918132095, 1.5586557743335523, 6.81882529933057]
		_state_machine.userdata.OPEN = [0,0]
		_state_machine.userdata.right_lift = [5.739989927016048, 4.351818274076682, 1.1057325669550215, 3.5978672494631065, 1.9470734251058108, 2.586587751888408]
		_state_machine.userdata.right_cup = [5.487217590047831, 4.894399529292847, 1.814038009170047, 3.419528667065951, 1.9052846991769412, 2.5484829766954453]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:1175 y:485, x:467 y:379
		_sm_pour_to_center_right_0 = OperatableStateMachine(outcomes=['reached', 'failed'], input_keys=['prepost_pour', 'mid_pour', 'joint_names', 'finish_pour', 'left_lift'])

		with _sm_pour_to_center_right_0:
			# x:121 y:147
			OperatableStateMachine.add('begin pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'mid pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prepost_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:385 y:146
			OperatableStateMachine.add('mid pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'finish pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'mid_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:660 y:159
			OperatableStateMachine.add('finish pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'upright', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'finish_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:935 y:163
			OperatableStateMachine.add('upright',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'init state', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prepost_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:976 y:318
			OperatableStateMachine.add('init state',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})


		# x:360 y:407, x:911 y:461
		_sm_right_grab_1 = OperatableStateMachine(outcomes=['failed', 'reached'], input_keys=['joint_names', 'right_lift', 'right_cup', 'CLOSE', 'left_lift'])

		with _sm_right_grab_1:
			# x:27 y:135
			OperatableStateMachine.add('right lifted no cup',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'right cup', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'right_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:243 y:132
			OperatableStateMachine.add('right cup',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'CLOSE', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'right_cup', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:471 y:131
			OperatableStateMachine.add('CLOSE',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'right lifted w cup', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})

			# x:706 y:124
			OperatableStateMachine.add('right lifted w cup',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'init location', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'right_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:783 y:233
			OperatableStateMachine.add('init location',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})


		# x:525 y:426, x:1076 y:348
		_sm_release_2 = OperatableStateMachine(outcomes=['failed', 'reached'], input_keys=['left_cup', 'OPEN', 'joint_names', 'left_lift'])

		with _sm_release_2:
			# x:89 y:157
			OperatableStateMachine.add('prep place',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'place', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:307 y:168
			OperatableStateMachine.add('place',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'open', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_cup', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:544 y:171
			OperatableStateMachine.add('open',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'clear cup', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})

			# x:818 y:175
			OperatableStateMachine.add('clear cup',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})


		# x:1252 y:251, x:609 y:359
		_sm_pour_to_center_3 = OperatableStateMachine(outcomes=['reached', 'failed'], input_keys=['prepost_pour', 'mid_pour', 'joint_names', 'finish_pour'])

		with _sm_pour_to_center_3:
			# x:121 y:147
			OperatableStateMachine.add('begin pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'mid pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prepost_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:385 y:146
			OperatableStateMachine.add('mid pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'finish pour', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'mid_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:660 y:159
			OperatableStateMachine.add('finish pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'upright', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'finish_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:977 y:157
			OperatableStateMachine.add('upright',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prepost_pour', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})


		# x:465 y:367, x:1128 y:309
		_sm_left_grab_4 = OperatableStateMachine(outcomes=['failed', 'reached'], input_keys=['joint_values', 'joint_names', 'left_lift', 'CLOSE', 'left_cup'])

		with _sm_left_grab_4:
			# x:72 y:150
			OperatableStateMachine.add('left lift no cup',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'left cup', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:315 y:153
			OperatableStateMachine.add('left cup',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'CLOSE', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_cup', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:858 y:155
			OperatableStateMachine.add('left lift',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_lift', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:584 y:154
			OperatableStateMachine.add('CLOSE',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'left lift', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})



		with _state_machine:
			# x:262 y:63
			OperatableStateMachine.add('left grab',
										_sm_left_grab_4,
										transitions={'failed': 'failed', 'reached': 'pour to center'},
										autonomy={'failed': Autonomy.Inherit, 'reached': Autonomy.Inherit},
										remapping={'joint_values': 'joint_values', 'joint_names': 'joint_names', 'left_lift': 'left_lift', 'CLOSE': 'CLOSE', 'left_cup': 'left_cup'})

			# x:468 y:60
			OperatableStateMachine.add('pour to center',
										_sm_pour_to_center_3,
										transitions={'reached': 'release', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'prepost_pour': 'prepost_pour', 'mid_pour': 'mid_pour', 'joint_names': 'joint_names', 'finish_pour': 'finish_pour'})

			# x:727 y:48
			OperatableStateMachine.add('release',
										_sm_release_2,
										transitions={'failed': 'failed', 'reached': 'right grab'},
										autonomy={'failed': Autonomy.Inherit, 'reached': Autonomy.Inherit},
										remapping={'left_cup': 'left_cup', 'OPEN': 'OPEN', 'joint_names': 'joint_names', 'left_lift': 'left_lift'})

			# x:917 y:106
			OperatableStateMachine.add('right grab',
										_sm_right_grab_1,
										transitions={'failed': 'failed', 'reached': 'pour to center right'},
										autonomy={'failed': Autonomy.Inherit, 'reached': Autonomy.Inherit},
										remapping={'joint_names': 'joint_names', 'right_lift': 'right_lift', 'right_cup': 'right_cup', 'CLOSE': 'CLOSE', 'left_lift': 'left_lift'})

			# x:1038 y:230
			OperatableStateMachine.add('pour to center right',
										_sm_pour_to_center_right_0,
										transitions={'reached': 'finished', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'prepost_pour': 'prepost_pour', 'mid_pour': 'mid_pour', 'joint_names': 'joint_names', 'finish_pour': 'finish_pour', 'left_lift': 'left_lift'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
