#!/usr/bin/env python3

from collections import OrderedDict
import textwrap
import sys

# Global dictionary containing donor list and donation amounts
donor_dict = {"Harry Potter": [10000, 5000, 500.55], "Ronald Weasley": [2499.99, 7500.01], "Hermione Granger": [100, 2000, 30000], "Draco Malfoy": [10, 888.88], "Neville Longbottom": [10]}

# Email template for Thank You message
email = textwrap.dedent('''
    Dear {:s},

    Thank you for your very kind donation of ${:.2f}.
    It will be put to very good use.

    Sincerely,
    -Hogwarts School of Witchcraft and Wizardry

    ''')


def send_thankyou():
    """
    Provides the following functionality:
    1. Lists all donors
    2. Adds new donors
    3. Enters new donations
    4. Sends a thank you email

    Args: None
    """
    donor_name = input("Please enter the full name of a donor. You can also enter list to see all current donors or 'e' to exit: ")
    if donor_name == "e":
        return

    while donor_name != "list":
        while True:
            donation_amount = input("Please enter the donation amount or 'e' to exit: ")
            if donation_amount == "e":
                return
            try:
                donation_amount = float(donation_amount)
            except ValueError:
                print("Invalid donation amount. Please try again.\n")
            else:
                break

        if donor_name in donor_dict:
            donor_dict[donor_name].append(donation_amount)
        else:
            donor_dict[donor_name] = [float(donation_amount)]

        print(email.format(donor_name, donation_amount))
        return

    if donor_name == "list":
        for donor in donor_dict:
            print(donor)


def create_report():
    """
    Prints a report of all donors sorted by total donations descending.

    Args: None
    """
    print ("{:30s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num donations", "Average donation"))
    print ("-" * 71)

    sorted_donor_dict = OrderedDict(sorted(donor_dict.items(), key=lambda i: sum(i[1]), reverse=True))
    
    for (donor, donations) in sorted_donor_dict.items():
        donor_name = donor
        total_given = sum(donations)
        num_donations = len(donations)
        average_donation = (total_given / num_donations)
        print ("{:30s}  ${:11.2f}   {:9d}  ${:12.2f}".format(donor_name, total_given, num_donations, average_donation))


def create_email_file():
    """
    Creates a text file with a thank you message

    Args: None
    """
    for donor, donation in donor_dict.items():
        filename = donor + ".txt"
        letter = email.format(donor, donation[-1])
        try:
            with open(filename, 'w') as outfile:
                outfile.write(letter)
        except IOError:
            print("Unable to open file or write file.")

def abort():
    """
    Quit the script

    Args: None
    """
    print("Bye!")
    sys.exit()


"""
The funtion below produce the main selection menu
"""

def menu_selection(prompt, menu_dict):
    while True:
        try:
            response = input(prompt)
            menu_dict[response]()
        except KeyError:
            print("Please select a valid selection from the menu.")


main_prompt = ("""\nChoose an action:
      1 - Send a Thank You
      2 - Create a Report
      3 - Send letters to everyone
      4 - Quit
      : """)

main_dispatch = {"1": send_thankyou,
                 "2": create_report,
                 "3": create_email_file,
                 "4": abort,
                 }

if __name__ == '__main__': 
    menu_selection(main_prompt, main_dispatch)