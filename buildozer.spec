[app]
title = SSH Tunnel Manager
package.name = sshtunnelmanager
package.domain = org.sshapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0

# لیست کتابخانه‌های الزامی (نسخه‌های کاملاً پایدار شده)
requirements = python3, kivy==master, git+https://github.com/kivymd/KivyMD.git@master, pillow, jnius, openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
