import os
import datetime
# import webbrowser

# The Challenge:
# using python docs
# strftime and strptime
# Make script that accepts month and day dates
# and returns wikipedia links for those dates.


def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def day_facts(dates):
    """Returns a wikipedia link for the date argument."""
    clear_screen()
    input_format = '%m/%d'
    link_date = "%B_%d"
    dates_list = dates.split()
    for day in dates_list:
        try:
            url_string = 'https://en.wikipedia.org/wiki/'
            datestring = datetime.datetime.strptime(day, input_format)
            url_string += datestring.strftime(link_date)
            # webbrowser.open_new(url_string)
            print("Your day is {}.".format(datestring.strftime('%B %d')))
            print(url_string + "\n" + ("*"*50))
        except ValueError:
            print('''
"{}" is not a valid date.  Please try again.
******************************'''.format(day.upper()))


if __name__ == "__main__":

    while True:

        dates = input(
            """Greetings!
            Please insert month/day dates in this format: 'MM/DD MM/DD'.
            Enter 'quit' to quit.
            > """)
        if dates.lower() == 'quit':
            break

        day_facts(dates)
