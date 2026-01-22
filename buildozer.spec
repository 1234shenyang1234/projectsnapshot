[app]

# (str) Title of your application
title = 项目随手�?
# (str) Package name
package.name = projectsnapshot

# (str) Package domain (needed for android/ios packaging)
package.domain = org.projectsnapshot

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
# Do not prefix with './' #source.exclude_patterns = license,images/*/*.png

# (str) Application versioning (method 1)
version = 2.0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,plyer,pillow==9.0.0,pygame==2.1.0

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
#services =


#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.0.0


#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names: red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray, darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy, olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/ for general documentation. #android.presplash_lottie = %(source.dir)s/data/presplash.lottie

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
android.permissions = CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible. android.api = 31

# (int) Minimum API your APK will support. android.minapi = 21

# (int) Android SDK version to use android.sdk = 20

# (str) Android NDK version to use android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21
android.ndk = 25.1.8937393
android.sdk = 33

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path = 

# (bool) If True, then skip trying to update the Android sdk 
# This can be useful to avoid excess Internet downloads or save time when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements. This is intended for automation only. If set to False, the default, you will be shown the license when first running a build.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = @android:style/Theme.NoTitleBar

# (list) Pattern to match in the console output to identify that the app crashed
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple arch at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters = 

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_x86_64 = libs/android-x86_64/*.so

# (list) Android additional java .jar files to add to the libs; appends to the list generated by requirements
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) Android additional java classes to add to the manifest. Remember to prefix with full package name.
#android.add_src = com.example.ExampleClass

# (str) Android logcat pattern
#android.logcat_patterns = *:S python:D

# (bool) Android logcat colors (not supported by all terminals)
android.logcat_colors = False

# (list) Android additional res folders to add to your apk
#android.add_resources = src/res,/path/to/extra/res

# (list) Android additional asset folders to add to your apk
#android.add_assets = src/assets,/path/to/extra/assets

# (list) Fonts to add to your apk (uses the same syntax as android.add_assets)
#android.add_fonts = fonts/[font1.ttf,font2.ttf]

# (list) Allows filtering of any of the minSdkVersion, targetSdkVersion, compileSdkVersion, and buildToolsVersion in build.gradle
# android.filtered_build_tools_version = "30.0.3"
# android.filtered_target_sdk_version = 30

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk


#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url = 

# (str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
#p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes = 

# (str) Filename to the hook for p4a
#p4a.hook = 

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port = 

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future" it will be passed to p4a by default. Set it to false to disable it
#p4a.setup_py = true

# (str) extra command line arguments to pass when invoking python-for-android
#p4a.extra_args = 


#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout: ios.kivy_ios_url = https://github.com/kivy/kivy-ios ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios-deploy
# Or specify URL and branch ios.ios_deploy_url = https://github.com/phonegap/ios-deploy ios.ios_deploy_branch = 1.10.0

# (bool) Whether or not to sign the code
ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing the release version
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url` options.
#ios.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download and installation
# This option should be defined along with `app_url` and `full_size_image_url` options.
#ios.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be used by iTunes
# This option should be defined along with `app_url` and `display_image_url` options.
#ios.manifest.full_size_image_url = 


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

# (list) The list of targets to build (i.e. android, ios, both)
targets = android

# (list) List of devices to test (when available) 
# android.device = emulator,192.168.1.1:5555

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) If true, then skip trying to update the android sdk 
# android.skip_update = False

# (str) Android sdk path to use 
# android.sdk_path = <path-to-your-sdk>

# (str) Android ndk path to use 
# android.ndk_path = <path-to-your-ndk>

# (str) Android ndk version to use 
# android.ndk_version = 23b

# (int) Android API to use. Should be as high as possible. 
# android.api = 31

# (int) Minimum API your app will support 
# android.minapi = 21

# (int) Android SDK version to use 
# android.sdk = 30

# (str) Android buildtools version to use 
# android.buildtools = 30.0.3

# (str) Android build tools version to use, 
# defaults to latest available in the sdk
# android.build_tools_version = 30.0.3

# (str) Python version to use (valid options are 2, 3, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12)
# android.python_version = 3.9

# (str) Python implementation to use (valid options are cpython, pypy3)
# android.python_implementation = cpython

# (bool) If True, then build with --release option
# android.release = False

# (bool) If True, then build with --debug option
# android.debug = False

# (str) The format used to package the app for release mode (aab or apk or aar)
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar)
# android.debug_artifact = apk

# (str) The format used to package the app for release mode (aab or apk or aar)
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar)
# android.debug_artifact = apk

# (list) List of files to ignore by the zip utility during the debug apk build
# android.debug_ignore_patterns = 

# (list) List of files to ignore by the zip utility during the release apk build
# android.release_ignore_patterns = 

# (str) The name of the custom target to use for the android build
# android.custom_target = debug

# (list) List of custom targets for the android build
# android.custom_targets = debug, release

# (str) The name of the custom target to use for the ios build
# ios.custom_target = debug

# (list) List of custom targets for the ios build
# ios.custom_targets = debug, release

# (list) List of files to ignore by the zip utility during the build
# ignore_patterns = 

# (str) The name of the custom target to use for the web build
# web.custom_target = debug

# (list) List of custom targets for the web build
# web.custom_targets = debug, release

# (str) The name of the custom target to use for the desktop build
# desktop.custom_target = debug

# (list) List of custom targets for the desktop build
# desktop.custom_targets = debug, release

# (str) The name of the custom target to use for the linux build
# linux.custom_target = debug

# (list) List of custom targets for the linux build
# linux.custom_targets = debug, release

# (str) The name of the custom target to use for the macos build
# macos.custom_target = debug

# (list) List of custom targets for the macos build
# macos.custom_targets = debug, release

# (str) The name of the custom target to use for the windows build
# windows.custom_target = debug

# (list) List of custom targets for the windows build
# windows.custom_targets = debug, release

# (list) List of files to ignore by the zip utility during the build
# ignore_patterns = 

# (bool) If True, then automatically accept SDK license agreements. This is intended for automation only. If set to False, the default, you will be shown the license when first running a build.
android.accept_sdk_license = True

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes = 

# (str) The directory in which python-for
