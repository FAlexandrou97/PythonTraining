from cx_Freeze import setup, Executable
import os.path

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

includefiles=["frog.png", "carBlack.png", "carFast.png", "carTruckLeft.png", "carTruckRight.png",
              "carWhiteLeft.png", "carWhiteRight.png", "grass.jpg", "road.png", "water.png",
              "music.mp3"]
setup(
    name="Froggerz",
    version="0.1",
    description="test",
    options={'build_exe': {'include_files': includefiles}},
    executables=[Executable("game.py")],
)