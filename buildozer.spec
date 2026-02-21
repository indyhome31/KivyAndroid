[app]
title = MonAppKivy
package.name = monapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Android Permissions
android.permissions = INTERNET

# SDK and API Configuration
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# SDK and Toolchain versions
android.sdk_version = 34
android.ndk_version = 26
android.archs = arm64-v8a

# Cython version
cython.min_version = 0.29.36

# p4a configuration
p4a.branch = master
p4a.source_dir = 

# ✅ ADD THIS: Specify SDL2-based pyjnius to avoid build issues
android.entrypoint = org.kivy.android.PythonActivity
android.bootstrap = sdl2

# Android backup configuration
android.allow_backup = True

# Entry point
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 0