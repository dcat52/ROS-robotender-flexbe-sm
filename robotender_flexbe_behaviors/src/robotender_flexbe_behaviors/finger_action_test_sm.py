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
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Oct 23 2017
@author: Davis Catherman, Shannon Enders
'''
class fingeractiontestSM(Behavior):
	'''
	finger action test. Simple test of finger action states.  Do the wave.
	'''


	def __init__(self):
		super(fingeractiontestSM, self).__init__()
		self.name = 'finger action test'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:922 y:113, x:674 y:345
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.OPEN = [0,6000]
		_state_machine.userdata.CLOSE = [6000,0]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:376 y:99
			OperatableStateMachine.add('CLOSE fingers',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'OPEN fingers', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'CLOSE'})

			# x:643 y:105
			OperatableStateMachine.add('OPEN fingers',
										FingerPositionState(result_topic="/m1n6s200_driver/fingers_action/finger_positions/result", action_topic="/m1n6s200_driver/fingers_action/finger_positions", robot_name="m1n6s200"),
										transitions={'reached': 'finished', 'failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'finger_values': 'OPEN'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
