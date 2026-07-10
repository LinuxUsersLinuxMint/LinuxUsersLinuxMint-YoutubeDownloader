#!/usr/bin/python3
""" Copyright© 2025-2026 OpenSoftware-World
OpenSoftware-World-YoutubeDownloader Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
OpenSoftware-World-YoutubeDownloader All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/OpenSoftware-World-YoutubeDownloader
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/OpenSoftware-World-YoutubeDownloader"""

import configparser

tray_config = configparser.ConfigParser()
tray_config.read('TrayMenu/tray.ini')

tray_visible = tray_config['TraySettings']['tray_visible']

if tray_visible == "True":
    tray_visible = True
else:
    tray_visible = False