# Copyright (C) 2022 Stryzhniou Fiodar

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import with_statement
import os, subprocess
from common_names import *


def makesis(pkg, path):
   print "pkg: %s" %pkg
   cmd = subprocess.Popen("makesis -v %s" %pkg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path, shell=True)
   out, err = cmd.communicate()
   # After cmd.communicate() we have ugly 'crcrlf' line endings
   append2file(build_log, out.replace("\r", ""))
   append2file(build_err, err.replace("\r", ""))

def build_installers(path):
   if path == "":
      path = os.getcwd()
   t = os.listdir(path)
   [makesis(pkg, path) for pkg in t if ".pkg" in pkg]

if __name__ == "__main__":
   build_installers("")
