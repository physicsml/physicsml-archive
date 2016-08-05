#!/usr/bin/env python

import os

os.system("make")
os.system("git add *.html")
os.system("git add author/*.html")
os.system("git add category/*.html")
os.system("git add tag/*.html")
os.system("git add develop/content/*")
os.system("git commit -a -m \"Site update\"")
#os.system("git push")
