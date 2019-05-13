__author__ = "Firebolt, Inc."
__copyright__ = "Firebolt, Inc."
__version__ = "1.0.0"
__license__ = "MIT"

try:
    import subprocess
except EnvironmentError:
    print("Your Python 3 environment is correupted! Re-install Python 3!")

except EOFError:
    print("There was an unknown error with your system!")

except ImportError:
    print("Please install the evaluator essentials kit!")

except ImportWarning:
    print("Warning while importing the evaluator essentials kit!")
def start():
    print("Starting The Evaluator For Testing.")

    run_script()

def run_script():
    try:
        print("Running Evaluation Scripts!")
        subprocess.call("evaluation_test.sh")
        print("Successfully Ran Evaluation Script!")
    except EnvironmentError:
        print("Your Python 3 environment is correupted! Re-install Python 3!")

    except EOFError:
        print("There was an unknown error with your system!")

def stop():
    print("Successfully Tested Evaluation Scripts!")