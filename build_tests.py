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

import test_builder

#All UID started with 0xA belongs to unprotected range. Read SDK help.
#They not used for regular apps and can't conflict with builtin apps
uid_range_start = 0xA0000020

tests = [
("multisrc-test", ["test1.cpp", "test1_.cpp"]),
("singlesrc-test", ["test2.cpp",]),
]

tests_installer_name = "my_tests_batch_wout_extension"

project_path = ""

phone_menu_folder = "" #tests_installer_name

src_path = ""

if __name__ == "__main__":
   test_builder.run(uid_range_start, tests, test_installer_name,
       project_path, phone_menu_folder, src_path)
