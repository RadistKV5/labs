# TODO решите задачу
def task() -> float:
    dict_numbers = 0
    sum_ = 0
    num1 = 0
    num2 = 0
    input_ = open("input.json", "r")
    dict_numbers = input_.readlines()
    for i in range(len(dict_numbers)):
        if dict_numbers[i].find("score") != -1:
            num1 = float(dict_numbers[i][((dict_numbers[i].find("score"))+8):len(dict_numbers[i])-2])
        elif (dict_numbers[i].find("weight")) != -1:
            num2 = float(dict_numbers[i][((dict_numbers[i].find("weight"))+9):len(dict_numbers[i])-1])
        if(num1 != 0) and (num2 != 0):
            sum_ += num1*num2
            num1, num2 = 0, 0
    input_.close()
    return round(sum_, ndigits=3)


print(task())
