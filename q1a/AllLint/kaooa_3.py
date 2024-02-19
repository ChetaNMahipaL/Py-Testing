"""
This module initializes and imports the pygame library.
"""
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((800, 800))

#Title and Icon
pygame.display.set_caption("Board Game")

# background
backgorund = pygame.image.load('bg.png')

# Adding heading
font = pygame.font.Font('freesansbold.ttf', 84)
# create a text surface object,
# on which text is drawn on it.
text = font.render('KAOOA', True, (255,255,255))
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
# set the center of the rectangular object.
textRect.center = (400, 75)
TURN = 0
pawns = []
DEAD_CROW = 0

# Run until the user asks to quit
RUNNING = True
DRAGGING = False
CR_INTERIM_POS = (0,0)
VR_INTERIM_POS = (0,0)

pos_1 = (398,236)
pos_2 = (228,360)
pos_3 = (357,360)
pos_4 = (438,360)
pos_5 = (568,360)
pos_6 = (332,436)
pos_7 = (463,436)
pos_8 = (398,484)
pos_9 = (293,560)
pos_10 = (502,560)

adj_dict = {
    pos_1: [pos_3, pos_4],
    pos_2: [pos_3, pos_6],
    pos_3: [pos_2, pos_4, pos_6, pos_1],
    pos_4: [pos_3, pos_5, pos_7, pos_1],
    pos_5: [pos_4, pos_7],
    pos_6: [pos_2, pos_3, pos_8, pos_9],
    pos_7: [pos_4, pos_5, pos_8, pos_10],
    pos_8: [pos_10, pos_9, pos_6, pos_7],
    pos_9: [pos_6, pos_8],
    pos_10: [pos_7, pos_8]
}

lines = [[] for _ in range(5)]

lines[0] = [pos_1, pos_3, pos_6, pos_9]
lines[1] = [pos_1, pos_4, pos_7, pos_10]
lines[2] = [pos_2, pos_3, pos_4, pos_5]
lines[3] = [pos_2, pos_6, pos_8, pos_10]
lines[4] = [pos_5, pos_7, pos_8, pos_9]

def cr_check(coord,color):
    """
    This function checks position for crow
    """
    for pawn in pawns:
        if pawn[0] == coord:
            if color == pawn[1]:
                return 1
            else:
                return 0
    if CR_INTERIM_POS == (0,0):
        return 2
    if DRAGGING:
        if coord in adj_dict[CR_INTERIM_POS]:
            return 2
        else:
            return -1
    return 2

def find_list_with_points(lines_1, point1, point2):
    """
    This function checks position for vulture to kill crows
    """
    for line in enumerate(lines_1):
        if point1 in line and point2 in line:
            index_point1 = line.index(point1)
            index_point2 = line.index(point2)
            return line, index_point1, index_point2
    return -1

def vr_check(coord,color,drag):
    """
    This function checks position for vulture
    """
    global DEAD_CROW
    for pawn in pawns:
        if pawn[0] == coord:
            if color == pawn[1]:
                return 1
            else:
                return 0
    if drag is True:
        return -1
    if VR_INTERIM_POS == (0,0):
        return 2
    result = find_list_with_points(lines,coord,VR_INTERIM_POS)
    if result == (-1):
        return -1
    else:
        req_line,index_1,index_2= find_list_with_points(lines,coord,VR_INTERIM_POS)
        if abs(index_1 - index_2 ) == 3:
            return -1
        else:
            if (index_1 + index_2) % 2 == 0:
                if cr_check(req_line[int((index_1+index_2)/2)],opponent_1.color) == 1:
                    DEAD_CROW = DEAD_CROW + 1
                    pawns.remove((req_line[int((index_1+index_2)/2)],opponent_1.color))
                else:
                    return -1
            return 2

def get_coord():
    """
    This function get's co-ordinates from board
    """
    x_coordinate, y_coordinate = pygame.mouse.get_pos()
    if 547 < y_coordinate < 573:
        if 489 < x_coordinate < 515:
            return (502,560)
        if 280 < x_coordinate < 306:
            return (293,560)
    elif 347 < y_coordinate < 373:
        if 555 < x_coordinate < 581:
            return (568,360)
        if 425 < x_coordinate < 451:
            return (438,360)
        if 344 < x_coordinate < 370:
            return (357,360)
        if 215 < x_coordinate < 241:
            return (228,360)
    elif  423 < y_coordinate < 449:
        if 450 < x_coordinate < 476:
            return (463,436)
        if 319 < x_coordinate < 345:
            return (332,436)
    elif 385 < x_coordinate < 411:
        if  471 < y_coordinate < 497:
            return (398,484)
        if  223 < y_coordinate < 249:
            return (398,236)
    else:
        return (-1,-1)

def draw(circles):
    """
    This function draws circles representing pawwns
    """
    for circle in circles:
        pygame.draw.circle(screen, circle[1], circle[0], 12)

