import cv2
import screen
import templates
import transforms




def get_state():
    screenshot = screen.take_screenshot()
    board_coords, next_coords = screen.segment_screen(screenshot)

    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    board = get_board(board_coords, gray)
    next = get_next(next_coords[0], next_coords[1], gray)

    print(board, next)

    return (board, next)


def change_state(dir):
    screenshot = screen.take_screenshot()
    board_coords, next_coords = screen.segment_screen(screenshot)

    if dir == 0:
        screen.swipe_board(board_coords, 0, -100)
    elif dir == 1:
        screen.swipe_board(board_coords, 100, 0)
    elif dir == 2:
        screen.swipe_board(board_coords, 0, 100)
    elif dir == 3:
        screen.swipe_board(board_coords, -100, 0)






def get_next(coords, n, gray):
    x, y, w, h = transforms.next_transform(coords, n)

    tile = gray[y:y+h, x:x+w]
    val = templates.match_tile(tile, templates.next_templates, w, h)

    if n == 1:
        return [val]
    elif n == 2:
        return [val, val*2]
    elif n == 3:
        return [val, val*2, val*4]


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
                         
            val = templates.match_tile(tile, templates.board_templates, w, h)
            
            row.append(val)
        board.append(row)

    return board



if __name__ == "__main__":
    change_state(1)