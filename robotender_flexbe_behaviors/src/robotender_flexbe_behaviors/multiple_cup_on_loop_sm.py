#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robotender_flexbe_behaviors.multiple_cups_pour_behavior_using_containers_sm import multiplecupspourbehaviorusingcontainersSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Nov 02 2017
@author: Davis Catherman, Shannon Enders
'''
class multiplecuponloopSM(Behavior):
	'''
	loooped
	'''


	def __init__(self):
		super(multiplecuponloopSM, self).__init__()
		self.name = 'multiple cup on loop'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(multiplecupspourbehaviorusingcontainersSM, 'multiple cups pour behavior using containers')
		
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


		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:947 y:100, x:618 y:382
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:212 y:48
			OperatableStateMachine.add('multiple cups pour behavior using containers',
										self.use_behavior(multiplecupspourbehaviorusingcontainersSM, 'multiple cups pour behavior using containers'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
