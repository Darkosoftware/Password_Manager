import os

def add():
	account = input("Account: ")
	username = input("Username: ")
	password = input("Password: ")
	with open('passwords.txt','a') as f:
		f.write(account +"|" + username + "|" + password[::-1] + "\n")

def view():
	with open('passwords.txt', 'r') as f:
		for line in f.readlines():
			data = line.rstrip()
			account, username, password = data.split("|")
			print("Account: ", account, "Username: ", username, "Password: ", password[::-1])

while True:
	password_ui = input("Input Master Password: ")
	if password_ui == "masterpass":
		mode = input("Would you like to view existing passwords or add new ones (view,add, q to quit)?: ")
		if mode == "q":
			break
		if mode == "view":
			view()
		elif mode == "add":
			add()
		else:
			print("Invalid Entry.")
			continue
	else:
		print("Incorrect Master Password.")
		continue

		
