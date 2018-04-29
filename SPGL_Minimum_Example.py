# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import turtle 

# Create Classes
class Player(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        
    def jump(self):
        pass
		    	
    def move_left(self):
        self.fd(-50)
		    	
    def move_right(self):
        self.fd(50)
    	
    def exit(self):
        pass
    	
class Dog(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        
class Question(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        
class Gate(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y) 
        
class House(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)    
# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "The Math Quest", 0)

# Create Sprites
# Create Person
player = Player("triangle", "white", -300, 0)
dog = Dog("turtle", "darkgoldenrod", -390, 0)
question = Question("square", "yellow", -200, 10)
question = Question("square", "yellow", -100, 70)
question = Question("square", "yellow", 0, 30)
question = Question("square", "yellow", 100, 0)
question = Question("square", "yellow", 200, 40)
question = Question("square", "yellow", 270, 50)
gate = Gate("square", "dimgray", 300, 0)
gate.shapesize(5, 1, 0)
house = House("square", "slategrey", 350, 0)
house.shapesize(4, 2, 0)
# Create Labels

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_SPACE, player.jump)
game.set_keyboard_binding(spgl.KEY_LEFT, player.move_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.move_right)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)
while True:
    # Call the game tick method
    game.tick()
