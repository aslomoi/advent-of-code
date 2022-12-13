input_txt = "target area: x=241..273, y=-97..-63"
# input_txt = "target area: x=20..30, y=-10..-5"
x_lims = [int(x) for x in input_txt.split('x=')[1].split(',')[0].split('..')]
y_lims = [int(y) for y in input_txt.split('y=')[1].split(',')[0].split('..')]


def step(x, y, dx, dy):
    x += dx
    y += dy

    if dx > 0:
        dx -= 1
    elif dx < 0:
        dx += 1
    dy -= 1

    return x, y, dx, dy


def trajectory(dx, dy):
    x, y = 0, 0
    ymax = 0
    while True:
        x, y, dx, dy = step(x, y, dx, dy)
        if y > ymax:
            ymax = y
        if x_lims[0] <= x <= x_lims[1] and y_lims[0] <= y <= y_lims[1]:
            return True, ymax
        if x > x_lims[1] or y < y_lims[0]:
            return False, -1

ybest = 0
vels = []
for x in range(x_lims[1]+1):
    for y in range(-abs(y_lims[0]), abs(y_lims[0])):
        pos, ymax = trajectory(x, y)
        if pos:
            vels.append((x,y))
            if ymax > ybest:
                ybest = ymax
                best = (x,y)

print(f'{best}: {ybest}')
print('Length: ' + str(len(vels)))
