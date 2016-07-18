#!/usr/bin/env python
# Must commit all the changes to master, before change the branch
import os

os.popen("git checkout master")
os.mkdir("../temp/")
os.popen("cp output -r ../temp/")
os.popen("git checkout gh-pages")
os.popen("cp ../temp/output/* -r .")
os.popen("rm ../temp -r")
