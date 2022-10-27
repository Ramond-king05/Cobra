import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name="Ramond snake Game",
    options={"build_exe": {"packages":["pygame"],
                           }},
    executables = executables

    )
