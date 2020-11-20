import pygame
from pygame import *
running = True
circles = {}
player = 0
win = 0
winner = ''
mode = ''
class Screen():
    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.display = pygame.display.set_mode([self.width,self.length])

class Circle():
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self):
        self.sprite = pygame.draw.circle(screen.display,self.color,[self.x,self.y],self.radius)

class Text():
    def __init__(self,x,y,size,text,color,bgcolor):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.color = color
        self.bgcolor = bgcolor
    def display(self):
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.Text = self.font.render(self.text, True, self.color, self.bgcolor)
        screen.display.blit(self.Text, [self.x,self.y])


def checkEvents():
  global running
  keys = pygame.key.get_pressed()
  global player
  mouse_pos = pygame.mouse.get_pos()
  if keys[K_ESCAPE]:
      running = False
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN and not win:
      for c in circles:
        click = circles[c].sprite.collidepoint(mouse_pos)
        if click and circles[c].color == [255,255,255]:
          if not player:
              circles[c].color = [255,0,0]
              status.text = "Yellow's Turn"
              player=1
          else:
            circles[c].color = [255,251,0]
            status.text = "Red's Turn"
            player=0
def checkGravityAndWins():
    global win
    global winner
    for c in circles:
        #gravity
        f = f"circle{int(c.replace('circle',''))+7}"
        if circles[c].color != [255,255,255] and int(f.replace('circle',''))<=41 and circles[f].color == [255,255,255]:
            circles[f].color = circles[c].color
            circles[c].color = [255,255,255]
        #check for wins
        points = 0
        if circles[c].color == [255,0,0]:
            points = 1
            if int(c.replace('circle',''))+1 not in [6,13,20,27,34,41] and int(c.replace('circle',''))+1 <41 and int(c.replace('circle','')) and circles[f"circle{int(c.replace('circle',''))+1}"].color == [255,0,0]:
                points += 1
                if int(c.replace('circle',''))+2 not in [6,13,20,27,34,41] and circles[f"circle{int(c.replace('circle',''))+2}"].color == [255,0,0]:
                    points += 1
                    if int(c.replace('circle',''))+3 not in [6,13,20,27,34,41] and circles[f"circle{int(c.replace('circle',''))+3}"].color == [255,0,0]:
                        points += 1
                        winner = 'Red'
                        win = 1


        points = 0
        if circles[c].color == [255,251,0]:
            points = 1
            if int(c.replace('circle',''))+1 not in [6,13,20,27,34,41] and int(c.replace('circle',''))+1 <41 and int(c.replace('circle',''))<42 and circles[f"circle{int(c.replace('circle',''))+1}"].color == [255,251,0]:
                points += 1
                if int(c.replace('circle',''))+2 not in [6,13,20,27,34,41] and circles[f"circle{int(c.replace('circle',''))+2}"].color == [255,251,0]:
                    points += 1
                    if int(c.replace('circle',''))+3 not in [6,13,20,27,34,41] and circles[f"circle{int(c.replace('circle',''))+3}"].color == [255,251,0]:
                        points += 1
                        winner = 'Yellow'
                        win = 1



        points = 0
        if circles[c].color == [255,0,0]:
            points = 1
            if int(c.replace('circle',''))-7 >= 0 and circles[f"circle{int(c.replace('circle',''))-7}"].color == [255,0,0]:
                points += 1
                if int(c.replace('circle',''))-14 >= 0 and circles[f"circle{int(c.replace('circle',''))-14}"].color == [255,0,0]:
                    points += 1
                    if int(c.replace('circle',''))-21 >= 0 and circles[f"circle{int(c.replace('circle',''))-21}"].color == [255,0,0]:
                        points += 1
                        winner = 'Red'
                        win = 1


        points = 0
        if circles[c].color == [255,251,0]:
            points = 1
            if int(c.replace('circle',''))-7 >= 0 and circles[f"circle{int(c.replace('circle',''))-7}"].color == [255,251,0]:
                points += 1
                if int(c.replace('circle',''))-14 >= 0 and circles[f"circle{int(c.replace('circle',''))-14}"].color == [255,251,0]:
                    points += 1
                    if int(c.replace('circle',''))-21 >= 0 and circles[f"circle{int(c.replace('circle',''))-21}"].color == [255,251,0]:
                        points += 1
                        winner = 'Yellow'
                        win = 1

        points = 0
        if circles[c].color == [255,0,0]:
            points = 1
            if int(c.replace('circle',''))-8 >= 0 and circles[f"circle{int(c.replace('circle',''))-8}"].color == [255,0,0]:
                points += 1
                if int(c.replace('circle',''))-16 >= 0 and circles[f"circle{int(c.replace('circle',''))-16}"].color == [255,0,0]:
                    points += 1
                    if int(c.replace('circle',''))-24 >= 0 and circles[f"circle{int(c.replace('circle',''))-24}"].color == [255,0,0]:
                        points += 1
                        winner = 'Red'
                        win = 1

        points = 0
        if circles[c].color == [255,251,0]:
            points = 1
            if int(c.replace('circle',''))-8 >= 0 and circles[f"circle{int(c.replace('circle',''))-8}"].color == [255,251,0]:
                points += 1
                if int(c.replace('circle',''))-16 >= 0 and circles[f"circle{int(c.replace('circle',''))-16}"].color == [255,251,0]:
                    points += 1
                    if int(c.replace('circle',''))-24 >= 0 and circles[f"circle{int(c.replace('circle',''))-24}"].color == [255,251,0]:
                        points += 1
                        winner = 'Yellow'
                        win = 1
        points = 0
        if circles[c].color == [255,0,0]:
            points = 1
            if int(c.replace('circle',''))-6 >= 0 and circles[f"circle{int(c.replace('circle',''))-6}"].color == [255,0,0]:
                points += 1
                if int(c.replace('circle',''))-12 >= 0 and circles[f"circle{int(c.replace('circle',''))-12}"].color == [255,0,0]:
                    points += 1
                    if int(c.replace('circle',''))-18 >= 0 and circles[f"circle{int(c.replace('circle',''))-18}"].color == [255,0,0]:
                        points += 1
                        winner = 'Red'
                        win = 1

        points = 0
        if circles[c].color == [255,251,0]:
            points = 1
            if int(c.replace('circle',''))-6 >= 0 and circles[f"circle{int(c.replace('circle',''))-6}"].color == [255,251,0]:
                points += 1
                if int(c.replace('circle',''))-12 >= 0 and circles[f"circle{int(c.replace('circle',''))-12}"].color == [255,251,0]:
                    points += 1
                    if int(c.replace('circle',''))-18 >= 0 and circles[f"circle{int(c.replace('circle',''))-18}"].color == [255,251,0]:
                        points += 1
                        winner = 'Yellow'
                        win = 1

