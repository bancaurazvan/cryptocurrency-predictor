#
# Copyright 2019 - Present Firebolt, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# utility.py
# This file will server as a utility file for our cryptocurrency predictor AI.
#
__author__ = "Firebolt, Inc."
__copyright__ = "Firebolt, Inc."
__version__ = "1.0.0"
__license__ = "MIT"

import datetime

class Counter():
    def __init__(self):
        self.start_counter = None
    
    def start(self):
        self.start_counter = datetime.datetime.now()
    
    def stop(self):
        stop_counter = datetime.datetime.now()
        print('Time It Took: %s' %(stop_counter - self.start_counter))