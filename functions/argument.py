# Required arguments
def mean( a,b):
    mean=(a*b)/(a+b)
    #also give value using return
    return mean
    
a=8
b=9
print(mean(a,b))



# default argument
def mean( a=9,b=5):
    mean=(a*b)/(a+b)
    print(mean)
mean()
a=3
mean(a)

