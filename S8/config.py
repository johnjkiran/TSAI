# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 02:19:02 2020

@author: SG0304944
"""

import pprint

class ModelConfig(object):

	def __init__(self,):
		super(ModelConfig, self).__init__()
		self.seed = 1
		self.batch_size_cuda = 64
		self.batch_size_cpu = 64	
		self.num_workers = 4
		self.epochs = 50
		self.dropout_value = 0.15

	def print_config(self):
		print("Model Parameters:")
		pprint.pprint(vars(self), indent=2)