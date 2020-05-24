# Frogger 2D
A summer project, implementing the classical arcade game "Frogger" using the [PyGame](https://www.pygame.org) python (3.5) library. 
I have used the [cx_freeze](https://anthony-tuininga.github.io/cx_Freeze) library to create installers for windows and linux operating systems.

Various game concepts techniques were used such as Finite State Machines and Collision Detection - Resolution.
I have attempted to follow an object-oriented approach that formats the code for readability.
### Classes Implemented
* Frog (Player)
* Moving Object (Abstract Class)
* Turtle, Fly, Car, Trunk - All inherit from the Moving Object base class
### Game Finite State Machine
0. Intro State
1. Play State
2. Pause State
3. Win State
4. Over State
5. Cookie State
