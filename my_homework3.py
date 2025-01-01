import math

n = 5
result = math.factorial(n)
print("Факториал числа", n, "равен", result)



def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
    
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))




def sum_numbers(list):
    sum = 0
    for i in range(0, len(list)):
        sum += list[i]
    
    return sum

list = [1,4,6,8,9]
sum = sum_numbers(list)
print(f'sum of list is {sum}')




def list(obj):
    print(obj.popitem())
    print(obj)






array = [2,"ooo",4,5,9,"fab",99,3]

def remove_strs(list):
    new_array = []

    for value in list:
        try:
            int(value)
            new_array.append(value)
        except:
            pass
    
    return new_array

print(array)
print(remove_strs(array))
