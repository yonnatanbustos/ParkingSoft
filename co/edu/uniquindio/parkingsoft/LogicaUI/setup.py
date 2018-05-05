from cx_Freeze import setup, Executable

executables = [Executable("Login.py",
                          base="Win32GUI",
                          icon="icons\parking-idea.png")]

build_exe_options = {"packages": [],
                     "include_files": ["LogicaUI"]}

setup(
    name="Prueba",
    version="1.0",
    description="Prueba",
    options={"build_exe": build_exe_options},
    executables=executables
)