def hCheckEvents(buttons):
    global mode
    global running
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    if keys[K_ESCAPE]:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                click = buttons[button].sprite.collidepoint(mouse_pos)
                if click:
                    mode = button


class Rect():
    def __init__(self,x,y,width,length,color):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.color = color
        self.name = ""
        self.text = Text(self.x,self.y,75,"",[255,255,255],self.color)
    def draw(self):
        self.sprite = pygame.draw.rect(screen.display,self.color,[self.x,self.y,self.width,self.length])


def home():
    #buttons = {"AI":Rect(25,screen.length/1.5,75,35,[0,0,0]),"Normal":Rect(screen.width/2-75,screen.length/1.5,75,35,[0,0,0]),"Online":Rect(screen.width/1.3,screen.length/1.5,75,35,[0,0,0])}
    buttons = {"Normal":Rect(screen.width/2-75,screen.length/1.5,75,35,[0,0,0])}
    title = Text(screen.width/4,screen.length/2,25,"Connect Four",[255,255,255],[0,0,0])
    screen.display.fill([0,0,215])
    for button in buttons:
        buttons[button].name = button
        buttons[button].draw()
        buttons[button].text.text = buttons[button].name
        buttons[button].text.display()
    pygame.draw.circle(screen.display,[255,251,0],[screen.width/2,screen.length/4],100)
    title.display()
    hCheckEvents(buttons)
    pygame.display.flip()



status = Text(25,410,25,"Red's Turn",[255,255,255],[0,0,0])
def main():
    screen.display.fill([0,0,215])
    status.display()
    for c in circles:
        circles[c].draw()
    checkEvents()
    if not win:
        checkGravityAndWins()
    if win:
        status.text = f"{winner} has won the round"

    pygame.display.flip()

