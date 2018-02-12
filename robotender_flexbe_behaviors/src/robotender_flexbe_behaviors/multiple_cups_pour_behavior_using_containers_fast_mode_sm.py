#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robotender_kinova_flexbe_states.finger_position_state import FingerPositionState
from robotender_kinova_flexbe_states.feedback_joint_state_to_moveit import FeedbackJointStateToMoveit
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Nov 01 2017
@author: Davis Catherman, Shannon Enders
'''
class multiplecupspourbehaviorusingcontainersfastmodeSM(Behavior):
	'''
	Pour to left cup from center, then pour to center cup from left cup. (loop possibilities)
	'''


	def __init__(self):
		super(multiplecupspourbehaviorusingcontainersfastmodeSM, self).__init__()
		self.name = 'multiple cups pour behavior using containers fast mode'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:958 y:78, x:440 y:324
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_names = ["m1n6s200_joint_1", "m1n6s200_joint_2", "m1n6s200_joint_3", "m1n6s200_joint_4", "m1n6s200_joint_5", "m1n6s200_joint_6"]
		_state_machine.userdata.center_values = [4.825370393837993, 4.804768712277358, 1.7884682005958692, 2.781744729201632, 1.7624776125694588, 2.5668808924540394]
		_state_machine.userdata.prep_pour_to_left = [4.8484381625680415, 4.322889801498073, 1.372345285529353, 3.0126762157540004, 1.4690217615247554, 2.627620406383804]
		_state_machine.userdata.pour_to_left = [4.566518592733344, 4.3267512703163105, 1.393352300207898, -3.4085460570465727, 7.739404454396004, 4.906765118866303]
		_state_machine.userdata.post_pour_to_left = [4.8484381625680415, 4.322889801498073, 1.372345285529353, 3.0126762157540004, 1.4690217615247554, 2.627620406383804]
		_state_machine.userdata.left_values = [4.501794723496712, 4.784133474886988, 1.6909002314255626, 2.766800400744653, 1.8037183931040444, 2.543646143523643]
		_state_machine.userdata.prep_pour_to_center = [4.5690588912549435, 4.3365780179046835, 1.371823705429861, 2.7555946178259263, 1.6906042210704002, 2.5960829864389763]
		_state_machine.userdata.pour_to_center = [4.704875670317358, 4.372941136262645, 1.5029825249035005, -3.5267722999506783, 7.63555022663062, 0.3984061360462231]
		_state_machine.userdata.post_pour_to_center = [4.5690588912549435, 4.3365780179046835, 1.371823705429861, 2.7555946178259263, 1.6906042210704002, 2.5960829864389763]
		_state_machine.userdata.OPEN = [0,0]
		_state_machine.userdata.CLOSE = [6400,6400]
		_state_machine.userdata.pre_grab_left = [4.616985495390345, 4.361768642857545, 0.8309522662125534, 2.772490244413607, 1.7511775537481435, 2.6507113446153356]
		_state_machine.userdata.back_off_center = [4.8380550301100405, 4.49428940291265, 1.2147491327564424, 2.784340512316133, 1.7494544885228622, 2.530367888644617]
		_state_machine.userdata.mid_pour_center = [4.595038384847002, 4.374602948782854, 1.4727919986799805, -3.5220619669306554, 7.626154061672603, 1.4440939079313413]
		_state_machine.userdata.mid_pour_left = [4.639588276194066, 4.306920307575145, 1.3567719184228966, -3.3707214464002866, 7.72652274420329, 4.057045223556825]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:617 y:525, x:724 y:512, x:799 y:501, x:1346 y:582
		_sm_stuff_with_left_cup_0 = OperatableStateMachine(outcomes=['planning_failed', 'control_failed', 'failed', 'reached'], input_keys=['left_values', 'post_pour_to_center', 'pre_grab_left', 'joint_names', 'CLOSE', 'prep_pour_to_center', 'pour_to_center', 'OPEN', 'mid_pour_center'])

		with _sm_stuff_with_left_cup_0:
			# x:57 y:91
			OperatableStateMachine.add('pregrableft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'left', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pre_grab_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1058 y:196
			OperatableStateMachine.add('postppourcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'left2', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.High, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'post_pour_to_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1338 y:85
			OperatableStateMachine.add('left2',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'releaseleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:77 y:478
			OperatableStateMachine.add('graspleft',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'preppourcenter', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Low, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})

			# x:377 y:194
			OperatableStateMachine.add('preppourcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'mid pour', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.High, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prep_pour_to_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:832 y:195
			OperatableStateMachine.add('pourcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'postppourcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.High, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pour_to_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1356 y:253
			OperatableStateMachine.add('releaseleft',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'backoffleft', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})

			# x:1348 y:408
			OperatableStateMachine.add('backoffleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pre_grab_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:76 y:267
			OperatableStateMachine.add('left',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'graspleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:605 y:173
			OperatableStateMachine.add('mid pour',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'pourcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'mid_pour_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})


		# x:941 y:608, x:928 y:554, x:986 y:505, x:1150 y:560
		_sm_stuff_1 = OperatableStateMachine(outcomes=['failed', 'planning_failed', 'control_failed', 'reached'], input_keys=['OPEN', 'CLOSE', 'center_values', 'prep_pour_to_left', 'pour_to_left', 'post_pour_to_left', 'back_off_center', 'joint_names', 'mid_pour_left'], output_keys=['joint_names'])

		with _sm_stuff_1:
			# x:31 y:164
			OperatableStateMachine.add('startopen',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'precenter', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Low, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})

			# x:263 y:371
			OperatableStateMachine.add('graspcenter',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'preppourleft', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Low, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})

			# x:270 y:272
			OperatableStateMachine.add('startcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'graspcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'center_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:566 y:100
			OperatableStateMachine.add('preppourleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'midpourleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.High, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prep_pour_to_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1060 y:95
			OperatableStateMachine.add('pourleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'postpourleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.High, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pour_to_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1315 y:96
			OperatableStateMachine.add('postpourleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'endcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.High, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'post_pour_to_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1621 y:101
			OperatableStateMachine.add('endcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'releasecenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Low, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'center_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1613 y:419
			OperatableStateMachine.add('backoffcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'back_off_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:270 y:149
			OperatableStateMachine.add('precenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'startcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'back_off_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1625 y:262
			OperatableStateMachine.add('releasecenter',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'backoffcenter', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})

			# x:813 y:81
			OperatableStateMachine.add('midpourleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'pourleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'mid_pour_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})



		with _state_machine:
			# x:247 y:69
			OperatableStateMachine.add('stuff',
										_sm_stuff_1,
										transitions={'failed': 'failed', 'planning_failed': 'failed', 'control_failed': 'failed', 'reached': 'Stuff with left cup'},
										autonomy={'failed': Autonomy.Inherit, 'planning_failed': Autonomy.Inherit, 'control_failed': Autonomy.Inherit, 'reached': Autonomy.Inherit},
										remapping={'OPEN': 'OPEN', 'CLOSE': 'CLOSE', 'center_values': 'center_values', 'prep_pour_to_left': 'prep_pour_to_left', 'pour_to_left': 'pour_to_left', 'post_pour_to_left': 'post_pour_to_left', 'back_off_center': 'back_off_center', 'joint_names': 'joint_names', 'mid_pour_left': 'mid_pour_left'})

			# x:550 y:74
			OperatableStateMachine.add('Stuff with left cup',
										_sm_stuff_with_left_cup_0,
										transitions={'planning_failed': 'failed', 'control_failed': 'failed', 'failed': 'failed', 'reached': 'stuff'},
										autonomy={'planning_failed': Autonomy.Inherit, 'control_failed': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'reached': Autonomy.Inherit},
										remapping={'left_values': 'left_values', 'post_pour_to_center': 'post_pour_to_center', 'pre_grab_left': 'pre_grab_left', 'joint_names': 'joint_names', 'CLOSE': 'CLOSE', 'prep_pour_to_center': 'prep_pour_to_center', 'pour_to_center': 'pour_to_center', 'OPEN': 'OPEN', 'mid_pour_center': 'mid_pour_center'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