def check_win():
    """
    This function checks result
    """
    global RUNNING
    if DEAD_CROW >= 4:
        font_1 = pygame.font.Font(None, 36)
        text_1 = font_1.render("Opponent_2 Wins!", True, (0, 0, 0))
        test_react_1 = text_1.get_rect()
        test_react_1.center = (400, 150)
        screen.blit(text_1,test_react_1)
        pygame.display.update()
        pygame.time.delay(2000)
        RUNNING = False
    else:
        win_flag = 0
        for line in enumerate(lines):
            if VR_INTERIM_POS in line:
                index = line.index(VR_INTERIM_POS)
                if index in (1,2):
                    win_flag = all(cr_check(line_point, opponent_1.color) == 1 and
                                   line_point != VR_INTERIM_POS for line_point in line[1:])
                    if not win_flag:
                        break
                else:
                    win_flag = cr_check(line[1],
                                        opponent_1.color) == cr_check(line[2],
                    opponent_1.color) == 1
                    if not win_flag:
                        break

        if win_flag == 1:
            # print("Yes")
            font_1 = pygame.font.Font(None, 36)
            text_1 = font_1.render("Opponent_1 Wins!", True, (0, 0, 0))
            test_react_1 = text_1.get_rect()
            test_react_1.center = (400, 150)
            screen.blit(text_1,test_react_1)
            pygame.display.update()
            pygame.time.delay(2000)
            RUNNING = False


class Crow:
    """
        Takes care of crows functions
    """
    def __init__(self,color,count):
        """
        This intialize the class
        """
        self.color = color
        self.count = count

    def cr_movement(self,event_1):
        """
        This function implement crow's move
        """
        global DRAGGING
        global CR_INTERIM_POS
        global TURN
        if event_1.type == pygame.MOUSEBUTTONDOWN:
            pos = get_coord()
            static = cr_check(pos,self.color)
            if static == 1:
                DRAGGING = True
                CR_INTERIM_POS = pos
                pawns.remove((pos,self.color))
        if event_1.type == pygame.MOUSEBUTTONUP:
            pos = get_coord()
            static = cr_check(pos,self.color)
            if DRAGGING and pos != (-1,-1):
                if static == 2 and self.count >= 7:
                    temp = (pos,self.color)
                    pawns.append(temp)
                    TURN = (TURN + 1) % 2
                else:
                    temp = (CR_INTERIM_POS,self.color)
                    pawns.append(temp)
                DRAGGING = False
            elif self.count < 7 and pos != (-1,-1) and DRAGGING is False:
                if static == 2:
                    self.count = self.count + 1
                    temp = (pos,self.color)
                    pawns.append(temp)
                    TURN = (TURN + 1) % 2


class Vulture:
    """
        Takes care of vultures functions
    """
    def __init__(self,color,count):
        """
        This intializes class
        """
        self.color = color
        self.count = count

    def vr_movement(self,event_2):
        """
        This function implements vulture's move
        """
        global DRAGGING
        global VR_INTERIM_POS
        global TURN
        if event_2.type == pygame.MOUSEBUTTONDOWN:
            pos = get_coord()
            static = vr_check(pos,self.color,True)
            # print(static)
            if static == 1:
                DRAGGING = True
                VR_INTERIM_POS = pos
                pawns.remove((pos,self.color))
        if event_2.type == pygame.MOUSEBUTTONUP:
            pos = get_coord()
            if DRAGGING and pos != (-1,-1):
                static = vr_check(pos,self.color,False)
                # print(static)
                if static == 2:
                    temp = (pos,self.color)
                    pawns.append(temp)
                    VR_INTERIM_POS = pos
                    TURN = (TURN + 1) % 2
                else:
                    temp = (VR_INTERIM_POS,self.color)
                    pawns.append(temp)
                DRAGGING = False
            elif self.count < 1 and pos != (-1,-1):
                static = vr_check(pos,self.color,False)
                if static == 2:
                    self.count = self.count + 1
                    temp = (pos,self.color)
                    pawns.append(temp)
                    TURN = (TURN + 1) % 2
                    VR_INTERIM_POS = pos


opponent_1 = Crow((127, 255, 212),0)
opponent_2 = Vulture((255, 234, 0),0)


while RUNNING:

    screen.fill((255,140,0))
    # update background image
    screen.blit(backgorund,(150,150))
    screen.blit(text,textRect)

    for event in pygame.event.get():

        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            RUNNING = False
        # print(TURN)
        if TURN == 0:
            opponent_1.cr_movement(event)
        else:
            opponent_2.vr_movement(event)
        # set the center of the rectangular object.vement(event)
    if DRAGGING:
        continue
    draw(pawns)
    pygame.display.update()
    check_win()
    # # get pawns co-ordinate
    # x, y = pygame.mouse.get_pos()
    # print(x)
    # print(y)
    # must to make changes visible
# Done! Time to quit.
pygame.quit()
