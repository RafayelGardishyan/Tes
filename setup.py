import sys
from cx_Freeze import setup, Executable

setup(
    name = "RafAssistant",
    version = "0.1",
    description = "An assistant thas is going to grow.",
    executables = [Executable("main.py", base = "Win32GUI")])
