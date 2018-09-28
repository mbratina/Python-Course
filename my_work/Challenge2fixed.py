#!/usr/bin/en python

# Python for Network Engineers Problem Script
# Revision May 22 2018

# Copyright (C) 2013 Matt Oswalt (http://keepingitclassless.net/)
# Obviously humorous and meant to be taken as such.


# <<<<<<< HEAD

import webbrowser


class CCIE:
    """
    A class to describe a CCIE-certified engineer
    """
    def __init__(self):
        self.name = ''
        self.salary = ''
        self.iq = ''
        self.homeless = True

    def setname(self, name=''):
        self.name = name


thisCCIE = CCIE()
thisCCIE.setname(raw_input('Please enter your name.'))

answer = raw_input("Can you use a GUI? (yes/no/huh)")

if answer == "no":

    print "That's awkward."
    thisCCIE.homeless = True

elif answer == 'yes':
    print "Congratulations! You're a networking expert!"
    thisCCIE.salary = 1000000000
    thisCCIE.iq = 42

else:
    print "I see that you are in management. Go fire some CCIEs or something."
# =======


answer = raw_input("Can you use a GUI? (yes/no/huh/hello)")

if answer == 'no':
    webbrowser.open_new('http://www.opendaylight.org/')
elif answer == 'yes':
    print "Congratulations! You're a networking expert!"
elif answer == "hello":
    print "I see that you are in management. Go fire some CCIEs or something."
# >>>>>>> a2cf24d6c37bf7143e5e2766a0470322ca56bb99
else:
    print "What's a goooey ?"
    thisCCIE.homeless = True
