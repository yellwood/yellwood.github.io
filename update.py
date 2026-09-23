#!/usr/bin/env python3

import sys
import os
import re
import time
import io as StringIO
from subprocess import *
import tempfile

os.system('git pull')
os.system('git add *')
os.system('git commit -m "update"')
os.system('git push')
