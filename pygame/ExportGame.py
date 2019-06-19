import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Frogger Mabye",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["frog.png"]}},
    executables = executables

    )