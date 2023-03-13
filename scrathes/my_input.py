# hello my_input


def my_password():
    word = input()
    password = ''
    for i in word:
        password += chr(ord(i) + pow(3, 2))
    return password


def unpass(password):
    key = ''
    for i in password:
        key += chr(ord(i) - pow(3, 2))
    return key

ps = my_password()

back = unpass(ps)

print(ps)
print(back)