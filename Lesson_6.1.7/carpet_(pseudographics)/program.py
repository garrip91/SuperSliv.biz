def draw_carpet(w=0, h=0):
    """Принимает ширину и высоту в клетках и генерирует \"ковёр\" из псевдографики"""


    result = ""
    for i in range(h):
        result += f"XXXX*{'#'*w}*XXXX\n"
    return result


print(draw_carpet(10,10))
