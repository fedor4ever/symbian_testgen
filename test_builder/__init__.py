#!/usr/bin/env python2

# Copyright (C) 2022 Stryzhniou Fiodar

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.


import time
from datetime import datetime
from common_names import *


from app_builder import build_apps
from installer_builder import build_installers
from pkg_addon_generator import create_addon_pkg
from prj_app_generator import create_app_mmps

def run(uid_range_start, tests, test_installer_name,
       project_path, phone_menu_folder, src_path,
       test_log_folder):
    log = "Build tests started at: %s\n" %time.ctime()
    save2file(build_log, log)
    save2file(build_err, '')

    create_app_mmps(project_path, tests, uid_range_start, phone_menu_folder, src_path)
    create_addon_pkg(project_path, tests, uid_range_start, test_installer_name, test_log_folder)
    build_apps(project_path)
    build_installers(project_path)

    log = "Build tests ended at: %s\n" %time.ctime()
    save2file(build_log, log, 'a')
