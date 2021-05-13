import time
def task1():
    # this code only if the input value is 1 and 0 
    start_time = time.time()
    parameter = input("enter your number: ")
    print(f'your parameter: {parameter}')
    # convert string into list
    list_input = list(parameter)
    result = []
    result_in_string = ""
    for i in list_input:
        if int(i) == 1:
            result.insert(len(result),i)
        elif int(i) == 0:
            result.insert(0,i)
        elif int(i) > 1:
            print("contain value higher then one")
            break
    print(result_in_string.join(result))
    print("execution time  --- %s seconds ---" % (time.time() - start_time))

def task2():
    start_time = time.time()
    list_parmater = input("please enter array elements seperated by space ")
    list_parmater_split = list_parmater.split(" ")
    print(list_parmater_split)
    target_paramter = input("please input your target: ")
    result = []
    for index, value in enumerate(list_parmater_split):
        if value >= target_paramter:
            # if array value is bigger then target continue to next value
            continue
        else:
            subtract_result = int(value) - int(target_paramter)
            try:
                substract_index = list_parmater_split.index(str(abs(subtract_result)))
            except Exception:
                # if enter exeception means that when we try to find the value inside the list we cannot find it 
                substract_index = None
                continue
            else:
                if substract_index:
                    result.append(index)
                    result.append(substract_index)
                    break
    if len(result) < 1:
        print("there is no answer")
    else:
        print("your first result is : %s" % result)
        print("execution time --- %s seconds ---" % (time.time() - start_time))
          

task2()