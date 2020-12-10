from tkinter import *
import random

#Initialize the graphic interface
width = 1024
height = 768

root = Tk()
root.title("Snake Retro Game")

cv_width = root.winfo_screenwidth()
cv_height = root.winfo_screenheight()
#to place the window on the center of the screen
root.geometry('%dx%d+%d+%d' % (1024, 768, (cv_width - 1024) / 2, (cv_height - 768) / 2))
background = PhotoImage(file="image_1.png")
theLabel = Label(root, image=background, borderwidth=0)
theLabel.place(relx=0, rely=0)

title = Label(root, text="Snake Retro Game", font="Arial 40 bold",bg="black", fg="white")
title.place(relx = 0.5, rely=0.15, anchor="center")

ID = "none"
SCORE = 0
gameOverPic = PhotoImage(file="Gameover.png")

def homePage():
	global b1, b2, b3, b4
	b1 = Button(root, text="Play", command=gamePage, font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b1.place(relx = 0.5, rely=0.3, anchor="center")
	b2 = Button(root, text="Leader board", command=openLeaderboard,font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b2.place(relx = 0.5, rely=0.4, anchor="center")
	b3 = Button(root, text="About the game", command=aboutPage, font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b3.place(relx = 0.5, rely=0.5, anchor="center")
	b4 = Button(root, text="Exit", command=root.quit, font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b4.place(relx = 0.5, rely=0.6, anchor="center")

def Nickname():
	global enterNick, submitNick, labelNick

	labelNick = Label(root, text="Enter Your Nickname: ", font=("Arial 20 bold"), bg="black", fg="#9966FF")
	labelNick.place(relx=0.5, rely=0.33, anchor="center")

	enterNick = Entry(root, textvariable="StringVar", fg="#9966FF", font=("Arial 20 bold"), bg="white", width=20)
	enterNick.place(relx = 0.5, rely=0.40, anchor="center")

	submitNick = Button(root, text="Submit", command=getID, fg="#9966FF", font=("Arial 20 bold"), bg="black")
	submitNick.place(relx = 0.5, rely=0.5, anchor="center")

def getID():
	global ID
	ID = enterNick.get()
	labelNick.destroy()
	enterNick.destroy()
	submitNick.destroy()
	homePage()
def aboutPage():
	global aboutTitle, aboutCanvas
	aboutTitle = Label(root, text="     About the Game     ", font="Arial 40 bold",bg="black", fg="white")
	aboutTitle.place(relx = 0.5, rely=0.15, anchor="center")
	#create a canvas for displaying the game information
	aboutCanvas = Canvas(root, width=800, height=500, bg="black")
	aboutCanvas.place(relx=0.5, rely=0.56, anchor="center")
	aboutText = "Welcome to Snake Retro Game, \n" +\
				"This is an advanced version of snake game.\n\n" +\
				"The snake will need to eat the apples,\n" +\
				"which will +10 for the score each time.\n\n" +\
				"Also, during the game, a mystery box will sometimes\n" +\
				"appear on the screen which has two possible functions.\n\n" +\
				"1. A frog can pop up, you will get +50 score by eating it.\n" +\
				"2. The snake body can possibly get larger...\n\n" +\
				"You will see it in the game.\n\n" +\
				"Hope you have fun and ENJOY it =)"
	aboutLabel = Label(aboutCanvas, text=aboutText, font="Arial 25 bold", fg="#9966FF", bg="black")
	aboutLabel.place(relx = 0.5, rely=0.45, anchor="center")
	Button(aboutCanvas, text="Back", font="Arial 20 bold", bg="white", fg="#9966FF", width=20, command=aboutBack).place(relx = 0.5, rely=0.92, anchor="center")

def gamePage():
	b1.destroy()
	b2.destroy()
	b3.destroy()
	b4.destroy()
	global SCORE, buttonHeight, scoreText
	buttonHeight = 20.5
	# global canvas
	# canvas = Canvas(root, bg="black", width=1024, height=768)
	canvas.pack()
	#3 function buttons you can use when playing the game
	Button(canvas,text="Save Game", command=lambda: writeLb(ID, SCORE)).place(rely=0,width=1024,height=buttonHeight)
	Button(canvas,text="Exit",command = root.destroy, bg="black").place(rely=0.02,width=1024, height=buttonHeight)
	Button(canvas,text="Home", command=homeButton).place(rely=0.04,width=1024, height=buttonHeight)

	txt = "Score: " + str(SCORE)
	scoreText = canvas.create_text(width/2, buttonHeight * 3, fill="#9966FF", font="Arial 20 italic bold", text=txt)
	placeFood()
	placeBox()
	global snake
	snake.clear()
	snake.append(canvas.create_rectangle(snakeSize, int(buttonHeight * 5) + 1, snakeSize * 2, int(buttonHeight * 5) + 1 + snakeSize, fill="#33CC66"))
	moveSnake()

def placeFood():
	global foodX, foodY, apple, food
	apple = PhotoImage(file="apple.png")
	food = canvas.create_image(0, 0, anchor=NW, image=apple)
	foodX = random.randint(0, width - 40)
	foodY = random.randint(int(buttonHeight * 5) + 1, height - 40)
	canvas.move(food, foodX, foodY)
	print(canvas.coords(food))

def moveFood():
	global food, foodX, foodY
	canvas.move(food, (foodX*(-1)), (foodY*(-1)))

	foodX = random.randint(0,width-40)
	foodY = random.randint(int(buttonHeight * 5) + 1, height-40)

	canvas.move(food, foodX, foodY)
	# print(canvas.coords(food))

def placeBox():
	# root.after(30000, placeBox)
	global box, boxX, boxY
	mystery_img = PhotoImage(file="mystery_box.png")
	box = canvas.create_image(0, 0, anchor=NW, image=mystery_img)
	boxX = random.randint(0, width - 40)
	boxY = random.randint(int(buttonHeight * 5) + 1, height - 40)
	# canvas.coords(box, boxX, boxY)
	canvas.move(box, boxX, boxY)
	print(canvas.coords(box))

	# after(10000, hideBox)
def overlapping(a, b):
	if abs(a[0] - b[0]) < 30 and a[2] > b[0] and abs(a[1] - b[1]) < 30 and a[3] > b[1]:
		return True
	return False

def moveSnake():	
	global gameOverPic

	positions = []
	positions.append(canvas.coords(snake[0]))

	if len(positions[0]) == 0:
		return

	#to set so that the snake can appear from the other side when it hits the border of the window
	if positions[0][0] < 0:
		canvas.coords(snake[0],width,positions[0][1],width-snakeSize,positions[0][3])
	elif positions[0][2] >width:
		canvas.coords(snake[0],0-snakeSize,positions[0][1], 0, positions[0][3])
	elif positions[0][1] < 0:
		canvas.coords(snake[0],positions[0][0], height, positions[0][2], height-snakeSize)
	elif positions[0][3] > height:
		canvas.coords(snake[0],positions[0][0], 0 - snakeSize, positions[0][2], 0)

	positions.clear()
	positions.append(canvas.coords(snake[0]))


	if direction == "left":
		canvas.move(snake[0], -snakeSize, 0)
	elif direction == "right":
		canvas.move(snake[0], snakeSize, 0)
	elif direction == "up":
		canvas.move(snake[0], 0, -snakeSize)
	elif direction == "down":
		canvas.move(snake[0], 0, snakeSize)

	sHeadPos = canvas.coords(snake[0])
	foodPos = canvas.coords(food)

	#collision detection - to see if the snake eats the apple
	if overlapping(sHeadPos, foodPos):
		moveFood()
		growSnake()

	for i in range(1,len(snake)):
		list1 = canvas.coords(snake[i])
		if sHeadPos[0] < list1[2] and sHeadPos[2] > list1[0] and sHeadPos[1] < list1[3] and sHeadPos[3] > list1[1]:
			gameOver = True
			gameOverPic = PhotoImage(file="Gameover.png")
			canvas.create_image(width/2,height/2 - 50, image=gameOverPic, anchor="c")
			canvas.update()
			writeLb(ID, SCORE)
			return
	    
	if "gameOver" not in locals():
		if status == "run":
			root.after(90, moveSnake)


	for i in range(1, len(snake)):
		positions.append(canvas.coords(snake[i]))

	for i in range(len(snake)-1):
		canvas.coords(snake[i+1],positions[i][0],positions[i][1],positions[i][2],positions[i][3])



def growSnake():
	global SCORE
	lastElement = len(snake) - 1
	lastElementPos = canvas.coords(snake[lastElement])
    
	snake.append(canvas.create_rectangle(0, 0, snakeSize,snakeSize, fill="#00FF99"))
    
	if (direction == "left"):
		canvas.coords(snake[lastElement+1], lastElementPos[0]+snakeSize, lastElementPos[1],lastElementPos[2]+snakeSize,lastElementPos[3])
	elif (direction == "right"): 
		canvas.coords(snake[lastElement+1],lastElementPos[0] - snakeSize,lastElementPos[1],lastElementPos[2] - snakeSize,lastElementPos[3])
	elif (direction == "up"):
		canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]+snakeSize,lastElementPos[2],lastElementPos[3]+snakeSize)
	else:
 		canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]-snakeSize,lastElementPos[2],lastElementPos[3]-snakeSize)

