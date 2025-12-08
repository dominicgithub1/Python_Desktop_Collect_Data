# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    # file chính của bạn. 
    # Windows: dist\\main.py
    # Linux/MacOS: dist/main.py
    ['dist\\main.py'],
    # đường dẫn gốc của project <your source code path>/AdapterApp
    # khi sử dụng pyarmor, thì pathex trỏ vào thư mục <your source code path>/dist/main.py
    pathex=['<your source code path>/AdapterApp/dist/main.py'],  
    binaries=[],
    #datas=[('config.json.enc', '.'),('dist/pyarmor_runtime_000000/*', 'pyarmor_runtime_000000')], 
    datas=[
        ('config.json.enc', '.'),
        ('dist/pyarmor_runtime_000000/*', 'pyarmor_runtime_000000'),
        ('dist/ui/*', 'ui'),
        ('dist/infrastructure/*', 'infrastructure'),
        ('dist/extension/*','extension')
        ],
    hiddenimports=[
        'pyodbc',
        'pandas',
        'pandas._libs',
        'numpy',
        'PySide6',
        'PySide6.QtWidgets',
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'getpass',
        'cryptography', # python-oracledb đang chạy ở thin mode thì cần import thư viện cryptography để hoạt động
        'cryptography.fernet',
        'cryptography.hazmat',
        'cryptography.x509',
        'cryptography.hazmat.backends',
        'cryptography.hazmat.primitives',
        'cryptography.hazmat.primitives.ciphers',
        'cryptography.hazmat.primitives.kdf',
        'cryptography.hazmat.primitives.kdf.pbkdf2'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ANix',        # tên file exe
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,        # đổi thành False nếu bạn muốn ẩn console (GUI app)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ANix'
)
