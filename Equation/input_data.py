def input_lenght():
    my_input = input().split(' ')
    if len(my_input) == 3:
        return my_input
    else:
        return 'Invalid Input Length'
