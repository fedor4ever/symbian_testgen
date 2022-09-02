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

from datetime import datetime


timestamp = datetime.now().strftime('_%H_%M_%d_%m_%Y')

build_log = "build%s.log" %timestamp
build_err = "build%s.err" %timestamp
build_time = "build_time%s.log" %timestamp


def save2file(path, data, mode = 'w'):
   """Save list elements as strings. Save strings as is"""
   with open(path, mode) as f:
      if type(data) is list:
         for s in data:
            f.write(s + '\n')
      else:
         f.write(data)

def append2file(path, data):
   save2file(path, data, mode = 'a')

if __name__ == "__main__":
   print "This script holds together data used multiple modules."
