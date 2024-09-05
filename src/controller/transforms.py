

def transform(coords, xt, yt, wt, ht, xgt, ygt):
    x, y, w, h = coords

    x += round(w * xt)
    y += round(h * yt)
    tw = round(w * wt)
    th = round(h * ht)
    xg = round(w * xgt)
    yg = round(h * ygt)

    return (x, y, tw, th, xg, yg)


def board_transform(coords):
    return transform(coords, 0.04, 0.03, 0.2, 0.225, 0.04, 0.014)

def next_transform(coords, n):
    c = None
    if n == 1:
        c = transform(coords, 0.22, 0.43, 0.58, 0.44, 0, 0)
    return (c[0], c[1], c[2], c[3])