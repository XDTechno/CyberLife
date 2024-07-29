"""
all constants and immutables could be here.
"""
HELLO = 114514
# for early develop
Gofor = 232
Eat = 1919810
Kill = 1919811
FOOD = 1919
Pacman = 2222
move_cmd = {
    "right": 0xA8,
    "left": 0xA9,
    "up": 0xAA,
    "down": 0xAB
}

move_direction = {
    0xA8: [1, 0]
    , 0xA9: [-1, 0]
    , 0xaa: [0, -1]
    , 0xab: [0, 1]
}
