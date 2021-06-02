from flask import Blueprint
from graphics import *
import threading

chess = Blueprint("chess",__name__)
width = 800
height = 600
cell = 60
size = 36
win = GraphWin("chess", width, height)
color = "white"


@chess.route("/my_chess")
def my_chess():
   # width = 800
   # height = 600
   # cell = 60
   # size = 36
    #win = GraphWin("chess", width, height)
   # color = "white"

    def Mouse():
        p = win.getMouse()
        x1 = p.x
        y1 = p.y
        return x1,y1

    def gen_table_dict():
        d = {}
        y_start = height / 2 - 4 * cell
        x_start = width / 2 - 4 * cell
        for i in range(8):
            d[i] = {}
            y = y_start + i * cell
            y1 = y + cell / 2
            for j in range(8):
                x = x_start + j * cell
                x1 = x + cell / 2
                d[i][j] = {}
                if i % 2 != 0:
                    if j % 2 != 0:
                        d[i][j] = {"color": "dimgray"}
                    else:
                        d[i][j] = {"color": "white"}
                else:
                    if j % 2 != 0:
                        d[i][j] = {"color": "white"}
                    else:
                        d[i][j] = {"color": "dimgray"}
                d[i][j]["v"] = None
                d[i][j]["x"] = x
                d[i][j]["y"] = y
                d[i][j]["x1"] = x1
                d[i][j]["y1"] = y1
                d[i][j]["rect"] = None
        return d

    def draw_table(table):
        for i in TABLE_DICT:
            for j in TABLE_DICT[i]:
                rect = Rectangle(Point(table[i][j]['x'],table[i][j]['y']),Point(table[i][j]['x']+cell,table[i][j]['y']+cell))
                rect.setFill(table[i][j]['color'])
                rect.draw(win)
                TABLE_DICT[i][j]["rect"] = rect
    TABLE_DICT = gen_table_dict()

    def update_table():
        for x in TABLE_DICT:
            for y in TABLE_DICT:
                if TABLE_DICT[x][y]["v"]:
                    TABLE_DICT[x][y]["v"].undraw()
        for x in TABLE_DICT:
            for y in TABLE_DICT:
                if TABLE_DICT[x][y]["v"]:
                    TABLE_DICT[x][y]["v"].draw()

    class Pawn():
        def __init__(self, color, start_x, start_y):
            global TABLE_DICT
            self.color = color
            self.start_x = start_x
            self.start_y = start_y
            self.cur_x = start_x
            self.cur_y = start_y
            TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
            if self.color == "white":
                self.code = u"\u2659"
            else:
                self.code = u"\u265F"
            self.pos = Point(TABLE_DICT[self.cur_y][self.cur_x]["x1"],TABLE_DICT[self.cur_y][self.cur_x]["y1"])
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)

        def __str__(self):
            return "Pawn " + self.color

        def move(self, y, x):
            global TABLE_DICT
            if self.check(y, x):
                if TABLE_DICT[y][x]["v"] != None:
                    if TABLE_DICT[y][x]["v"].color == self.color:
                        print ("pawn buzy same")
                        return False
                    TABLE_DICT[y][x]["v"].undraw()
                    TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.undraw()
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.cur_x = x
                self.cur_y = y
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
                self.draw()
                return True
            else:
                print ("pawn unchecked")
                return False

        def check(self, y, x):
            global TABLE_DICT
            if self.color == "white":
                if TABLE_DICT[y][x]["v"] == None:
                    if (x == self.cur_x and y == self.cur_y + 1) or (self.cur_y == 1 and x == self.cur_x and y == self.cur_y + 2):
                        return True
                elif TABLE_DICT[y][x]["v"] != None:
                    if (x == self.cur_x - 1 and y == self.cur_y + 1) or (x == self.cur_x + 1 and y == self.cur_y + 1):
                        return True
            elif self.color == "black":
                if TABLE_DICT[y][x]["v"] == None:
                    if x == self.cur_x and y == self.cur_y -1 or self.cur_y == 6 and x == self.cur_x and y == self.cur_y - 2:
                        return True
                elif TABLE_DICT[y][x]["v"] != None:
                    if x == self.cur_x - 1 and y == self.cur_y - 1 or x == self.cur_x + 1 and y == self.cur_y - 1:
                        return True
            else:
                return False

        def undraw(self):
            self.inst.undraw()
            del self.inst
    
        def draw(self):
            self.pos.x = TABLE_DICT[self.cur_y][self.cur_x]["x1"]
            self.pos.y = TABLE_DICT[self.cur_y][self.cur_x]["y1"]
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
            self.inst.draw(win)

    class Rook():
        def __init__(self, color, start_x, start_y):
            global TABLE_DICT
            self.color = color
            self.start_x = start_x
            self.start_y = start_y
            self.cur_x = start_x
            self.cur_y = start_y
            TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
            if color == "white":
                self.code = u"\u2656"
            else:
                self.code = u"\u265C"
            self.pos = Point(TABLE_DICT[self.cur_y][self.cur_x]["x1"],TABLE_DICT[self.cur_y][self.cur_x]["y1"])
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)

        def __str__(self):
            return "Rook " + self.color

        def move(self, y, x):
            global TABLE_DICT
            if self.check(y, x):
                if TABLE_DICT[y][x]["v"] != None:
                    if TABLE_DICT[y][x]["v"].color == self.color:
                        print ("rook buzy same")
                        return False
                    TABLE_DICT[y][x]["v"].undraw()
                    TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.undraw()
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.cur_x = x
                self.cur_y = y
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
                self.draw()
                return True
            else:
                print ("rook unchecked")
                return False
        
        def check(self, y, x):
            if self.cur_y == y or self.cur_x == x:
                if self.cur_x == x:
                    tmp_y = self.cur_y
                    if self.cur_y < y:
                        tmp_y += 1
                        while tmp_y < y:
                            if TABLE_DICT[tmp_y][x]["v"] != None:
                                print ("rook 1")
                                return False
                            tmp_y += 1
                    elif self.cur_y > y:
                        tmp_y -= 1
                        while tmp_y > y:
                            if TABLE_DICT[tmp_y][x]["v"] != None:
                                print ("rook 2")
                                return False
                            tmp_y -= 1
                elif self.cur_y == y:
                    tmp_x = self.cur_x
                    if self.cur_x < x:
                        tmp_x += 1
                        while tmp_x < x:
                            if TABLE_DICT[y][tmp_x]["v"] != None:
                                print ("rook 3")
                                return False
                            tmp_x += 1
                    elif self.cur_x > x:
                        tmp_x -= 1
                        while tmp_x > x:
                            if TABLE_DICT[y][tmp_x]["v"] != None:
                                print ("rook 4")
                                return False
                            tmp_x -= 1
                return True
        
                
        def undraw(self):
            self.inst.undraw()
            del self.inst
    
        def draw(self):
            self.pos.x = TABLE_DICT[self.cur_y][self.cur_x]["x1"]
            self.pos.y = TABLE_DICT[self.cur_y][self.cur_x]["y1"]  
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
            self.inst.draw(win)

    class Knight():
        def __init__(self, color, start_x, start_y):
            global TABLE_DICT
            self.color = color
            self.start_x = start_x
            self.start_y = start_y
            self.cur_x = start_x
            self.cur_y = start_y
            TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
            if color == "white":
                self.code = u"\u2658"
            else:
                self.code = u"\u265E"
            self.pos = Point(TABLE_DICT[self.cur_y][self.cur_x]["x1"],TABLE_DICT[self.cur_y][self.cur_x]["y1"])
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)

        def __str__(self):
            return "Knight " + self.color

        def move(self, y, x):
            global TABLE_DICT
            if self.check(y, x):
                if TABLE_DICT[y][x]["v"] != None:
                    if TABLE_DICT[y][x]["v"].color == self.color:
                        print ("knight buzy same")
                        return False
                    TABLE_DICT[y][x]["v"].undraw()
                    TABLE_DICT[y][x]["v"] = None
                self.undraw()
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.cur_x = x
                self.cur_y = y
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
                self.draw()
                return True
            else:
                print("knight unchecked")
                return False

        def check(self, y, x):
            if abs(self.cur_y - y) == 2 and abs(self.cur_x - x) == 1 or abs(self.cur_y - y) == 1 and abs(self.cur_x - x) == 2:
                return True

        def undraw(self):
            self.inst.undraw()
            del self.inst
    
        def draw(self):
            self.pos.x = TABLE_DICT[self.cur_y][self.cur_x]["x1"]
            self.pos.y = TABLE_DICT[self.cur_y][self.cur_x]["y1"]
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
            self.inst.draw(win)

    class Bishop():
        def __init__(self, color, start_x, start_y):
            global TABLE_DICT
            self.color = color
            self.start_x = start_x
            self.start_y = start_y
            self.cur_x = start_x
            self.cur_y = start_y
            TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
            if color == "white":
                self.code = u"\u2657"
            else:
                self.code = u"\u265D"
            self.pos = Point(TABLE_DICT[self.cur_y][self.cur_x]["x1"],TABLE_DICT[self.cur_y][self.cur_x]["y1"])
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)

        def __str__(self):
            return "Bishop " + self.color

        def move(self, y, x):
            global TABLE_DICT
            if self.check(y, x):
                if TABLE_DICT[y][x]["v"] != None:
                    if TABLE_DICT[y][x]["v"].color == self.color:
                        print ("bishop buzy same")
                        return False
                    TABLE_DICT[y][x]["v"].undraw()
                    TABLE_DICT[y][x]["v"] = None
                self.undraw()
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.cur_x = x
                self.cur_y = y
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
                self.draw()
                return True
            else:
                print ("bishop unchecked")
                return False

        def check(self, y, x):
            if abs(self.cur_x - x) == abs(self.cur_y - y):
                if self.cur_y < y and self.cur_x > x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y += 1
                    tmp_x -= 1
                    while tmp_y < y and tmp_x > x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print ("bishop 1")
                            return False
                        tmp_y += 1
                        tmp_x -= 1
                elif self.cur_y < y and self.cur_x < x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y += 1
                    tmp_x += 1
                    while tmp_y < y and tmp_x < x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print("bishop 2")
                            return False
                        tmp_y += 1
                        tmp_x += 1
                elif self.cur_y > y and self.cur_x < x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y -= 1
                    tmp_x += 1
                    while tmp_y > y and tmp_x < x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print("bishop 3")
                            return False
                        tmp_y -= 1
                        tmp_x += 1
                elif self.cur_y > y and self.cur_x > x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y -= 1
                    tmp_x -= 1
                    while tmp_y > y and tmp_x > x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print("bishop 4")
                            return False
                        tmp_y -= 1
                        tmp_x -= 1
                return True

        def undraw(self):
            self.inst.undraw()
            del self.inst
    
        def draw(self):
            self.pos.x = TABLE_DICT[self.cur_y][self.cur_x]["x1"]
            self.pos.y = TABLE_DICT[self.cur_y][self.cur_x]["y1"]
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
            self.inst.draw(win)

    class Queen():
        def __init__(self, color, start_x, start_y):
            global TABLE_DICT
            self.color = color
            self.start_x = start_x
            self.start_y = start_y
            self.cur_x = start_x
            self.cur_y = start_y
            TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
            if color == "white":
                self.code = u"\u2655"
            else:
                self.code = u"\u265B"
            self.pos = Point(TABLE_DICT[self.cur_y][self.cur_x]["x1"],TABLE_DICT[self.cur_y][self.cur_x]["y1"])
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
 
        def __str__(self):
            return "Quen " + self.color
    
        def move(self, y, x):
            global TABLE_DICT
            if self.check(y, x):
                if TABLE_DICT[y][x]["v"] != None:
                    if TABLE_DICT[y][x]["v"].color == self.color:
                        print ("Quen buzy same")
                        return False
                    TABLE_DICT[y][x]["v"].undraw()
                    TABLE_DICT[y][x]["v"] = None
                self.undraw()
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.cur_x = x
                self.cur_y = y
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
                self.draw()
                return True
            else:
                print("Quen unchecked")
                return False

        def check(self, y, x):
            if self.cur_y == y or self.cur_x == x:
                if self.cur_x == x:
                    tmp_y = self.cur_y
                    if self.cur_y < y:
                        tmp_y += 1
                        while tmp_y < y:
                            if TABLE_DICT[tmp_y][x]["v"] != None:
                                print ("Quen 1")
                                return False
                            tmp_y += 1
                    elif self.cur_y > y:
                        tmp_y -= 1
                        while tmp_y > y:
                            if TABLE_DICT[tmp_y][x]["v"] != None:
                                print ("Quen 2")
                                return False
                            tmp_y -= 1
                elif self.cur_y == y:
                    tmp_x = self.cur_x
                    if self.cur_x < x:
                        tmp_x += 1
                        while tmp_x < x:
                            if TABLE_DICT[y][tmp_x]["v"] != None:
                                print ("Quen 3")
                                return False
                            tmp_x += 1
                    elif self.cur_x > x:
                        tmp_x -= 1
                        while tmp_x > x:
                            if TABLE_DICT[y][tmp_x]["v"] != None:
                                print ("Quen 4")
                                return False
                            tmp_x -= 1
                return True
            if abs(self.cur_x - x) == abs(self.cur_y - y):
                if self.cur_y < y and self.cur_x > x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y += 1
                    tmp_x -= 1
                    while tmp_y < y and tmp_x > x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print ("Quen 5")
                            return False
                        tmp_y += 1
                        tmp_x -= 1
                elif self.cur_y < y and self.cur_x < x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y += 1
                    tmp_x += 1
                    while tmp_y < y and tmp_x < x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print("Quen 6")
                            return False
                        tmp_y += 1
                        tmp_x += 1
                elif self.cur_y > y and self.cur_x < x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y -= 1
                    tmp_x += 1
                    while tmp_y > y and tmp_x < x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print("Quen 7")
                            return False
                        tmp_y -= 1
                        tmp_x += 1
                elif self.cur_y > y and self.cur_x > x:
                    tmp_y = self.cur_y
                    tmp_x = self.cur_x
                    tmp_y -= 1
                    tmp_x -= 1
                    while tmp_y > y and tmp_x > x:
                        if TABLE_DICT[tmp_y][tmp_x]["v"] != None:
                            print("Quen 8")
                            return False
                        tmp_y -= 1
                        tmp_x -= 1
                return True
                        
        def undraw(self):
            self.inst.undraw()
            del self.inst
    
        def draw(self):
            self.pos.x = TABLE_DICT[self.cur_y][self.cur_x]["x1"]
            self.pos.y = TABLE_DICT[self.cur_y][self.cur_x]["y1"]
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
            self.inst.draw(win)

    class King():
        def __init__(self, color, start_x, start_y):
            self.color = color
            self.start_x = start_x
            self.start_y = start_y
            self.cur_x = start_x
            self.cur_y = start_y
            TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
            if color == "white":
                self.code = u"\u2654"
            else:
                self.code = u"\u265A"
            self.pos = Point(TABLE_DICT[self.cur_y][self.cur_x]["x1"],TABLE_DICT[self.cur_y][self.cur_x]["y1"])
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
        
        def __str__(self):
            return "King " + self.color

        def move(self, y, x):
            global TABLE_DICT
            if self.check(y, x):
                if TABLE_DICT[y][x]["v"] != None:
                    if TABLE_DICT[y][x]["v"].color == self.color:
                        print ("king buzy same")
                        return False
                    TABLE_DICT[y][x]["v"].undraw()
                    TABLE_DICT[y][x]["v"] = None
                self.undraw()
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = None
                self.cur_x = x
                self.cur_y = y
                TABLE_DICT[self.cur_y][self.cur_x]["v"] = self
                self.draw()
                return True
            else:
                print ("king unchecked")
                return False

        def check(self,y,x):
            if abs(self.cur_x - x) <= 1 and abs(self.cur_y - y) <= 1:
                    return True

        def undraw(self):
            self.inst.undraw()
            del self.inst
    
        def draw(self):
            self.pos.x = TABLE_DICT[self.cur_y][self.cur_x]["x1"]
            self.pos.y = TABLE_DICT[self.cur_y][self.cur_x]["y1"]
            self.inst = Text(self.pos,self.code)
            self.inst.setSize(size)
            self.inst.draw(win)

    draw_table(gen_table_dict())

    z = 0
    while z < 8:
        b_pawn = Pawn("black",z,6)
        w_pawn = Pawn("white",z,1)
        z+=1
    w_rook_1 = Rook("white", 0,0)
    w_rook_2 = Rook("white", 7, 0)
    b_rook_1 = Rook("black",0,7)
    b_rook_2 = Rook("black",7,7)
    w_knight_1 = Knight("white",1,0)
    w_knight_2 = Knight("white",6,0)
    b_knight_1 = Knight("black",1,7)
    b_knight_2 = Knight("black",6,7)
    w_bishop_1 = Bishop("white",2,0)
    w_bishop_2 = Bishop("white",5,0)
    b_bishop_1 = Bishop("black",2,7)
    b_bishop_2 = Bishop("black",5,7)
    w_queen = Queen("white",3,0)
    b_queen = Queen("black",3,7)
    w_king = King("white",4,0)
    b_king = King("black",4,7)
    update_table()

    def dirq():
        mx,my = Mouse()
        for y in TABLE_DICT:
            for x in TABLE_DICT[y]:
                if my >= TABLE_DICT[y][x]["y"] and my < TABLE_DICT[y][x]["y"] + cell:
                    if mx >= TABLE_DICT[y][x]["x"] and mx < TABLE_DICT[y][x]["x"] + cell:
                        return y, x
        return -1, -1

            
    def get_color(x,y):
        return TABLE_DICT[y][x]["v"].color

    def play():
        selected = False
        selected_x = -1
        selected_y = -1
        while True:
            global color
            y, x = dirq()
            if not selected:
                if x != -1  and y != -1:
                    if TABLE_DICT[y][x]["v"]:
                        if get_color(x, y) != color:
                            continue
                        TABLE_DICT[y][x]["rect"].setFill("red")
                        selected_x = x
                        selected_y = y
                        selected = True
            if selected:
                if x != -1 and y != -1:
                    if TABLE_DICT[y][x]["v"] == None:
                        if TABLE_DICT[selected_y][selected_x]["v"].move(y, x):
                            if color == "white":
                                color = "black"
                            else:
                                color = "white"
                        TABLE_DICT[selected_y][selected_x]["rect"].setFill(TABLE_DICT[selected_y][selected_x]["color"])
                        selected_x = -1
                        selected_y = -1
                        selected = False
                    elif TABLE_DICT[y][x]["v"].color == TABLE_DICT[selected_y][selected_x]["v"].color:
                        TABLE_DICT[selected_y][selected_x]["rect"].setFill(TABLE_DICT[selected_y][selected_x]["color"])
                        TABLE_DICT[y][x]["rect"].setFill("red")
                        selected_x = x
                        selected_y = y
                        selected = True
                    else:
                        if TABLE_DICT[y][x]["v"].color != TABLE_DICT[selected_y][selected_x]["v"].color:
                            if TABLE_DICT[selected_y][selected_x]["v"].move(y,x):
                                if color == "white":
                                    color = "black"
                                else:
                                    color = "white"
                            TABLE_DICT[selected_y][selected_x]["rect"].setFill(TABLE_DICT[selected_y][selected_x]["color"])     
                            selected_x = -1
                            selected_y = -1
                            selected = False
    play()
