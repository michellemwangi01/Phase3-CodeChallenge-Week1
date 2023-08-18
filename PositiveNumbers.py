def positive_identifier(a,b,c):
    positive_nums = [num for num in [a,b,c] if num > 0]
    return True if len(positive_nums) == 2 else False


print(positive_identifier(-14, -3, -4))