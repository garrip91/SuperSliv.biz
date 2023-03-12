#░▒▓

def carpet(width, height):

    border_line = "▓"+"▒"*(width-2)+"▓"
    middle_line = "▓"+"▒"+"▓"*(width-4)+"▒"+"▓"

    print(border_line)
    print((middle_line + "\n") * (height-2), end="")
    print(border_line)


carpet(12, 8)
