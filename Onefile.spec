# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\PythonProjects\Test_exe'],
             binaries=[],
             datas=[('D:/PythonProjects/Test_exe/venv/Lib/site-packages/mne/report/js_and_css', 'mne/report/js_and_css'),
             ('D:/PythonProjects/Test_exe/venv/Lib/site-packages/mne/icons/mne_icon-cropped.png', 'mne/icons'),
             ('D:/PythonProjects/Test_exe/icon.ico', '.')],  # здесь путь к файлу report.js
             hiddenimports=[],
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
          name='FreqApp',
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
          entitlements_file=None ,
          icon='D:/PythonProjects/Test_exe/icon.ico',
          )
