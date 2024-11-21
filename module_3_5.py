def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    print(first,str_number)
    if len(str_number) == 1:
        return first
    elif len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
print(get_multiplied_digits(40203))