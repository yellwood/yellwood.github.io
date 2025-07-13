#!/usr/bin/env python

import sys
import os
import re
import time
import StringIO
from subprocess import *
import tempfile

os.system('git add *')
os.system('git commit -m "update"')
os.system('git push')
