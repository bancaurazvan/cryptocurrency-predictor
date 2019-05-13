#
# Copyright 2019 - Present Firebolt, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# main.py
# This file is the main file for the stock prediction.
#
__author__ = "Firebolt, Inc."
__copyright__ = "Firebolt, Inc."
__version__ = "1.0.0"
__license__ = "MIT"

import os
import math
import numpy as np
import datetime as dt
from numpy import newaxis
from core.utility import Counter
from keras.layers import Dense, Activation, Dropout, LSTM
from keras.models import Sequential, load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint

class Model():
    def __init__(self):
        self.model = Sequential()
    
    def load_model(self, data_file):
	    print('Loading Model: %s' % data_file)
	    self.model = load_model(data_file)

    def build_model(self, configs):
	    timer = Counter()
	    timer.start()

    def train(self, x, y, epochs, batch_size, save_dir):
        pass
    
    def train_generator(self, data_gen, epochs, batch_size, steps_per_epoch, save_dir):
        pass
    
    def predict_point_by_point(self, data):
        pass
    
    def predict_sequences_multiple(self, data, window_size, prediction_len):
        pass
    
    def predict_sequence_full(self, data, window_size):
        pass