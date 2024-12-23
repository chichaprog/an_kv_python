#homework exercise number 1.
obj = {
    "key":30,
    "255":"wffff",
    "qwe":[1,2,4],
    488:"wdw",
}

obj.update({
    0:23,
    "mouse":112343
})



#homework exercises number 2.

obj = {
    1:1,
    8:2,
    27:3,
    64:4,
    125:5,
    216:6,
    343:7,
    512:8,
    729:9,
    1000:10

}


#homework  exercises number 5.


def calaculator(a,b,ops):

    r = 0

    match ops:
        case "+":
            r = a + b
        case "-":
            r = a - b
        case "*":
            r = a * b
        case "/":
            r = a / b
        case _: 
            print("enter operator simbol please")
    
    return r


def calaculator_v2():

    a = input("Input a value: ")
    b = input("Input b value: ")
    ops = input("Input operator (+,-,/,*): ")

    a = int(a)
    b = int(b)


    r = 0

    match ops:
        case "+":
            r = a + b
        case "-":
            r = a - b
        case "*":
            r = a * b
        case "/":
            r = a / b
        case _: 
            print("enter operator simbol please")
    
    return r


def dictionary_from_string(mystring: str):

    if len(mystring) == 0:
        print("mystring can't be null")
        return
    
    mydict = {}
    
    for i in range(0, len(mystring)):
        mydict[mystring[i]] = i

    print(mydict)
