import csv
import os, os.path, time, datetime
import getpass
import pandas as pd
import matplotlib.pyplot as plt
import guide
import encryption

def menu():
    while True:
        os.system('clear')
        guide.open()
        menu = input('Enter command >').lower()
        if menu == '1':#Create the account
            create()       
        elif menu =='2':#Log in the account
            login()            
        elif menu == '3':
            guide.close_app()            
        elif menu == 'h':
            os.system("clear")
            guide.help()
        else:
            print('Code error. Try again or enter [h] for help.')
            time.sleep(1.5)


def create(): # create login info
    print("\nCreat account\n")
    user = input("Username: ").strip()
    pwd = getpass.getpass("Password: ").strip()
    if encryption.encrypt(user, "usr"):
        encryption.encrypt(pwd, "pwd")
    print("\nUser created.")
    time.sleep(1)


def login(): # log in and update data to database
    print("\nLogin Page\n")
    user = input("Username: ").strip()
    pwd = getpass.getpass("Password: ").strip()
    if encryption.decrypt(user, "usr"):
        if encryption.decrypt(pwd, "pwd"):
            print('Welcome back! Proceeding your login......')
            time.sleep(0.5)
            while True:
                os.system('clear')
                print('\nHello,', user)
                select_use = input('Please enter [1] for loging expense or income, [2] for anaylsing the data, [3] for exit\n> ').strip()
                if select_use == '1':
                    log_data(user)
                elif select_use == '2':
                    analysis(user)
                elif select_use == '3':
                    closing = input('Do you want to log out?\n> ').lower()
                    if closing == 'y'or closing =='yes':
                        break
        else:
            print("Password is incorrect or does not exist. Please try again.")
            time.sleep(1)
    else:
        print("Username is incorrect or does not exist. Please try again.")
        time.sleep(1)
        
 # enter data, create 'username'.csv and log data 
def log_data(user):
    os.system('clear')
    print('\nLog your record\n')
    print('*If it is expense, please enter [0] in [income]')
    print('*If it is income, please enter [0] in [expense]\n')
    description = input('Description: ').lower()
    category = input('Category   : ').lower()
    moneyOut = int(input('Expense    : '))
    moneyIn = int(input('Income     : '))
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d')
    
    if os.path.isfile(f'{user}.csv') is True:
        if os.stat(f'{user}.csv').st_size == 0:
            with open(f'{user}.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(['Date', 'Description', 'Category', 'Out', 'In'])
                writer.writerow([now, description, category, moneyOut, moneyIn])
        else:
            with open(f'{user}.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([now, description, category, moneyOut, moneyIn])
        time.sleep(0.5)
        print("Record logged successfully.")
        time.sleep(1)
    else:
        with open(f'{user}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Date', 'Description', 'Category', 'Out', 'In'])
            writer.writerow([now, description, category, moneyOut, moneyIn])

# use padnas to analyse data
def analysis(user):
    exp_inc = pd.read_csv(f'{user}.csv', sep=',')
    exp_inc[['Out', 'In']].sum()
    category_sums = exp_inc.groupby('Category').sum()
    category_sums.index
    ax = category_sums.plot.pie(y='Out', autopct='%1.1f%%', title = 'Expense')
    ax.set_ylabel('')
    ax.legend(bbox_to_anchor=(1,1), borderaxespad=0, title = 'Category')
    plt.show()
    
    input('\nPress [ENTER] key to go back to menu.')


menu()