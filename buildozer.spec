[app]
title = MonAppKivy
package.name = monapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Icône (optionnel)
# icon.filename = %(source.dir)s/icon.png

requirements = python3,kivy
orientation = portrait

fullscreen = 1

# Permissions Android (ajoute selon ton besoin)
android.permissions = INTERNET

# Pour éviter les erreurs de compatibilité
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 
android.accept_sdk_license = True

# Utiliser la dernière toolchain stable
android.sdk = 28
android.archs = arm64-v8a, armeabi-v7a
android.sdk_version = 34
android.ndk_version = 26

# Empêche les erreurs de compilation liées à Cython
cython.min_version = 0.29.36

# Empêche les erreurs de compilation dans GitHub Actions
p4a.branch = master

# Empêche les erreurs de packaging
android.allow_backup = True

# Ajoute ton fichier main
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 0
