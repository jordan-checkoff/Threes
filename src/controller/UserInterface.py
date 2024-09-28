import controller.screen as screen
import cv2
import controller.transforms as transforms
import controller.templates as templates
import time
from model.Directions import Directions

class UserInterface():

    def __init__(self):
        screenshot = screen.take_screenshot()
        board_coords, next_coords = screen.segment_screen(screenshot)
        self.board_coords = board_coords

    
    def get_state(self):
        time.sleep(0.5)
        screenshot = screen.take_screenshot()
        board_coords, next_coords = screen.segment_screen(screenshot)

        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        board = get_board(board_coords, gray)
        next = get_next(next_coords[0], next_coords[1], gray)

        print(board, next)

        return (board, next)
    

    def change_state(self, dir):
        match dir:
            case Directions.UP:
                screen.swipe_board(self.board_coords, 0, -100)
            case Directions.RIGHT:
                screen.swipe_board(self.board_coords, 100, 0)
            case Directions.DOWN:
                screen.swipe_board(self.board_coords, 0, 100)
            case Directions.LEFT:
                screen.swipe_board(self.board_coords, -100, 0)
    



def get_board(coords, gray):
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    x, y, w, h, xg, yg = transforms.board_transform(coords)

    board = []

    for i in range(4):
        row = []
        for j in range(4):
            x_start = x + (w + xg) * j
            y_start = y + (h + yg) * i
            tile = thresh[y_start:y_start+h, x_start:x_start+w]

            # if i == 2 and j == 2:
            #     cv2.imwrite("1536.jpg", tile)
            #     exit()
                         
            val = templates.match_tile(tile, templates.board_templates, w, h)
            
            row.append(val)
        board.append(row)

    return board

def get_next(coords, n, gray):
    x, y, w, h = transforms.next_transform(coords, n)

    tile = gray[y:y+h, x:x+w]
    # cv2.imwrite("48.jpg", tile)
    # exit()
    val = templates.match_tile(tile, templates.next_templates, w, h)

    if n == 1:
        return [val]
    
    elif val == 1:
        exit()

    elif n == 2:
        return [val, val*2]
    elif n == 3:
        return [val, val*2, val*4]