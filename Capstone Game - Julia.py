# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import turtle 
import random
import math

class Game(turtle.Turtle):
	pass
	#def change_score(self, points):
	#	self.score += points
	#	self.update_score()
	#	score_label.update("Score: {}".format(change_score))
		
# Create Classes
class Player(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.score = 0
		self.frame = 0
		self.y_acceleration = 5
		self.y_speed = 5
		self.strength = 7
		self.score
		self.state = "running"
        
	def jump(self):
		if self.state == "running":
			self.y_acceleration += self.strength
			self.sety(0)
			self.state = "jumping"
	
	def tick(self):
		self.setx(self.xcor())
		if self.ycor() < -100:
			self.y_acceleration = 0
			self.y_speed = 0
			self.sety(-100)
			self.state = "running"
			
		self.y_acceleration += game.gravity
		self.y_speed += self.y_acceleration
		self.sety(self.ycor() + self.y_speed)
		    	
	def move_left(self):
		self.fd(-10)
		    	
	def move_right(self):
		self.fd(10)
    	
	def exit(self):
		pass
		
	#def is_collision(self, sprite_1, sprite_2):
        # Axis Aligned Bounding Box
        #x_collision = (math.fabs(sprite_1.xcor() - sprite_2.xcor()) * 2) < (sprite_1.width + sprite_2.width)
        #y_collision = (math.fabs(sprite_1.ycor() - sprite_2.ycor()) * 2) < (sprite_1.height + sprite_2.height)
        #return (x_collision and y_collision)

    #def is_circle_collision(sprite_1, sprite_2, radius):
        # Collision based on distance
    	#a=sprite_1.xcor()-sprite_2.xcor()
    	#b=sprite_1.ycor()-sprite_2.ycor()
    	#distance = math.sqrt((a**2) + (b**2))

    	#if distance < radius:
    		#return True
    	#else:
    		#return False
    		
class Dog(spgl.Sprite):
	def __init__(self, shape, color, x, y):
		spgl.Sprite.__init__(self, shape, color, x, y)
		self.speed = 0.5
        
	def tick(self):
		self.fd(self.speed)
		
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
game.gravity = -0.9

# Create Sprites
# Create Person
player = Player("triangle", "white", -300, 0)
dog = Dog("turtle", "darkgoldenrod", -390, 0)
question1 = Question("square", "yellow", -200, 10)
question2 = Question("square", "yellow", -100, 70)
question3 = Question("square", "yellow", 0, 30)
question4 = Question("square", "yellow", 100, 0)
question5 = Question("square", "yellow", 200, 40)
question6 = Question("square", "yellow", 270, 50)
gate = Gate("square", "dimgray", 300, 0)
gate.shapesize(5, 1, 0)
house = House("square", "slategrey", 350, 0)
house.shapesize(4, 1.5, 0)

# Create Labels
score_label = spgl.Label("Score: 0", "white", -380, 280)

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_SPACE, player.jump)
game.set_keyboard_binding(spgl.KEY_LEFT, player.move_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.move_right)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)

while True:
    # Call the game tick method
	game.tick()
    
    # Check collisions
	if game.is_collision(player, question1):
		print("QUESTION 1 COLLISION")
		answer = int(input("1 + 2 = "))
		if answer == 3:
			print ("CORRECT :)")
			question1.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))

		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))
    		
	elif game.is_collision(player, question4):
		print("QUESTION 4 COLLISION")
		answer = int(input("18 * 3 = "))
		if answer == 54:
			print ("CORRECT :)")
			question4.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))
		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))