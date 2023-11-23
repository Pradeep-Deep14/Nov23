def my_fun(x,y):
    if y == 0:
        return 1
    else:
        return x * my_fun(x,y-1)
print(my_fun(2,4))
