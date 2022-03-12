# GenPass
import random
import os
import platform
import string
import time
import shutil
from typing import IO
from pystyle import Colors, Colorate, Box, Center, System
from pathlib import Path
from importlib.resources import path

programVersion = 'dev 1.0.2'
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

def clear():
  clearConsole = lambda: print('\n' * 150)
  clearConsole()

def actions(string):
  if(string == 'home'):
    action = input(Colorate.Horizontal(Colors.red_to_purple, '--> ', 1))
    possibilities = ['pswd create', 'path', 'exit', 'clear', 'pswd delete', 'pswd modify', 'pswd list', 'backup create', 'backup load', 'backup reload', 'backup delete']
    if possibilities.__contains__(action):
      if (action == 'pswd create'):
        actions('password_creation')
      else:
        if (action == 'path'):
          print(Colorate.Horizontal(Colors.red_to_purple, 'GenPass path --> /home/' + os.environ.get('USER') + '/Documents/GenPass/', 1))
          actions('home')
        else :
          if (action == 'exit'):
            clear()
          else:
            if (action == 'clear'):
              page('home')
            else:
              if (action == 'pswd delete'):
                actions('password_removal')
              else:
                if (action == 'pswd modify'):
                  actions('password_changing') 
                else:
                  if (action == 'pswd list'):
                    list = os.listdir('/home/' + os.environ.get('USER') + "/Documents/GenPass/")
                    listContent = len(list)
                    print(Colorate.Horizontal(Colors.red_to_purple, Box.SimpleCube('Total of ' + str(listContent) + ' password(s)\n\n' + '\n'.join(map(str, list))), 1))
                    actions('home')
                  else:
                    if (action == 'backup create'):
                      actions('backup_current_directory')
                    else:
                      if (action == 'backup load'):
                        actions('load_existing_backup')
                      else:
                        if (action == 'backup reload'):
                          actions('reload_existing_backup')
                        else:
                          if (action == 'backup delete'):
                            actions('delete_existing_backup')
    else:
      print(Colorate.Horizontal(Colors.red_to_purple, Box.SimpleCube('➔ Create a new password [pswd create]\n➔ Delete a password [pswd delete]\n➔ Change a password [pswd modify]\n➔ List of current passwords [pswd list]\n➔ Backup the GenPass folder to another location [backup create]\n➔ Load a GenPass backup folder [backup load]\n➔ Delete a GenPass backup folder [backup delete]\n➔ Reload a GenPass backup folder [backup reload]\n➔ GenPass folder path [path]\n➔ Exit GenPass [exit]\n➔ Clear [clear]\n'), 1))
      print()
      actions('home')
  elif (string == 'password_creation'):

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()."

    password_name = input(Colorate.Horizontal(Colors.red_to_purple, 'Give a name to the file wich contains your new password --> ', 1))
    try:
      existing_file = open(password_name + '.txt')
      print(Colors.red + 'ERROR: A file with name ' + password_name + ' already exists !')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.red + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home')
    except IOError:
      try:
        password_length = int(input(Colorate.Horizontal(Colors.red_to_purple, 'How long will your password be ? (min=6 : max=72) --> ', 1)))
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
            print(Colors.red + '-> ' + str(i) + '...')
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

  elif (string == 'password_removal'):
    password_name = input(Colorate.Horizontal(Colors.red_to_purple, 'Give the name of the password to remove --> ', 1))
    try:
      existing_file = open(password_name + '.txt')
      existing_file.close
      confirmation = input(Colorate.Horizontal(Colors.red_to_purple, 'Are you sure that you want to definitively remove the password file for ' + password_name + ' ? (y/N) --> ', 1))
      confirmation_possibilities = ['y', 'N']
      if (confirmation_possibilities.__contains__(confirmation)):
        if (confirmation == "y"):
          os.remove(password_name + '.txt')
          print(Colorate.Horizontal(Colors.red_to_purple, 'SUCCESS ! The password for ' + password_name + ' has been deleted', 1))
          actions('home')
        elif (confirmation == "N"):
          print(Colorate.Horizontal(Colors.red_to_purple, 'The password file for ' + password_name + ' has not been deleted.', 1))
          actions('home')
      else:
        print(Colorate.Horizontal(Colors.red_to_purple, 'The password file for ' + password_name + ' has not been deleted.', 1))
        actions('home')
    except IOError:
      print(Colors.red + 'ERROR: The target file to delete does not exist.')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.red + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home')

  elif (string == 'password_changing'):

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()."

    password_name = input(Colorate.Horizontal(Colors.red_to_purple, 'Give the name of the password that you want to change --> ', 1))

    try:
      existing_file = open(password_name + '.txt')
      existing_file.close()
      confirmation = input(Colorate.Horizontal(Colors.red_to_purple, 'Are you sure that you want to change the password for ' + password_name + ' ? (y/N) --> ', 1))
      confirmation_possibilities = ['y', 'N']
      if (confirmation_possibilities.__contains__(confirmation)):
        if (confirmation == "y"):
          try:
            password_length = int(input(Colorate.Horizontal(Colors.red_to_purple, 'How long will your password be ? (min=6 : max=72) --> ', 1)))
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
                print(Colors.red + '-> ' + str(i) + '...')
                i = i-1
                time.sleep(1)
              page('home')
            else:
              result = lower + upper + numbers + symbols
              password = "".join(random.sample(result, password_length))
              os.remove(password_name + '.txt')
              storage_file = open(password_name + '.txt', "w+")
              storage_file.write(password)
              storage_file.close()
              print(Colorate.Horizontal(Colors.red_to_purple, 'SUCCESS ! The password for ' + password_name + ' has been changed to ' + password, 1))
              actions('home')
        elif (confirmation == "N"):
          print(Colorate.Horizontal(Colors.red_to_purple, 'The password file for ' + password_name + ' has not been changed.', 1))
          actions('home')
      else:
        print(Colorate.Horizontal(Colors.red_to_purple, 'The password file for ' + password_name + ' has not been changed.', 1))
        actions('home')
    except IOError:
      print(Colors.red + 'ERROR: The target file to change does not exist.')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.red + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home')

  elif (string == 'backup_current_directory'):
    backup_dir = input(Colorate.Horizontal(Colors.red_to_purple, 'Write here the path where the GenPass folder will be backuped --> ', 1))
    try:
      os.chdir(backup_dir)
      try:
        os.chdir(backup_dir + 'GenPass/')
        print(Colors.red + 'ERROR: The target directory already have a backup folder.')
        print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
        i = 3
        while (i != 0):
          print(Colors.red + '-> ' + str(i) + '...')
          i = i-1
          time.sleep(1)
        page('home')
      except FileNotFoundError: 
        source_dir = '/home/' + os.environ.get('USER') + '/Documents/GenPass/'
        shutil.copytree(source_dir, backup_dir + "GenPass/")
        print(Colorate.Horizontal(Colors.red_to_purple, 'SUCCESS ! ' + str(len(os.listdir(source_dir))) + ' passwords have been backuped to ' + backup_dir + 'GenPass/', 1))
        os.chdir(source_dir)
        actions('home')
    except FileNotFoundError:
      print(Colors.red + 'ERROR: The target directory does not exist.')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.red + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home')

  elif (string == 'load_existing_backup'):
    current_backup_dir = input(Colorate.Horizontal(Colors.red_to_purple, 'Write here the path where the GenPass folder backup is --> ', 1))
    try:
      os.chdir(current_backup_dir + 'GenPass/')
      default_genpass_path = '/home/' + os.environ.get('USER') + '/Documents/GenPass/'
      shutil.rmtree(default_genpass_path)
      shutil.copytree(current_backup_dir + 'GenPass/', default_genpass_path)
      os.chdir(default_genpass_path)
      print(Colorate.Horizontal(Colors.red_to_purple, 'SUCCESS ! ' + str(len(os.listdir(current_backup_dir + 'GenPass/'))) + ' passwords have been loaded to ' + default_genpass_path, 1))
      actions('home')
    except FileNotFoundError:
      print(Colors.red + 'ERROR: No backup folder in the target directory.')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.red + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home')

  elif (string == 'reload_existing_backup'):
    current_backup_dir = input(Colorate.Horizontal(Colors.red_to_purple, 'Write here the path where the GenPass folder backup is --> ', 1))
    try:
      os.chdir(current_backup_dir + 'GenPass/')
      default_genpass_path = '/home/' + os.environ.get('USER') + '/Documents/GenPass/'
      shutil.rmtree(current_backup_dir + 'GenPass/')
      shutil.copytree(default_genpass_path, current_backup_dir + 'GenPass/')
      os.chdir(default_genpass_path)
      print(Colorate.Horizontal(Colors.red_to_purple, 'SUCCESS ! ' + str(len(os.listdir(current_backup_dir + 'GenPass/'))) + ' passwords have been reloaded to ' + current_backup_dir + 'GenPass/', 1))
      actions('home')
    except FileNotFoundError:
      print(Colors.red + 'ERROR: No backup folder in the target directory.')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.red + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home')
  
  elif (string == 'delete_existing_backup'):
    current_backup_dir = input(Colorate.Horizontal(Colors.red_to_purple, 'Write here the path where the GenPass folder backup is --> ', 1))
    try:
      os.chdir(current_backup_dir + 'GenPass/')
      confirmation = input(Colorate.Horizontal(Colors.red_to_purple, 'Are you sure that you want to delete your ' + current_backup_dir + 'GenPass/ backup ? (y/N) --> ', 1))
      confirmation_possibilities = ['y', 'N']
      if (confirmation_possibilities.__contains__(confirmation)):
        if (confirmation == 'y'):
          shutil.rmtree(current_backup_dir + 'GenPass/')
          print(Colorate.Horizontal(Colors.red_to_purple, 'SUCCESS ! Your ' + current_backup_dir + 'GenPass/ has been deleted.', 1))
          actions('home')
        elif (confirmation == 'N'):
          print(Colorate.Horizontal(Colors.red_to_purple, 'Your ' + current_backup_dir + 'GenPass/ has not been deleted.', 1))
          actions('home')
      else:
        print(Colorate.Horizontal(Colors.red_to_purple, 'Your ' + current_backup_dir + 'GenPass/ has not been deleted.', 1))
        actions('home')
    except FileNotFoundError:
      print(Colors.red + 'ERROR: No backup folder in the target directory.')
      print(Colorate.Horizontal(Colors.red_to_purple, 'Back to program home page...', 1))
      i = 3
      while (i != 0):
        print(Colors.red + '-> ' + str(i) + '...')
        i = i-1
        time.sleep(1)
      page('home') 

