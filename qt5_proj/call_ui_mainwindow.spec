# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['call_ui_mainwindow.py'],
             pathex=['C:\\Users\\Lex Chen\\py_proj\\qt5_proj\\qt5_proj'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='call_ui_mainwindow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='line_chart_72px_1223234_easyicon.net.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='call_ui_mainwindow')
