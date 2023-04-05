master_pwd = input("What is the master password? ")

def view():
    with open("Passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:", passw)
        
            
        

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("Passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")
        
        
while True:
    mode = input("would you like to add a anew password or view exisitng ones? (view, add), press q to quite ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue