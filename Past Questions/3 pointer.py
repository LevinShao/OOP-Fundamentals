def CheckUsername(username):
    if len(username) > 8 or username.isdigit():
        print("Error")
    else:
        print("Pass")

input = input("Input username > ")

CheckUsername(input)