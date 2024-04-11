import sqlite3

db = sqlite3.connect('Bball.db')
connect = sqlite3.connect("Bball.db")
c = connect.cursor()
players = c.execute("SELECT * FROM Player;").fetchall()
age = c.execute("SELECT Age FROM Player;").fetchall()
name = c.execute("SELECT Firstname FROM Player;").fetchall()
Lastname = c.execute("SELECT Lastname FROM Player;").fetchall()
Team = c.execute("Select teamid FROM Player;").fetchall()

user_input = input("Hi please enter 1 to view all results in NBA players. 2 For only age of the players, enter 3 to see only Firstname of players, enter 4 to see last name of players, enter 5 to see Teams of Players: ")


if user_input == "1":
    print(players)

if user_input == "2":
    print(age)

if user_input == "3":
    print(name)

if user_input == "4":
    print(Lastname)

if user_input == "5":
    print(Team)
