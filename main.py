def fun(num , index , save = 1):
    if(index > 0):
        # print(index)
        return fun(num , index - 1 , save * num)
    return save
print(fun(5,5))



def fun(num , index , save = 1):
    if(index > 0):
        # print(index)
        return fun(num , index - 1 , save * num)
    return save
print(fun(2 , 3))



def fun_8(arr_loc:list , answer = 0 , index = 0):
    if(index != len(arr_loc)):
        return fun_8(arr_loc , answer + arr_loc[index] , index + 1)
    return answer

arr = [1,2,3,4,5]
print(fun_8(arr))



def array(arr,arr_2):
    if len(arr) == len(arr_2):
        