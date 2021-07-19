from hash_maker import password
import subprocess
from database_manager import store_passwords, find_users, find_password
from sys import platform

def menu():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Exit')
    print('-' * 30)
    return input(': ')

def create():
   app_name = input('Please provide the name of the site or app you want to generate a password for: ')
   plaintext = input('Please provide a simple password for this site: ')
   passw = password(plaintext, app_name, 12)
   if platform == 'win32':
       subprocess.run('clip.exe', universal_newlines=True, input=passw,shell=True)
   elif platform.startswith('linux'):
       subprocess.run('xclip', universal_newlines=True, input=passw,shell=True)
   else:
       print('Sorry, OS still not compatible')
       exit()
   print('-' * 30,'\n','Your password has now been created and copied to your clipboard','\n','-' * 30)
   user_email = input('Please provide a user email for this app or site: ')
   username = input('Please provide a username for this app or site (if applicable): ')

   if username == None:
       username = ''
   url = input('Please provide the url to the site that you are creating the password for: ')
   store_passwords(passw, user_email, username, url, app_name)

def find():
    app_name = input('Please provide the name of the site or app you want to find the password: ')
    find_password(app_name)

def find_accounts():
     user_email = input('Please provide the email that you want to find accounts for: ') 
     find_users(user_email)
