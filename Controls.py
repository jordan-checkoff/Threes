import pyautogui
import numpy as np
import cv2
import math

class Controls():

    def __init__(self):
        self.templates = {}
        tiles = [3, 6, 12, 24, 48, 96]
        for tile in tiles:
            self.templates[tile] = cv2.imread(f'./{tile}.png', cv2.IMREAD_GRAYSCALE)


    def take_picture(self):

        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)

        hsv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2HSV)
        gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        
        contours = {}
        contours["red"] = self.get_contours(hsv, [150, 100, 200], [179, 200, 255], 25)
        contours["blue"] = self.get_contours(hsv, [100, 100, 200], [110, 125, 255], 25)
        contours["white"] = self.get_contours(hsv, [89, 0, 253], [91, 2, 255], 5)
        contours["gray"] = self.get_contours(hsv, [91, 28, 217], [91, 28, 217], 25)


        tiles = []
        next_tiles = []
        width = None
        for color, color_contours in contours.items():
            for tile in color_contours:
                x, y, w, h = cv2.boundingRect(tile)
                if not width:
                    width = w
                if w > width - 20 and w < w + 20:
                    tiles.append((x, y, w, h, color))
                else:
                    next_tiles.append((x, y, w, h, color))

        board = self.get_board(tiles, thresh)
        next = self.get_next_tiles(next_tiles, thresh)

        print(board, next)

        return (board, next)

        


    def show_img(self, img):
        cv2.imshow("Window", img)
        cv2.waitKey(0)

    def get_contours(self, img, lower_hsv, upper_hsv, kernel_size):
        mask = cv2.inRange(img, np.array(lower_hsv), np.array(upper_hsv))
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def get_tile_number(self, tile, thresh, templates):
        x, y, w, h, c = tile
        if c == "gray":
            return 0
        elif c == "blue":
            return 1
        elif c == "red":
            return 2
        else:
            tile_img = thresh[y:y+h, x:x+w]
            for num, template in templates.items():
                resized_template = cv2.resize(template, (w, h))
                res = cv2.matchTemplate(tile_img, resized_template, cv2.TM_CCOEFF_NORMED)
                if res > 0.8:
                    return num

    def get_board(self, tiles, thresh):
        tiles.sort(key=lambda x: (math.ceil(x[0] / 100.0) * 100, math.ceil(x[1] / 100.0) * 100))
        board = [[None for _ in range(4)] for _ in range(4)]
        
        i = 0
        for tile in tiles:
            board[i % 4][i // 4] = self.get_tile_number(tile, thresh, self.templates)
            i += 1

        return board

    def get_next_tiles(self, tiles, thresh):
        next_tiles = []
        for tile in tiles:
            next_tiles.append(self.get_tile_number(tile, thresh, self.templates))
        return next_tiles

    def make_move(self, move):
        pass


if __name__ == "__main__":
    controls = Controls2()
    controls.take_picture()
    # x, y = pyautogui.locateCenterOnScreen('terminal.png')