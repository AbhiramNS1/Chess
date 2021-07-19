# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Binu bot\\Desktop\\chess in tkinter\\New folder'],
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

a.datas+=[("logo.ico",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\logo.ico","DATA")]
a.datas+=[("u0.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\u0.png","DATA")]

a.datas+=[("im.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\im.png","DATA")]
a.datas+=[("Key\Brock.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Brock.png","DATA")]
a.datas+=[("Key\Wrock.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Wrock.png","DATA")]
a.datas+=[("Key\Bhorse.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Bhorse.png","DATA")]
a.datas+=[("Key\Belephant.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Belephant.png","DATA")]
a.datas+=[("Key\Whorse.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Whorse.png","DATA")]
a.datas+=[("Key\Welephant.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Welephant.png","DATA")]
a.datas+=[("Key\Bking.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Bking.png","DATA")]
a.datas+=[("Key\Wking.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Wking.png","DATA")]
a.datas+=[("Key\Bqueen.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Bqueen.png","DATA")]
a.datas+=[("Key\Wqueen.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Wqueen.png","DATA")]
a.datas+=[("Key\Bsoldier.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Bsoldier.png","DATA")]
a.datas+=[("Key\Wsoldier.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Wsoldier.png","DATA")]
a.datas+=[("Key\Wempty.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Wempty.png","DATA")]
a.datas+=[("Key\Bempty.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key\Bempty.png","DATA")]



a.datas+=[("Key1/Brock.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Brock.png","DATA")]
a.datas+=[("Key1/Wrock.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Wrock.png","DATA")]
a.datas+=[("Key1/Bhorse.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Bhorse.png","DATA")]
a.datas+=[("Key1/Belephant.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Belephant.png","DATA")]
a.datas+=[("Key1/Whorse.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Whorse.png","DATA")]
a.datas+=[("Key1/Welephant.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Welephant.png","DATA")]
a.datas+=[("Key1/Bking.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Bking.png","DATA")]
a.datas+=[("Key1/Wking.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Wking.png","DATA")]
a.datas+=[("Key1/Bqueen.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Bqueen.png","DATA")]
a.datas+=[("Key1/Wqueen.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Wqueen.png","DATA")]
a.datas+=[("Key1/Bsoldier.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Bsoldier.png","DATA")]
a.datas+=[("Key1/Wsoldier.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Wsoldier.png","DATA")]
a.datas+=[("Key1/Wempty.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Wempty.png","DATA")]
a.datas+=[("Key1/Bempty.png",r"C:\Users\Binu bot\Desktop\chess in tkinter\New folder\Key1\Bempty.png","DATA")]




pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Chess v1.1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='logo.ico')
