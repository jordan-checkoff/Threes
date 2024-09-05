import cv2


PATH = "./src/controller/images"

board_templates = {}
tiles = [0, 1, 2, 3, 6, 12, 24, 48, 96, 192, 384]
for tile in tiles:
    board_templates[tile] = cv2.imread(f'{PATH}/board_tiles/{tile}.jpg', cv2.IMREAD_GRAYSCALE)


next_templates = {}
tiles = [1, 2, 3, 6, 12]
for tile in tiles:
    next_templates[tile] = cv2.imread(f'{PATH}/next_tiles/{tile}.jpg', cv2.IMREAD_GRAYSCALE)


def match_tile(img, template, w, h):
    val = None
    score = 0

    for num, template in template.items():
        resized_template = cv2.resize(template, (w, h))
        res = cv2.matchTemplate(img, resized_template, cv2.TM_CCORR_NORMED)
        if res > score:
            score = res
            val = num
    return val