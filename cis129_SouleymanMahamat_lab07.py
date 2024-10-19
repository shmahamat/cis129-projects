from sys import exit

'''
This script gets the number of tickets sold for every predefined section from
the user while displaying the subtotal so far, then displays the subtotals for 
each section and the grand total.
'''

# sections by name
section_names = ('A','B','C')

# price per seat for each section
A_COST = 20
B_COST = 15
C_COST = 10

# number of seats per section
A_SEATS = 300
B_SEATS = 500
C_SEATS = 200

# each section defined as tuple for easier manipulation later
A = (section_names[0],A_SEATS,A_COST)
B = (section_names[1],B_SEATS,B_COST)
C = (section_names[2],C_SEATS,C_COST)

# sections placed in list for easier manipulation later
sections = [A,B,C]

#  welcome message with all the constant values
print(f"{'Section':<10} {'Seats':<10} {'Price/Seat'}")
for i in range(len(sections)):
    print(f'{sections[i][0]:<10} {sections[i][1]:<10} ${sections[i][2]}')


def isInvalid(section,tickets):
    '''
    This function returns True if the the number of tickets sold 
    entered is greater than the number of seats in the section, is negative, 
    or is not an integer.
    '''

    if tickets.lower == 'exit':
        return False
    
    #attempt to convert input tickets to integer
    try:
        tickets = int(tickets)
    except ValueError:
        return True
    
    if tickets > section[1] or tickets < 0:
        return True
    
    return False
   
    
def getTickets(section):
    '''This function gets the number of tickests sold from user.'''
    
    tickets = input(f'\nSection {section[0]} tickets sold (maximum {section[1]}, \'exit\' to quit): ')
    
    if tickets.lower() == 'exit':
        exit()
    
    while isInvalid(section,tickets):
        print('Invalid, try again. ')
        tickets = input(f'\nSection {section[0]} tickets sold (maximum {section[1]}, \'exit\' to quit): ')
    
    tickets = int(tickets)
    return tickets

# for each section, get number of tickets from user, display total so far,
# and store section subtotals in a list
subtotals = []
for section in sections:
    subtotals.append(getTickets(section) * section[2])
    print(f'Total so far: ${sum(subtotals)}')

print()

# for each section display subtotal
for i in range(len(sections)):
    print(f'Section {sections[i][0]} subtotal: ${subtotals[i]}')
    
print(f'\nGrand Total: ${sum(subtotals)}')
