[app]
title = MonAppKivy
package.name = monapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3==3.11.6,kivy==2.2.1
orientation = portrait
fullscreen = 1

# Android Permissions
android.permissions = INTERNET

# SDK and API Configuration
android.api = 34
android.minapi = 23
android.ndk = 25b
android.enable_androidx = True
android.accept_sdk_license = True


# SDK and Toolchain versions
android.sdk_version = 34
android.ndk_version = 25b
android.archs = arm64-v8a

# ✅ CRITICAL: Skip building pyjnius from source
android.skip_update = False
p4a.fork = kivy
p4a.branch = develop

# Cython version
cython.min_version = 0.29.36

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