'''
    This script gets information from the user to and displays the minimum
    number of packages of hotdogs and hotdog buns as well the leftovers
    for a hotdog cookout.

    By Souleyman Mahamat
    cis-129
'''

def get_total_hotdogs():
    '''This function get the values for the variables below.'''

    attendees = int(input('Maximum number of attendees? : '))
    hotdogs = int(input('How many hotdogs per attendee? : '))
    total = attendees*hotdogs
    return total


def show_results(total):
    '''This function does the calculations and displays the results when passed
    the total number of hotdogs.'''

    DOGS = 10 # number of hotdogs per package
    BUNS = 8 # number of hotdog buns per package

    if total_hotdogs%DOGS == 0:
        min_dogs = total//DOGS
    else:
        min_dogs = total//DOGS + 1

    if total_hotdogs%BUNS == 0:
        min_buns = total//BUNS
    else:
        min_buns = total//BUNS + 1

    dogs_left = min_dogs*DOGS - total_hotdogs
    buns_left = min_buns*BUNS - total_hotdogs

    print('Minimum packages of hot dogs needed : ',min_dogs)
    print('Minimum packages of hot dog buns needed : ',min_buns)
    print('Hot dogs remaining : ',dogs_left)
    print('Hot dog buns remaining : ',buns_left)

total_hotdogs = get_total_hotdogs()
show_results(total_hotdogs)
