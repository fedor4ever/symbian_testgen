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
import os, subprocess, Queue, threading, errno, time
import multiprocessing as mp

from common_names import *

# Workaround for "threading bug in strptime"
# See - https://stackoverflow.com/questions/32245560/module-object-has-no-attribute-strptime-with-several-threads-python/46401422
import _strptime

prj_template = "PRJ_MMPFILES\n%s"
prj_path = "paralell_build"

def thread_func(q):
   while True:
      dir = q.get()
      if dir is None:  # EOF?
         return
      cmd = subprocess.Popen('bldmake bldfiles', stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, shell=True)
      out, err = cmd.communicate()
      # Clean build directory from previous build.
      cmd = subprocess.Popen('abld reallyclean gcce urel', stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, shell=True)
      cmd.communicate()

      # Needed because datetime.now() returns the same time for every call.
      start = time.strftime("%H:%M:%S")
      cmd1 = subprocess.Popen('abld build gcce urel', stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dir, shell=True)
      out1, err1 = cmd1.communicate()

      end = time.strftime("%H:%M:%S" )
      start_dt = datetime.strptime(start, '%H:%M:%S')
      end_dt = datetime.strptime(end, '%H:%M:%S')
      diff = (end_dt - start_dt)

      out = out + out1
      err = err + err1

      # I hope it correctly stores logs in parallel tasks.
      # After cmd.communicate() we have ugly 'crcrlf' line endings.
      append2file(build_log, out.replace("\r", ""))
      append2file(build_err, err.replace("\r", ""))
      append2file(build_time, "Target %s build time: %s.\n" %(dir, str(diff)) )
      print "Target %s done!" %dir

def build_apps(path):
   if path == "":
      path = os.getcwd()
      # raise ValueError("Path to test app sources not set!")
   nodes = os.listdir(path)
   q = Queue.Queue()
   for x in nodes:
      dir = os.path.join(path, x)
      if os.path.isdir(dir):
         q.put(dir)

   t_count = mp.cpu_count() + 2
   if t_count > q.qsize():
      t_count = q.qsize()

   print "Queue size: %s" %q.qsize()
   print "Thread count: %s" %t_count
   threads = [threading.Thread(target=thread_func, args=(q,)) for i in range(t_count)]
   for thread in threads:
      thread.start()
      q.put(None)  # One EOF marker for each thread.
   for thread in threads:
      thread.join()

if __name__ == "__main__":
   build_apps("")
