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

def scramble():
	pass

def descramble():
	pass

def set_save_masterpassword():
	global master_password
	filesize = os.stat('masterpassword.txt').st_size
	with open('masterpassword.txt', 'r') as f:
		master_password = f.readline()
	if filesize == 0:
		master_password = input("Set master password for the Password Manager: ")
		with open('masterpassword.txt','a') as f:
			f.write(master_password[::-1])

while True:
    set_save_masterpassword()
    password_ui = input("Input Master Password: ")
    if password_ui == master_password[::-1]:
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
