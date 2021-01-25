import sys


def decode_from_emoji(emoji):
    if emoji == "☒":
        return -1
    else:
        return 0


def encode_to_emoji(char):
    if char == -1:
        return "☒"
    elif char == -2:
        return "☺"
    elif char == -3:
        return "☼"
    else:
        return "."


f_in = open('1.map', "r", encoding="utf-8")
map = []
line = f_in.readline()
x, y, start_x, start_y, finish_x, finish_y = 0, 0, 0, 0, 0, 0

while line:
    x = 0
    line_arr = []
    for c in line:
        if c != "\n":
            if c == "☺":
                start_x, start_y = x, y
            elif c == "☼":
                finish_x, finish_y = x, y
            line_arr.append(decode_from_emoji(c))
            x += 1
    map.append(line_arr)
    line = f_in.readline()
    y += 1

width, height = x, y


def wave(x, y, cur, map):
    map[y][x] = cur
    if y + 1 < height:
        if map[y + 1][x] == 0 or (map[y + 1][x] != -1 and map[y + 1][x] > cur):
            wave(x, y + 1, cur + 1, map)
    if x + 1 < width:
        if map[y][x + 1] == 0 or (map[y][x + 1] != -1 and map[y][x + 1] > cur):
            wave(x + 1, y, cur + 1, map)
    if x - 1 >= 0:
        if map[y][x - 1] == 0 or (map[y][x - 1] != -1 and map[y][x - 1] > cur):
            wave(x - 1, y, cur + 1, map)
    if y - 1 >= 0:
        if map[y - 1][x] == 0 or (map[y - 1][x] != -1 and map[y - 1][x] > cur):
            wave(x, y - 1, cur + 1, map)
    return map


def rewind(map, finish_x, finish_y):
    if map[finish_y][finish_x] != 0:
        x, y = finish_x, finish_y
        while (x, y) != (start_x, start_y):
            prev_x, prev_y = x, y
            if map[y + 1][x - 1] + 1 == map[y][x]:
                y += 1
                x -= 1
            elif map[y + 1][x] + 1 == map[y][x]:
                y += 1
            elif map[y + 1][x + 1] + 1 == map[y][x]:
                x += 1
                y += 1
            elif map[y][x - 1] + 1 == map[y][x]:
                x -= 1
            elif map[y][x + 1] + 1 == map[y][x]:
                x += 1
            elif map[y - 1][x - 1] + 1 == map[y][x]:
                x -= 1
                y -= 1
            elif map[y - 1][x] + 1 == map[y][x]:
                y -= 1
            elif map[y - 1][x + 1] + 1 == map[y][x]:
                x += 1
                y -= 1
            map[prev_y][prev_x] = -2
        map[y][x] = -2
    else:
        map[start_y][start_x] = -2
    return map


wave(start_x, start_y, 1, map)

rewind(map, finish_x, finish_y)
map[finish_y][finish_x] = -3

for line in map:
    for c in line:
        print(encode_to_emoji(c), end="")
    print()

f_in.close()
