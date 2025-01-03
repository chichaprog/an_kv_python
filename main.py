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


obj = {}
def array(arr,arr_2 , index = 0 , save_dist = {}):
    if len(arr) != len(arr_2):
        return None
    if (index > 0):
        return(arr,index + 1,save_dist + arr_2)
    print("1")  
index = 0
arr = [1,2,3,4]
arr_2 = [9,7,6,5]
obj[arr[index]] = [arr_2[index]]
       