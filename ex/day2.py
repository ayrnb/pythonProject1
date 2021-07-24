
# def sum_2_num(num1,num2):
#
#     result=num1+num2
#     return result
# print(sum_2_num(10,20))
def print_lines(chars,times):
    print(chars*times)
def print_times(chars,times):
    """打印多行分隔线
    :param chars:
    :param times:
    """
    low=0
    while low<5:
        print_lines(chars,times)
        low+=1
print_times('*',5)