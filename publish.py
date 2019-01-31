#!/usr/bin/env python

import os

os.system("cp -r develop/output/* .")
os.system("make")
os.system("git add .")

