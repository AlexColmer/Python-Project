name = input("Type your name ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river and you can walk around it or swim across? Type walk to walk or swim to swim ")
    if answer == "swim":
        print("You swim across and were eaten by an aligator. ")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game.")
    else:
        print("not a valid option")


elif answer == "right":
    answer = input("You come to a bridge it looks wobbly do you want to cross it or head back, (cross/back) ")
     
    if answer == "back":
        answer = input("You come across an inn on the dirt road. Do you spend the night or Keep on going down the path? ")

        if answer == "spend the night":
            print("you have a rested night but find youself awoken by strange creatures ")
        elif answer == "keep going down the path":
            print("you meet a starnger who aproaches you.")       

 