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
Created on Wed Nov 01 2017
@author: Davis Catherman, Shannon Enders
'''
class multiplecupspourbehaviorSM(Behavior):
	'''
	Pour to left cup from center, then pour to center cup from left cup. (loop possibilities)
	'''


	def __init__(self):
		super(multiplecupspourbehaviorSM, self).__init__()
		self.name = 'multiple cups pour behavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:958 y:78, x:24 y:694
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_names = ["m1n6s200_joint_1", "m1n6s200_joint_2", "m1n6s200_joint_3", "m1n6s200_joint_4", "m1n6s200_joint_5", "m1n6s200_joint_6"]
		_state_machine.userdata.center_values = [4.825370393837993, 4.804768712277358, 1.7884682005958692, 2.781744729201632, 1.7624776125694588, 2.5668808924540394]
		_state_machine.userdata.prep_pour_to_left = [4.8484381625680415, 4.172889801498073, 1.372345285529353, 3.0126762157540004, 1.4690217615247554, 2.627620406383804]
		_state_machine.userdata.pour_to_left = [4.610045297589599, 4.293199701639057, 1.419019181003809, 3.012844793851002, 1.4674078859041673, 4.845438377916176]
		_state_machine.userdata.post_pour_to_left = [4.8484381625680415, 4.172889801498073, 1.372345285529353, 3.0126762157540004, 1.4690217615247554, 2.627620406383804]
		_state_machine.userdata.left_values = [4.501794723496712, 4.784133474886988, 1.6909002314255626, 2.766800400744653, 1.8037183931040444, 2.543646143523643]
		_state_machine.userdata.prep_pour_to_center = [4.4696588912549435, 4.2865780179046835, 1.371823705429861, 2.7555946178259263, 1.6906042210704002, 2.5960829864389763]
		_state_machine.userdata.pour_to_center = [4.700331784865464, 4.265325726089742, 1.4461706409493849, 2.7535296027166787, 1.4171899888090882, 0.5029200288136196]
		_state_machine.userdata.post_pour_to_center = [4.4696588912549435, 4.2865780179046835, 1.371823705429861, 2.7555946178259263, 1.6906042210704002, 2.5960829864389763]
		_state_machine.userdata.OPEN = [0,0]
		_state_machine.userdata.CLOSE = [5000,5000]
		_state_machine.userdata.pre_grab_left = [4.616985495390345, 4.361768642857545, 0.8309522662125534, 2.772490244413607, 1.7511775537481435, 2.6507113446153356]
		_state_machine.userdata.back_off_center = [4.8380550301100405, 4.49428940291265, 1.2147491327564424, 2.784340512316133, 1.7494544885228622, 2.530367888644617]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:30 y:365, x:130 y:365, x:230 y:365, x:330 y:365
		_sm_stuff_0 = OperatableStateMachine(outcomes=['failed', 'planning_failed', 'control_failed', 'reached'], input_keys=['OPEN', 'CLOSE', 'center_values', 'prep_pour_to_left', 'pour_to_left', 'post_pour_to_left', 'back_off_center', 'joint_names'], output_keys=['joint_names'])

		with _sm_stuff_0:
			# x:41 y:57
			OperatableStateMachine.add('startopen',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'precenter', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})

			# x:246 y:134
			OperatableStateMachine.add('graspcenter',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'preppourleft', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})

			# x:244 y:63
			OperatableStateMachine.add('startcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'graspcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'center_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:453 y:58
			OperatableStateMachine.add('preppourleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'pourleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prep_pour_to_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:664 y:52
			OperatableStateMachine.add('pourleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'postpourleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pour_to_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:860 y:41
			OperatableStateMachine.add('postpourleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'endcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'post_pour_to_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1068 y:40
			OperatableStateMachine.add('endcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'releasecenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'center_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:30 y:213
			OperatableStateMachine.add('backoffcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'back_off_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:34 y:133
			OperatableStateMachine.add('precenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'startcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'back_off_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:1068 y:120
			OperatableStateMachine.add('releasecenter',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'backoffcenter', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})


		# x:30 y:365, x:130 y:365, x:230 y:365, x:330 y:365
		_sm_stuff_with_left_cup_1 = OperatableStateMachine(outcomes=['planning_failed', 'control_failed', 'failed', 'reached'], input_keys=['left_values', 'post_pour_to_center', 'pre_grab_left', 'joint_names', 'CLOSE', 'prep_pour_to_center', 'pour_to_center', 'OPEN'])

		with _sm_stuff_with_left_cup_1:
			# x:1156 y:40
			OperatableStateMachine.add('pregrableft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'left', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pre_grab_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:313 y:283
			OperatableStateMachine.add('postppourcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'left2', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'post_pour_to_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:549 y:280
			OperatableStateMachine.add('left2',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'releaseleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:608 y:142
			OperatableStateMachine.add('graspleft',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'preppourcenter', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})

			# x:298 y:199
			OperatableStateMachine.add('preppourcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'pourcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'prep_pour_to_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:30 y:243
			OperatableStateMachine.add('pourcenter',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'postppourcenter', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pour_to_center', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:797 y:266
			OperatableStateMachine.add('releaseleft',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'backoffleft', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})

			# x:1137 y:263
			OperatableStateMachine.add('backoffleft',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'reached', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'pre_grab_left', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})

			# x:876 y:95
			OperatableStateMachine.add('left',
										FeedbackJointStateToMoveit(position_topic="/m1n6s200_driver/joint_states", move_group="arm", action_topic="/move_group", robot_name="m1n6s200"),
										transitions={'reached': 'graspleft', 'planning_failed': 'planning_failed', 'control_failed': 'control_failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'left_values', 'joint_names': 'joint_names', 'move_group': 'move_group', 'action_topic': 'action_topic'})



		with _state_machine:
			# x:192 y:60
			OperatableStateMachine.add('stuff',
										_sm_stuff_0,
										transitions={'failed': 'failed', 'planning_failed': 'failed', 'control_failed': 'failed', 'reached': 'Stuff with left cup'},
										autonomy={'failed': Autonomy.Inherit, 'planning_failed': Autonomy.Inherit, 'control_failed': Autonomy.Inherit, 'reached': Autonomy.Inherit},
										remapping={'OPEN': 'OPEN', 'CLOSE': 'CLOSE', 'center_values': 'center_values', 'prep_pour_to_left': 'prep_pour_to_left', 'pour_to_left': 'pour_to_left', 'post_pour_to_left': 'post_pour_to_left', 'back_off_center': 'back_off_center', 'joint_names': 'joint_names'})

			# x:590 y:46
			OperatableStateMachine.add('Stuff with left cup',
										_sm_stuff_with_left_cup_1,
										transitions={'planning_failed': 'failed', 'control_failed': 'failed', 'failed': 'failed', 'reached': 'finished'},
										autonomy={'planning_failed': Autonomy.Inherit, 'control_failed': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'reached': Autonomy.Inherit},
										remapping={'left_values': 'left_values', 'post_pour_to_center': 'post_pour_to_center', 'pre_grab_left': 'pre_grab_left', 'joint_names': 'joint_names', 'CLOSE': 'CLOSE', 'prep_pour_to_center': 'prep_pour_to_center', 'pour_to_center': 'pour_to_center', 'OPEN': 'OPEN'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
