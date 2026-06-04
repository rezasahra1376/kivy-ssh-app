[app]

# (string) Title of your application
title = SSH Tunnel Manager

# (string) Package name
package.name = sshtunnelmanager

# (string) Package domain (needed for android packaging)
package.domain = org.sshapp

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (string) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# بسیار مهم: کتابخانه‌های مورد نیاز برنامه شما در اندروید
requirements = python3, kivy==master, git+https://github.com/kivymd/KivyMD.git@master, pillow, openssl, requests

# (str) Custom source for roms, light or dark theme
# (string) Presplash of the application (لوگوی اولیه هنگام باز شدن برنامه)
# presplash.filename = %(source.dir)s/presplash.png

# (string) Icon of the application (آیکون برنامه)
# icon.filename = %(source.dir)s/icon.png

# (string) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# مجوز دسترسی به اینترنت برای برقراری اتصال SSH
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
# نسخه اندرویدی که برنامه برای آن بهینه می‌شود (معمولاً 33 یا 34)
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) The Android architectures for which to build the APK
# معماری پردازنده‌هایی که فایل APK برای آن‌ها ساخته می‌شود
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
