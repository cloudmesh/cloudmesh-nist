#! /usr/bin/env python

# ../bin/cat_controlers.py keystore profile

import sys, os
for controller in sys.argv[1:]:
  try:
    filename = os.path.join("services", controller, controller + "_controller.py")
    print ("#" + filename)
    with open(filename, 'r') as _file:
      for line in iter((_file.readline), ""):
        print (line, end="")
  except IOError as _err:
    sys.stderr.write(os.path.basename(sys.argv[0]) + ": " + controller +
    ": " + _err.strerror + "\n")
