name = "黑马程序员"
def print_line(chars,times):
    print(chars*times)
def print_lines(chars,times):
    """打印多行分隔线
    :param chars:
    :param times:
    """
    low=0
    while low<5:
        print_line(chars,times)
        low+=1
