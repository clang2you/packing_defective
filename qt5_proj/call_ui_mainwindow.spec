# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['call_ui_mainwindow.py'],
             pathex=['.\\ConfigHelper\\config_helper.py', '.\\DbHelper\\db_helper.py', 'C:\\Users\\lex\\py_proj\\packing_defective\\qt5_proj'],
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
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='call_ui_mainwindow')
