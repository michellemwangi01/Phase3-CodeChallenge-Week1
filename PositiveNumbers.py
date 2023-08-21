# Challenge 2: Two numbers are positive.
# Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True
# if exactly two of the three integers are positive numbers (greater than zero), and False - otherwise.
def positive_identifier(a,b,c):
    positive_nums = [num for num in [a,b,c] if num > 0]
    return f'Value is {True}' if len(positive_nums) == 2 else f'Value is {False}'

count = 1
value_list = []
while count < 4:
    try:
        value = int(input(f"input 3 numbers to check. Num {count}: "))
        value_list.append(value)
        count += 1
    except ValueError:
        print("Error! Value Must Be An Integer.")
a,b,c = value_list
print(a,b,c)

print(positive_identifier(a,b,c))


