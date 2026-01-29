"""Version 1"""
# def color_code(color):
#     complement_values = {
#         "black": 0,
#         "brown": 1,
#         "red": 2,
#         "orange": 3,
#         "yellow": 4,
#         "green": 5,
#         "blue": 6,
#         "violet": 7,
#         "grey": 8,
#         "white": 9
#     }
#     return complement_values[color]

"""Version 2"""
def color_code(color):
    return colors().index(color)

def colors():
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]

