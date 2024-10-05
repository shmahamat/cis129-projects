keep_going = 'y'

#function that gets data
def getBottles():
    nbr_of_days = 7
    today_bottles = 0
    total_bottles = 0
    counter = 1

    while counter <= nbr_of_days:
        today_bottles = int(input('Enter number of bottles returned for day #' + str(counter) + ': '))
        total_bottles += today_bottles
        counter += 1
    
    return total_bottles

# main loop to get data and display results
while keep_going == 'y':
    total_payout = 0
    total_bottles = getBottles()
    # calculate payout
    payout_per_bottle = .10
    total_payout = total_bottles * payout_per_bottle
    print('\nthe total number of bottles collected is ',total_bottles)
    print(f'''The total paid out is $ {total_payout:.1f}''')
    print('\nDo you want to enter another week\'s worth of data?')
    keep_going = input('(Enter y or n): ')
    if keep_going == 'y':
        print()