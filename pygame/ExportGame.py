from cx_Freeze import setup, Executable
import os.path

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

includefiles=["frog.png", "carBlack.png", "carFast.png", "carTruckLeft.png", "carTruckRight.png",
              "carWhiteLeft.png", "carWhiteRight.png", "grass.jpg", "road.png", "water.png", "fly.png",
              "turtle.png", "trunk.png", "cookie.png", "grass_green.jpg", "music.mp3"]
setup(
    name="Frogger_Pygame",
    version="1.1",
    description="Official Release (submitted version)",
    options={'build_exe': {'include_files': includefiles}},
    executables=[Executable("game.py")],
)