import time


def open():
    print('''
                    💰 Budget APP 💰
==      Command line interface budget mamangement      ==
==              Multiple users available               ==
==             Enter [h] for app guidance              ==

''')


def help():
    print("""
Command code list
|-------------------------------|
| Create New Account: enter [1] |
| Log in:             enter [2] |
| Close app:          enter [3] |
|-------------------------------|                 
""")
    input('\nPress [ENTER] key to go back to menu.')

    
def close_app():
    closing = input('Do you want to close the budget app?\n> ').lower()
    if closing == 'y'or closing =='yes':
        print('Thanks for using, happy budgeting!')
        time.sleep(1)
        exit()