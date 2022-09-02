This small package easy building test suite for ported libraries

Every exetutable for Symbian 9.1+ reqired registration resource file. Before build you should create project file per every test exe too. After building you need to install to device test suite. This require installer script - .pkg. May be you have not many tests - 2 or 3 - you may do it by hand and do not use that stuff.

For unlucky guys with many tests - give me a try. I tried to keep it small and simple.

How it works?
Preparation:
1. Copy symbian_testgen in you project source tree. Open build_tests.py. It is main configuration file.
 * uid_range_start - test apps UID range starts from hih. Be aware - no upper limits =)
 * tests - its siple
 * tests_installer_name - shows while istalling
 * project_path - where create project files to build
 * phone_menu_folder - specify folder in main menu where all tests shows
 * src_path - where tests sources are
 2. From test_builder copy tests_config.mmh where project_path points to. It contains shared data between all testing project files. Compiler, linker options etc.
 Additiomal customization for generation .pkg and .mmp see at pkg_addon_generator.py and prj_app_generator.py
 Building:
 Run build_tests.py and install <tests_installer_name>.sis.
 
 Enjoy!
 