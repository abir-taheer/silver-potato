#Verifies  username/password combination. Reads from file accounts.csv.
import csv

def signIn(username, password):
    accounts = csv.reader( open('accounts.csv', 'r') )
    for row in accounts:
        if row[0] == username:
            if row[1] == password:
                return True
    return False
