# Created accumulators for both customers and the amount of tickets that are sold
tickets_sold = 0
customers = 0

# Created while loop defining reiteration until the target number of 20 is reached
while tickets_sold < 20:

    print('You can Buy up to 4 tickets')

    # gathers quantity entered by the user.
    number = int(input('How many tickets would you like to buy?: '))

    # Creates the bounds for how many tickets can be sold, with a minimum
    #of one and a maximum of four.
    if number < 1 or number > 4:

        # Lets user know that their quantity was not accepted by the program.
        print('You can only choose 1, 2, 3 or 4 as a quantity!')


    # This creates the else-if display message and returns the loop if the user
    # enters a quantity greater than the amount of tickets left to buy.
    elif 20 - tickets_sold < number:

            print('Sorry! There\'s only ' + str(20 - tickets_sold) + ' tickets left!' )

    # This adds to the tickets sold's accumulator as well as the customers' accumulator.
    # Then when before the loop reiterates, it displays how many tickets are
    # left available to buy in the program.
    else:

        tickets_sold = tickets_sold + number

        customers = customers + 1

        print('There are ' + str(20 - tickets_sold) + ' tickets left available to buy!')

# Displays final message when iterations of the loop finish.
print('All tickets are sold! The number of customers who bought is ' + str(customers) + ('.'))







