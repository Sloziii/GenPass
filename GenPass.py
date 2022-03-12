# GenPass

import random
import os
import platform
import string
import time
from pystyle import Colors, Colorate, Box, Center, System
from pathlib import Path
from importlib.resources import path

programVersion = 'dev 1.0.1'
programAuthor = "slozi"

System.Title('GenPass')
System.Size(140, 40)

genpass = '''
  ________             __________                       
 /  _____/  ____   ____\______   \_____    ______ ______
/   \  ____/ __ \ /    \|     ___/\__  \  /  ___//  ___/
\    \_\  \  ___/|   |  \    |     / __ \_\___ \ \___ \ 
 \______  /\___  >___|  /____|    (____  /____  >____  >
        \/     \/     \/               \/     \/     \/                                                         
'''

# string = lower + upper + numbers + symbols
# length = 16 
# password = "".join(random.sample(string, length))

def clear():
  clearConsole = lambda: print('\n' * 150)
  clearConsole()

def actions(string):
  if(string == 'home'):
    action = input(Colorate.Horizontal(Colors.red_to_purple, '--> ', 1))
    possibilities = ['c', 'p', 'exit', 'h']
    if possibilities.__contains__(action):
      if (action == 'c'):
        actions('password_creation')
      else:
        if (action == 'p'):
          print(Colorate.Horizontal(Colors.red_to_purple, 'GenPass path --> /home/' + os.environ.get('USER') + '/Documents/GenPass/', 1))
          actions('home')
        else :
          if (action == 'exit'):
            clear()
          else:
            if (action == 'h'):
              page('home')
    else:
      print(Colorate.Horizontal(Colors.red_to_purple, Box.SimpleCube('Create a new password [c]\nDelete a password [Next version]\nChange a password [Next version]\nList of current passwords [Next version]\nGenPass folder path [p]\nExit GenPass [exit]\nMain page [h]\n'), 1))
      print()
      actions('home')
  elif (string == 'password_creation'):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()."
    password_name = input(Colors.red + 'Give a name to the file wich contains your new password --> ')
    try:
      existing_file = open(password_name + '.txt')
      print(Colors.red + 'ERROR: A file with name ' + password_name + ' already exists !')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.green + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home')
    except IOError:
      try:
        password_length = int(input(Colors.red + 'How long will your password be ? (minimum=6, maximum=72) --> '))
      except ValueError:
        print(Colors.red + 'ERROR: You entered an invalid lenght.')
        print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
        i = 3
        while (i != 0):
          print(Colors.red + '-> ' + str(i) + '...')
          i = i-1
          time.sleep(1)
        page('home')
      if (password_length < 6):
        print(Colors.red + 'ERROR: The minimum password lenght is 6.')
        print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
        i = 3
        while (i != 0):
          print(Colors.red + '-> ' + str(i) + '...')
          i = i-1
          time.sleep(1)
        page('home')
      else :
        if (password_length > 72):
          print(Colors.red + 'ERROR: The maximum password lenght is 72.')
          print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
          i = 3
          while (i != 0):
            print(Colors.green + '-> ' + str(i) + '...')
            i = i-1
            time.sleep(1)
          page('home')
        else:
          result = lower + upper + numbers + symbols
          password = "".join(random.sample(result, password_length))
          print()
          print(Colorate.Horizontal(Colors.red_to_purple, 'SUCCESS ! Your new password is : ' + password, 1))
          storage_file = open(password_name + '.txt', 'w+')
          storage_file.write(password)
          storage_file.close()
          print(Colorate.Horizontal(Colors.red_to_purple, '➞ Stored in /home/' + os.environ.get('USER') + '/Documents/GenPass/' + password_name + '.txt'))
          actions('home')
            

def page(string):
  if (string == 'home'):
    clear()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_purple, genpass, 1)))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, Box.Lines('Welcome to GenPass'), 1))
    print()
    print(Colors.purple + 'GenPass is an completely free and open-source software wich runs in the CLI. It cans create you new passwords and store them in a local folder. Never forget your passwords with GenPass :)')
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, 'Program Author ➟ ' + programAuthor, 1))
    print(Colorate.Horizontal(Colors.red_to_purple, 'Program Version ➟ ' + str(programVersion), 1))
    print(Colorate.Horizontal(Colors.red_to_purple, "Program maintened ➟ Yes", 1))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, 'GitHub ➟ https://github.com/Sloziii/genpass', 1))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, '⤵ Here are the commands you can execute to use GenPass ⤵'))
    print(Colorate.Horizontal(Colors.red_to_purple, Box.SimpleCube('Create a new password [c]\nDelete a password [Next version]\nChange a password [Next version]\nList of current passwords [Next version]\nBackup the GenPass folder to another location [Next version]\nGenPass folder path [p]\nExit GenPass [exit]\nMain page [h]\n'), 1))
    print()
    actions('home')

def installationVerification():
  # For Linux users
  if (platform.system() == 'Linux'):
    documents = '/home/' + os.environ.get('USER') + '/Documents/'
    os.chdir(documents)
    try:
      os.chdir(documents + 'GenPass/')
      page('home')
    except FileNotFoundError:
      os.mkdir('GenPass')
      os.chdir(documents + 'GenPass/')
      page('home')
  # else :
    # if (platform.system() == 'Windows'):
      
  
installationVerification()
# page("home")