
def draw_line(size, i):
    left_side = (size - i - 1) * " "
    right_side = "* " * (i + 1)
    return left_side + right_side.strip()

def draw_rhombus(size):
    for i in range(size):
        print(draw_line(size, i))

    for i in range(size - 2, -1, -1):
        print(draw_line(size, i))

N = int(input())
draw_rhombus(N)

# def draw_line(n, symbol):
#     return symbol * n
#
# def draw_triangle(size, symbol):
#     for i in range(1, size + 1):
#         print(draw_line(i, symbol))
#
#     for i in range(size - 1, -1, -1):
#         print(draw_line(i, symbol))
#
# # print(create_rhombus(5))
# draw_triangle(4, "+")
# draw_triangle(3, "*")