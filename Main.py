import sqlite3

db = sqlite3.connect('Bball.db')
connect = sqlite3.connect("Bball.db")
c = connect.cursor()
players = c.execute("SELECT * FROM Player;").fetchall()
age = c.execute("SELECT Age FROM Player;").fetchall()
name_age = c.execute("SELECT Firstname, Age FROM Player;").fetchall()
Lastname = c.execute("SELECT Lastname FROM Player;").fetchall()

user_input = input("Enter 1 to view all results. 2 For only age of players, enter 3 to see only Firstname and age of players, enter 4 to see last name of players: ")

if user_input == "1":
    print(players)

if user_input == "2":
    print(age)

if user_input == "3":
    print(name_age)

if user_input == "4":
    print(Lastname)
