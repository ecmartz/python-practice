#!/usr/bin/python3.4

# Chapter 6 Project: Insecure Password Locker

PASSWORDS = {'email' : 'emailpassword',
             'blog': 'blogpassword',
             'luggage': '12345'}
           
import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password into clipboard')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for account ' + account + ' copied to clipboard.')
else:
    print('There is no such account, ' + account)