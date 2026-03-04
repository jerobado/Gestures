# -*- mode: python ; coding: utf-8 -*-
# Use this file for development only
# Usage:
# > pyinstaller gestures-debug.spec --noconfirm
# or add --upx-dir=<path to UPX> if you want to compress the executable

import os

__appname__ = 'gestures'
__version__ = '2.1.0-develop'
_name = f'{__appname__}-{__version__}'

a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=__appname__,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=_name,
)