def page(string):
  if (string == 'home'):
    clear()
    print(Center.XCenter(Colorate.Horizontal(Colors.red_to_purple, genpass, 1)))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, Box.Lines('Welcome to GenPass'), 1))
    print()
    print(Colors.purple + 'GenPass is an completely free and open-source (you can see, modify all the code) software wich runs in the CLI. It can create you new passwords and store them in a local folder. Never forget your passwords with GenPass :)')
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, 'Program Author ➟ ' + programAuthor, 1))
    print(Colorate.Horizontal(Colors.red_to_purple, 'Program Version ➟ ' + str(programVersion), 1))
    print(Colorate.Horizontal(Colors.red_to_purple, "Program maintened ➟ Yes", 1))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, 'GitHub ➟ https://github.com/Sloziii/GenPass/blob/dev1.0.1/GenPass.py', 1))
    print()
    print(Colorate.Horizontal(Colors.red_to_purple, '⤵ Here are the commands that you can execute to use GenPass ⤵'))
    print(Colorate.Horizontal(Colors.red_to_purple, Box.SimpleCube('➔ Create a new password [pswd create]\n➔ Delete a password [pswd delete]\n➔ Change a password [pswd modify]\n➔ List of current passwords [pswd list]\n➔ Backup the GenPass folder to another location [backup create]\n➔ Load a GenPass backup folder [backup load]\n➔ Delete a GenPass backup folder [backup delete]\n➔ Reload a GenPass backup folder [backup reload]\n➔ GenPass folder path [path]\n➔ Exit GenPass [exit]\n➔ Clear [clear]\n'), 1))
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
  # For Windows users
  else : 
    if (platform.system() == 'Windows'):
      documents = 'C:/'
      # For MacOS users
    #else :

    
      
  
installationVerification()