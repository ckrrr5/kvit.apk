[app]
p4a.source_dir = .buildozer/android/platform/python-for-android

title = PyShell
package.name = thepyshell
package.domain = org.thepyshell
source.dir = .
source.include_exts = py

version = 0.1

android.src_dir = android/src
android.jni_dir = android/jni
requirements = python3,kivy
android.api = 33
android.ndk = 25b
android.archs = arm64‑v8a

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
