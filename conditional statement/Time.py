import time
# t=time.strftime('%H:%M:%S')
# print(t)
# t=int(time.strftime('%H'))
# print(t)
# t=int(time.strftime('%M'))
t=int(time.strftime('%H'))
print(t)
if t<12:
    print("Good Morning Sir")
elif t>=12 and t<=17:
    print("Good Evening Sir")
elif t>17 and t<=24:
    print("Good Night Sir")
    