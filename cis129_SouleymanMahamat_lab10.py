'''
Souleyman Mahamat
CIS-129

This script takes an integer or float as input. And returns it in check protection
format. If the final formatted number is less than 10 characters long, leading
asterisks are added.
'''


from sys import exit

# check if input is valid
def isinvalid(amount):

    if amount.isdigit():
        return False

    try:
        float(amount)
    except:
        return True

    return False


def check_protection(amount):

    amount = float(amount) # convert to float
    amount = f'{amount:*>10,.2f}' # format with ',' grouping, leading '*'s if less than 10 chars, 2 decimal points
    return amount


amount = input("amount (number only, 'exit' to quit): ")

# keep asking for input if input is invalid or exit
while isinvalid(amount):

    if 'exit' == amount.lower():
        exit()

    amount = input("amount (number only, 'exit' to quit): ")


print(check_protection(amount))
