def wait(x):
    from time import sleep
    sleep(x)

inputtime=input("Enter time:")
t=int(inputtime)
while t>0:
    print(t)
    t=t-1
    wait(1)
print("hahahahaha")
