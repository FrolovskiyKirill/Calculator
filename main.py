# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first_number = name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u") + name1.lower().count("e") + name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v") + name1.lower().count("e")
second_number = name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u") + name2.lower().count("e") + name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v") + name2.lower().count("e")

love_score = int(str(first_number) + str(second_number))

print(f"Your score is {love_score}")




