"""
all constants and immutables could be here.
"""
HELLO = "HELLO"
# for early develop
Gofor = "Gofor"
Eat = "Eat"
Kill = "Kill"
FOOD = "FOOD"
Pacman = "Pacman"
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
