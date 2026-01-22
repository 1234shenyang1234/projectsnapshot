[app]

title = ProjectSnapshot
package.name = projectsnapshot
package.domain = org.projectsnapshot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy==2.1.0,plyer,pillow==9.0.0,pygame==2.1.0
version = 2.0.1
orientation = portrait

# Android configuration
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 25.1.8937393
android.ndk_api = 21
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = "@android:style/Theme.NoTitleBar"
android.whitelist = *
android.private_storage = True
android.skip_update = True
android.logcat_filters = *:S python:D
android.copy_libs = 1
android.archs = arm64-v8a, armeabi-v7a

# p4a configuration
p4a.branch = master
p4a.bootstrap = sdl2
p4a.port = 5000