#if the cheat code is pressed, the score will plus 100 when eating an apple
	if cheat == "yes":
		SCORE += 100
		txt = "Score: " + str(SCORE)
		canvas.itemconfigure(scoreText, text=txt)
	else:
		SCORE += 10
		txt = "Score: " + str(SCORE)
		canvas.itemconfigure(scoreText, text=txt)



def openLeaderboard():
	global lbTitle, record
	lbTitle = Label(root, text="      Leader Board      ", font="Arial 40 bold",bg="black", fg="white")
	lbTitle.place(relx = 0.5, rely=0.15, anchor="center")
	#create a canvas for displaying the ranking
	record = Canvas(root, width=800, height=500, bg="black")
	record.place(relx=0.5, rely=0.56, anchor="center")
	a = sorted(dic.items(), key=lambda x: x[1], reverse=True)
	#it displays top 8 scores
	for i in range(0, len(a)):
		if i > 7:
			break
		rank = a[i]
		text = str(i + 1) + ". " + rank[0] + " ==== " + str(rank[1]) + "\n"
		txtLabel = Label(record, text=text, font="Arial 20 bold", fg="#9966FF", bg="black")
		txtLabel.place(relx = 0.5, rely=i/10 + 0.12, anchor="center")

	Button(record, text="Back", font="Arial 20 bold", bg="white", fg="#9966FF", width=20, command=lbBack).place(relx = 0.5, rely=0.9, anchor="center")
