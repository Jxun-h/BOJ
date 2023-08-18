ax, ay = 0, 0
bx, by = 0, 0

cx, cy = 0, 0
dx, dy = 0, 0


def point(ax, ay, bx, by, cx, cy, dx, dy):
    if ((ax, ay) == (dx, dy) or (bx, by) == (cx, cy) or (bx, ay) == (cx, dy) or (ax, by) == (dx, cy)):
        return True

    else:
        return False


def line(ax, ay, bx, by, cx, cy, dx, dy):
    if (((bx, by) == (cx, dy) and by > cy) or (((bx, ay) == (cx, cy) and dy > ay))
            or ((dx, cy) == (ax, ay) and by > cy) or ((dx, dy) == (ax, by) and dy > ay)

            or ((bx, by) == (cx, dy) and (bx, ay) == (cx, cy)) or ((ax, ay) == (dx, cy) and (dx, dy) == (ax, by))
            or ((cx, cy) == (ax, by) and (bx, by) == (dx, cy)) or ((ax, ay) == (cx, dy) and (dx, dy) == (bx, ay))

            or (ax == dx and (ay < cy < by or ay < dy < by)) or (bx == cx and (ay < cy < by or ay < dy < by))
            or (by == cy and (ax < cx < bx or ax < dx < bx)) or (ay == dy and (ax < cx < bx or ax < dx < bx))

            or (ax == dx and (cy < ay < dy or cy < by < dy)) or (bx == cx and (cy < ay < dy or cy < by < dy))
            or (by == cy and (cx < ax < dx or cx < bx < dx)) or (ay == dy and (cx < ax < dx or cx < bx < dx))

    ):
        return True
    else:
        return False


def null(ax, ay, bx, by, cx, cy, dx, dy):
    if bx < cx or dx < ax or by < cy or dy < ay:
        return True

    elif (bx - ax < dx - cx and by - ay < dy - cy and (cx < ax < dx and cx < bx < dx) and (
            cy < ay < dy and cy < by < dy)):
        return True
    elif (bx - ax > dx - cx and by - ay > dy - cy and (ax < cx < bx and ax < dx < bx) and (
            ay < cy < by and ay < dy < by)):
        return True
    else:
        return False


ax, ay, bx, by = map(int, input().split())
cx, cy, dx, dy = map(int, input().split())

if line(ax, ay, bx, by, cx, cy, dx, dy):
    print('LINE')
elif point(ax, ay, bx, by, cx, cy, dx, dy):
    print('POINT')
elif null(ax, ay, bx, by, cx, cy, dx, dy):
    print('NULL')
else:
    print('FACE')
