def factorial ( a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
    
def fabonici(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fabonici(a-1)+fabonici(a-2)
print(factorial(5))
print(fabonici(3))