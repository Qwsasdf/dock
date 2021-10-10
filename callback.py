def sum(a,b):
    return print("sum "+str(a+b))

def razn(a,b):
    return print("razn " + str(a - b))

def test_for_func_as_param(a,b,func_for_manipulate):
    func_for_manipulate(a,b)

a=50
b=30

test_for_func_as_param(a,b,sum)
test_for_func_as_param(a,b,razn)