pygame.init()
screen = Screen(500,450)
for i in range(42):
    if i in [0,7,14,21,28,35]:
        if i == 0:
            circles[f"circle{i}"] = Circle(50,50,25,[255,255,255])
        elif i == 7:
            circles[f"circle{i}"] = Circle(50,115,25,[255,255,255])
        elif i == 14:
            circles[f"circle{i}"] = Circle(50,180,25,[255,255,255])
        elif i == 21:
            circles[f"circle{i}"] = Circle(50,245,25,[255,255,255])
        elif i == 28:
            circles[f"circle{i}"] = Circle(50,310,25,[255,255,255])
        else:
            circles[f"circle{i}"] = Circle(50,375,25,[255,255,255])
    elif i in [1,8,15,22,29,36]:
        if i == 1:
            circles[f"circle{i}"] = Circle(115,50,25,[255,255,255])
        elif i == 8:
            circles[f"circle{i}"] = Circle(115,115,25,[255,255,255])
        elif i == 15:
            circles[f"circle{i}"] = Circle(115,180,25,[255,255,255])
        elif i == 22:
            circles[f"circle{i}"] = Circle(115,245,25,[255,255,255])
        elif i == 29:
            circles[f"circle{i}"] = Circle(115,310,25,[255,255,255])
        else:
            circles[f"circle{i}"] = Circle(115,375,25,[255,255,255])
    elif i in [2,9,16,23,30,37]:
        if i==2:
            circles[f"circle{i}"] = Circle(180,50,25,[255,255,255])
        elif i==9:
            circles[f"circle{i}"] = Circle(180,115,25,[255,255,255])
        elif i==16:
            circles[f"circle{i}"] = Circle(180,180,25,[255,255,255])
        elif i==23:
            circles[f"circle{i}"] = Circle(180,245,25,[255,255,255])
        elif i==30:
            circles[f"circle{i}"] = Circle(180,310,25,[255,255,255])
        else:
            circles[f"circle{i}"] = Circle(180,375,25,[255,255,255])
    elif i in [3,10,17,24,31,38]:
        if i==3:
            circles[f"circle{i}"] = Circle(245,50,25,[255,255,255])
        elif i==10:
            circles[f"circle{i}"] = Circle(245,115,25,[255,255,255])
        elif i==17:
            circles[f"circle{i}"] = Circle(245,180,25,[255,255,255])
        elif i==24:
            circles[f"circle{i}"] = Circle(245,245,25,[255,255,255])
        elif i==31:
            circles[f"circle{i}"] = Circle(245,310,25,[255,255,255])
        else:
            circles[f"circle{i}"] = Circle(245,375,25,[255,255,255])
    elif i in [4,11,18,25,32,39]:
        if i==4:
            circles[f"circle{i}"] = Circle(310,50,25,[255,255,255])
        elif i==11:
            circles[f"circle{i}"] = Circle(310,115,25,[255,255,255])
        elif i==18:
            circles[f"circle{i}"] = Circle(310,180,25,[255,255,255])
        elif i==25:
            circles[f"circle{i}"] = Circle(310,245,25,[255,255,255])
        elif i==32:
            circles[f"circle{i}"] = Circle(310,310,25,[255,255,255])
        else:
            circles[f"circle{i}"] = Circle(310,375,25,[255,255,255])
    elif i in [5,12,19,26,33,40]:
        if i==5:
            circles[f"circle{i}"] = Circle(375,50,25,[255,255,255])
        elif i==12:
            circles[f"circle{i}"] = Circle(375,115,25,[255,255,255])
        elif i==19:
            circles[f"circle{i}"] = Circle(375,180,25,[255,255,255])
        elif i==26:
            circles[f"circle{i}"] = Circle(375,245,25,[255,255,255])
        elif i==33:
            circles[f"circle{i}"] = Circle(375,310,25,[255,255,255])
        else:
            circles[f"circle{i}"] = Circle(375,375,25,[255,255,255])

    else:
        if i==6:
            circles[f"circle{i}"] = Circle(440,50,25,[255,255,255])
        elif i==13:
            circles[f"circle{i}"] = Circle(440,115,25,[255,255,255])
        elif i==20:
            circles[f"circle{i}"] = Circle(440,180,25,[255,255,255])
        elif i==27:
            circles[f"circle{i}"] = Circle(440,245,25,[255,255,255])
        elif i==34:
            circles[f"circle{i}"] = Circle(440,310,25,[255,255,255])
        else:
            circles[f"circle{i}"] = Circle(440,375,25,[255,255,255])


while running:
    if mode == '':
        home()
    else:
        main()

pygame.quit()
