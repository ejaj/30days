N = int(input())

output = []
for i in range(0,N):
    user_input = input().split()

    if user_input[0] == "print":
        print(output)
    elif user_input[0] == "insert":
        output.insert(int(user_input[1]), int(user_input[2]))
    elif user_input[0] == "remove":
        output.remove(int(user_input[1]))
    elif user_input[0] == "pop":
        output.pop()
    elif user_input[0] == "append":
        output.append(int(user_input[1]))
    elif user_input[0] == "sort":
        output.sort()
    else:
        output.reverse()