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

# (string) Application versioning
version = 1.0.0

# (list) Application requirements
# بسیار مهم: اضافه شدن کتابخانه‌های امنیت شبکه برای جلوگیری از کرش در لودینگ
requirements = python3, kivy==master, git+https://github.com/kivymd/KivyMD.git@master, pillow, openssl, paramiko, pycryptodome, jnius, requests

# (string) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# مجوز دسترسی به اینترنت و بررسی وضعیت شبکه برای پایداری تونل SSH
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK API to use
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) The Android architectures for which to build the APK
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
