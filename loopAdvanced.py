def board_draw(height, width):
    square = 0
    print(" --- " * width)
    for x in range(height):
        line = "| "
        for i in range(0, width):
            line += format(square, '02d') + " | "
            square += 1
        print(line)
    print(" --- " * width)    

hinp= int(input("Enter the height of the board: "))
winp= int(input("Enter the width of the board: "))

board_draw(hinp,winp)
