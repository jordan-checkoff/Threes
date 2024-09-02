import pyautogui
import numpy as np
import cv2
import math



class Controls():

    def __init__(self):
        self.templates = {}
        tiles = [0, 1, 2, 3, 6, 12, 24, 48, 96, 192, 384]
        for tile in tiles:
            self.templates[tile] = cv2.imread(f'./{tile}.jpg', cv2.IMREAD_GRAYSCALE)

        self.next_templates = {}
        tiles = [1, 2, 3]
        for tile in tiles:
            self.next_templates[tile] = cv2.imread(f'./_{tile}.jpg', cv2.IMREAD_GRAYSCALE)


    def take_picture(self):

        # Take screenshot
        screenshot = self.take_screenshot()

        # Segment game sections
        sections = self.get_game_sections(screenshot)

        # Segment board
        board_segment = self.segment_board(sections["board"])

        # Identify tiles
        board = self.identify_tiles(screenshot, board_segment)

        # Segment next tile
        next_tile_segment = self.segment_next_tile(screenshot, sections["next_tile"])

        # Identify next tile

        print(next_tile_segment)
        print(board)



    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        return cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    
    def get_game_sections(self, screenshot):
        hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv, np.array([20, 10, 150]), np.array([40, 30, 230]))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7, 7)))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        segments = {}

        for segment in contours:
            x, y, w, h = cv2.boundingRect(segment)
            ratio = w / h
            if 0.74 < ratio < 0.76:
                segments["board"] = (x, y, w, h)
            elif 0.55 < ratio < 0.57:
                segments["next_tile"] = (x, y, w, h)

        return segments
    

    def segment_board(self, coords):
        x, y, w, h = coords

        y += round(h * 0.03)
        x += round(w * 0.04)
        tile_height = round(h * 0.225)
        tile_width = round(h * 0.15)
        y_gap = round(h * 0.014)
        x_gap = round(w * 0.04)

        board = []

        for i in range(4):
            row = []
            for j in range(4):
                y_start = y + (tile_height + y_gap) * i
                x_start = x + (tile_width + x_gap) * j
                row.append((x_start, tile_width, y_start, tile_height))
            board.append(row)

        return board


    def identify_tiles(self, screenshot, coords):
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        board = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(self.identify_tile(thresh, coords[i][j]))
                # if i == 3 and j == 0:
                #     x, w, y, h = coords[i][j]
                #     cv2.imwrite("1.jpg", thresh[y:y+h, x:x+w])
            board.append(row)
        
        return board
            

    def identify_tile(self, screenshot, coords):
        val = None
        score = 0

        for num, template in self.templates.items():    
            x, w, y, h = coords
            resized_template = cv2.resize(template, (w, h))
            res = cv2.matchTemplate(screenshot[y:y+h, x:x+w], resized_template, cv2.TM_CCORR_NORMED)
            if res > score:
                score = res
                val = num

        return val


    def segment_next_tile(self, screenshot, coords):
        x, y, w, h = coords
        
        x += round(0.22 * w)
        y += round(0.43 * h)
        w = round (0.58 * w)
        h = round(0.44 * h)

        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        score = 0
        val = None

        for num, template in self.next_templates.items():
            resized_template = cv2.resize(template, (w, h))
            res = cv2.matchTemplate(gray[y:y+h, x:x+w], resized_template, cv2.TM_CCORR_NORMED)
            if res > score:
                score = res
                val = num

        return val

        # cv2.imwrite("_2.jpg", screenshot[y:y+tile_height, x:x+tile_width])
        # self.show_img(screenshot[y:y+tile_height, x:x+tile_width])


    def show_img(self, img):
        cv2.imshow("Window", img)
        cv2.waitKey(0)


if __name__ == "__main__":
    controls = Controls()
    controls.take_picture()