# def addition(num1, num2):
#     # print(num1+num2)
#     sum = num1 + num2
#     return sum
#
#
# sum = addition(addition(2,3), 4)
# print(sum)

def odd_or_even(num):
    if num%2 == 1:
        return "Odd Number"

    return "Even Number"

ans = odd_or_even(2)
print(ans)