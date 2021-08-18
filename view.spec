# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['view.py'],
             pathex=['C:\\Users\\nuigu\\Documents\\program\\study-03-desktop-01-master-main'],
             binaries=[],
             datas=[('C:\\Users\\nuigu\\Documents\\program\\venv\\lib\\site-packages\\eel\\eel.js', 'eel'), ('html', 'html')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='view',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
