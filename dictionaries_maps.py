T = int(input())
data={}
for i in range(0,T):
    string = str(input()).split(" ")
    data[string[0]] = string[1]

for j in range(0,T):
    name = str(input())
    if name in data:
        print(name + "=" + data[name])
    else:
        print("Not found")