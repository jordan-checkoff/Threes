import pyautogui
import numpy as np
import cv2

BOARD_COLOR_1 = [20, 10, 150]
BOARD_COLOR_2 = [40, 30, 230]


def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    return bgr


def segment_screen(screenshot):
    contours = get_contours(screenshot)
    board_coords = get_board_coords(contours)
    next_coords = get_next_coords(contours)

    return (board_coords, next_coords)


def swipe_board(coords, dx, dy):
    x, y, w, h = coords
    x += w // 2
    y += h // 2
    pyautogui.moveTo(x//2, y//2)
    pyautogui.click()
    pyautogui.dragTo(x//2 + dx, y//2 + dy, 0.15, button="left")


def show_img(screenshot, coords=None):
    if coords:
        x, y, w, h = coords
        screenshot = screenshot[y:y+h, x:x+w]
    cv2.imshow("Window", screenshot)
    cv2.waitKey(0)




def get_contours(screenshot):
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, np.array(BOARD_COLOR_1), np.array(BOARD_COLOR_2))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3)))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours




def get_board_coords(contours):
    for segment in contours:
        x, y, w, h = cv2.boundingRect(segment)
        ratio = w / h
        if 0.74 < ratio < 0.76 and h > 20:
            return (x, y, w, h)

def get_next_coords(contours):
    for segment in contours:
        x, y, w, h = cv2.boundingRect(segment)
        ratio = w / h
        if 0.55 < ratio < 0.57:
            return ((x, y, w, h), 1)
        elif 0.81 < ratio < 0.82:
            return ((x, y, w, h), 2)
        elif 1.25 < ratio < 1.26:
            return ((x, y, w, h), 3)