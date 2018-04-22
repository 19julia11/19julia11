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
		self.x_acceleration = 0
		self.x_speed = 0
		self.y_speed = 5
		self.strength = 7
		self.score = 0
		self.state = "running"
		self.frame = 0
		self.images = ["stickman1.gif", "stickman2.gif","stickman3.gif","stickman4.gif","stickman5.gif","stickman6.gif","stickman7.gif","stickman8.gif","stickman9.gif","stickman10.gif"]
        
	def jump(self):
		if self.state == "running":
			self.y_acceleration += self.strength
			self.sety(-100)
			self.state = "jumping"
	
	def tick(self):
		#Deal with x
		self.x_speed += self.x_acceleration
		if self.x_speed > 2:
			self.x_speed = 2
		elif self.x_speed < -2:
			self.x_speed = -2
			
		self.setx(self.xcor() + self.x_speed)
		self.move()
		
		# Switch frames
		current_image = self.images[self.frame]
		self.set_image(current_image, 31, 40)
		self.frame += 1
		if self.frame == 10:
			self.frame = 0
		
		
	def move(self):
		self.fd(self.speed)
			
		if self.xcor() > game.SCREEN_WIDTH / 2:
			self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

		if self.xcor() < -game.SCREEN_WIDTH /2 :
			self.goto(game.SCREEN_WIDTH / 2, self.ycor())

		if self.ycor() > game.SCREEN_HEIGHT / 2:
			self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

		if self.ycor() < -game.SCREEN_HEIGHT / 2:
			self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)
		
		# Deal with y 
		if self.ycor() < -100:
			self.y_acceleration = 0
			self.y_speed = 0
			self.sety(-100)
			self.state = "running"
		else:
			self.y_acceleration += game.gravity
			self.y_speed += self.y_acceleration
			self.sety(self.ycor() + self.y_speed)
		    	
	def move_left(self):
		self.x_speed = -1
		    	
	def move_right(self):
		self.x_speed = 1
    	
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
 
	def move(self):
		self.fd(self.speed)
		wn.ontimer(self.move, 100)

		
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
game = spgl.Game(800, 450, "black", "The Math Quest", 0)
game.gravity = -0.9
game.set_background("full_background.gif")

# Create Sprites
# Create Person
player = Player("Layer 12.gif", "white", -300, -100)
player.questions_answered = 0
dog = Dog("Dog.gif", "darkgoldenrod", -390, -120)
question1 = Question("question_small.gif", "yellow", -200, -70)
question2 = Question("question_small.gif", "yellow", -120, -10)
question3 = Question("question_small.gif", "yellow", 0, 10)
question4 = Question("question_small.gif", "yellow", 80, -50)
question5 = Question("question_small.gif", "yellow", 150, 0)
question6 = Question("question_small.gif", "yellow", 220, 20)
gate = Gate("Gate.gif", "dimgray", 220, -60)
gate.shapesize(5, 1, 0)
house = House("house.gif", "slategrey", 350, -100)
house.shapesize(4, 1.5, 0)

# Create Labels
score_label = spgl.Label("Score: 0", "black", -390, 200)

# Create Buttons

# Set Keyboard Bindings
def set_keyboard_bindings():
	wn = spgl.turtle.Screen()
	game.set_keyboard_binding(spgl.KEY_SPACE, player.jump)
	game.set_keyboard_binding(spgl.KEY_LEFT, player.move_left)
	game.set_keyboard_binding(spgl.KEY_RIGHT, player.move_right)
	game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)

set_keyboard_bindings()

wn = spgl.turtle.Screen()
wn.ontimer(dog.move, 200)

while True:
	
	print(player.state)
    # Call the game tick method
	game.tick()
	set_keyboard_bindings()
    
    # Check collisions
	if game.is_collision(player, question1):
		player.questions_answered += 1
		print("QUESTION 1 COLLISION")
		num = wn.numinput("Question 1", "What is 1 + 2?")
		if num == 3:
			print ("CORRECT :)")
			question1.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))
		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))
 			
	elif game.is_collision(player, question2):
		player.questions_answered += 1
		print("QUESTION 2 COLLISION")
		num = root.numinput("Question 2", "What is 56 + 89?")
		print (num)
		if num == 145:
			print ("CORRECT :)")
			question2.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))
		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))
 			
	elif game.is_collision(player, question3):
		player.questions_answered += 1
		print("QUESTION 3 COLLISION")
		num = root.numinput("Question 3", "What is 53 - 26?")
		print (num)
		if num == 27:
			print ("CORRECT :)")
			question3.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))
		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))
    		
	if game.is_collision(player, question4):
		player.questions_answered += 1
		print("QUESTION 4 COLLISION")
		num = root.numinput("Question 4", "What is 4 * 6?")
		print (num)
		if num == 24:
			print ("CORRECT :)")
			question4.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))
		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))
			
	if game.is_collision(player, question5):
		player.questions_answered += 1
		print("QUESTION 5 COLLISION")
		num = root.numinput("Question 5", "What is 18 * 3?")
		print (num)
		if num == 54:
			print ("CORRECT :)")
			question5.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))
		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))
			
	if game.is_collision(player, question6):
		player.questions_answered += 1
		print("QUESTION 6 COLLISION")
		num = root.numinput("Question 6", "What is 144 / 3?")
		print (num)
		if num == 48:
			print ("CORRECT :)")
			question6.destroy()
			player.score += 10
			score_label.update("Score: {}".format(player.score))
		else:
			print ("WRONG :(")
			player.score -= 10
			score_label.update("Score: {}".format(player.score))

	if game.is_collision(player, gate) and player.questions_answered == 6:
		gate.sety(100)
		
	if game.is_collision(player, house):
		exit()