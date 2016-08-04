import os

os.system("make")
os.system("git add *.html")
os.system("git add develop/content/*")
os.system("git commit -a -m \"Site update\"")
os.system("git push")