def writeLb(ID, score):
	file = open("record.txt", "a")
	info = "\n" + ID + "<" + str(SCORE) + ">"
	file.write(info)
	file.close()

def lbBack():
	lbTitle.destroy()
	record.destroy()
def aboutBack():
	aboutTitle.destroy()
	aboutCanvas.destroy()

def homeButton():
	global canvas
	canvas.destroy()
	b1 = Button(root, text="Play", command=gamePage, font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b1.place(relx = 0.5, rely=0.3, anchor="center")
	b2 = Button(root, text="Leader board", command=openLeaderboard,font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b2.place(relx = 0.5, rely=0.4, anchor="center")
	b3 = Button(root, text="About the game", command=aboutPage, font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b3.place(relx = 0.5, rely=0.5, anchor="center")
	b4 = Button(root, text="Exit", command=root.quit, font="Arial 20 bold", bg="white", fg="#9966FF", width=20)
	b4.place(relx = 0.5, rely=0.6, anchor="center")
	canvas = Canvas(root, bg="black", width=width, height=height)

#the oppsite direction is banned when moving towards to one diretion.
def leftKey(event):
	global direction
	if direction != "right":
		direction = "left"
def rightKey(event):
	global direction
	if direction != "left":
		direction = "right"
def upKey(event):
	global direction
	if direction != "down":
		direction = "up"
def downKey(event):
	global direction
	if direction != "up":
		direction = "down"
def Pause(event):
	global status
	status = "pause"
def Unpause(event):
	global status
	status = "run"
	moveSnake()
def mini(event):
	root.iconify()
def cheatMethod(event):
	global cheat
	cheat = "yes"

#initialized data
ID = "none"
SCORE = 0

snake = []
snakeSize = 15

direction = "right"
status = "run"
cheat = "no"

root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)
root.bind("<Up>", upKey)
root.bind("<Down>", downKey)
root.bind("<p>",Pause)  #to pause the game
root.bind("<s>",Unpause)  #to continue the game
root.bind("<q>",mini)  #boss key
root.bind("<x>",cheatMethod)  #cheat code

#to write a text file that contains the userID and the score
lbRecord = open("record.txt", "r").read()
start = 0
global name_list, score_list
name_list, score_list = [], []
#in the file, the score is inside "<" and ">" while the userID is before "<"
for i in range(0, len(lbRecord)):
	if lbRecord[i] == "<":
		name = lbRecord[start:i]
		name_list += [name]
		end = i + 1
	if lbRecord[i] == ">":
		score = lbRecord[end:i]
		score_list += [score]
		start = i + 2

global dic
dic = dict(map(lambda x,y:[x,int(y)],name_list,score_list))

Nickname()
# homePage()
canvas = Canvas(root, bg="black", width=width, height=height)

root.mainloop()
