import os
import time
from subprocess import Popen

hard_test_dir = (os.getcwd() + "/tests/bin/hard/")
simple_test_dir = (os.getcwd() + "/tests/bin/simple/")

hard_tests = os.listdir(hard_test_dir)
simple_tests = os.listdir(simple_test_dir)

hard_tests.sort()
simple_tests.sort()

abs_path = os.path.split(os.getcwd())[
    0] + "/SimpleSimulator/SimpleSimulator.py"


Popen("rm myTraces -r -f".split())
print("Removed old traces")
time.sleep(0.2)

Popen(f"mkdir myTraces/hard -p".split())
Popen(f"mkdir myTraces/simple -p".split())
print("Created required directories".split())
time.sleep(0.2)

for i in hard_tests:
    Popen(f"touch myTraces/hard/{i}".split())
    Popen(f"python3 {abs_path} < {hard_test_dir}{i} > myTraces/hard/{i}".split())

for i in simple_tests:
    Popen(f"touch myTraces/simple/{i}".split())
    Popen(f"python3 {abs_path} < {simple_test_dir}{i} > myTraces/simple/{i}".split())
    
want_zip = input("Do you want to zip the folder as well? [y/n] : ")
if want_zip == 'y':
    Popen("rm -rf myTraces.zip".split())
    print("Removed previous zip file".split())
    time.sleep(0.2)
    Popen("zip -r myTraces myTraces".split())
    print("Created new zip file")
