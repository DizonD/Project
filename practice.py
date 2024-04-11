import sqlite3


# First, lastname and team of players
def print_players():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("""SELECT Player.Firstname,
                            Player.Lastname, Team.teamname FROM Player JOIN Team ON Player
                            .Teamid=Team.team_id;""").fetchall()
    # print the header?
    for player in players:
        print(f"{player[0]:<20}{player[1]:<20}{player[2]:<20}")
    connect.close()


# A function to print that players and their id
def print_player_and_id():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("""Select id, Firstname, Lastname FROM Player""").fetchall()
    # print the header?
    for player in players:
        print(f"{player[0]:<20}{player[1]:<20}{player[2]:<20}")
    connect.close()


# A function to print info about one player by their id
def print_player_by_id(id):
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    player = c.execute("""Select Player.Firstname, Player.Lastname, Player.Height, Player.Age, Player.Jerseynumber, Team.teamname, Position.Positionname
                        FROM Player JOIN Team on Player.Teamid=Team.team_id
                        JOIN Position ON Player.Position=Position.ID
                        Where Player.id = ?""", (id,)).fetchone()
    # print the header?
    print("Firstname           Lastname           Height              Age   Jerseynumber Teamname Position")
    print(f"{player[0]:<20}{player[1]:<20}{player[2]:<20}{player[3]:<10}{player[4]:<10}{player[5]:<10}{player[6]:<10}")
    connect.close()


# First, lastname and height of players
def print_height():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("SELECT Firstname, Lastname, Height FROM Player order by Height desc").fetchall()
    # print the header?
    for player in players:
        print(f"{player[0]:<20}{player[1]:<20}{player[2]:<20}")
    connect.close()


# First, lastname and age of players
def print_age():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("SELECT Firstname, Lastname, Age FROM Player").fetchall()
    for player in players:
        print(f"{player[0]:<20}{player[1]:<20}{player[2]:<20}")
    connect.close()


# First, lastname and jerseynumber of players
def print_Jerseynumber():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("SELECT Firstname, Lastname, Jerseynumber FROM Player").fetchall()
    for player in players:
        print(f"{player[0]:<20}{player[1]:<20}{player[2]:<20}")
    connect.close()


# First, lastname and position of players
def print_Position():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("SELECT Player.Firstname, Player.Lastname, Position.Positionname FROM Player JOIN Position ON Player.Position=Position.ID").fetchall()
    for player in players:
        print(f"{player[0]:<20}{player[1]:<20}{player[2]:<20}")
    connect.close()


while True:
    # Topic for code
    print("Welcome to NBA Player Knowledge please follow the instructions below")

    user_input = input("""Enter 1 to see best players in each team:
                       \nEnter 2 to see the height of players:
                        \nEnter 3 to see the age of players:
                        \nEnter 4 to see the jersey number of players
                        \nEnter 5 to see the position of players
                       \nEnter 6 to see a specific player
                       \nEnter 7 to Leave: """)
    # players from different teams name
    if user_input == "1":
        print_players()
    # players from different teams height
    if user_input == "2":
        print_height()
    # players from different teams age
    if user_input == "3":
        print_age()
    # players from different teams jerseynumber
    if user_input == "4":
        print_Jerseynumber()
    # players from different teams position
    if user_input == "5":
        print_Position()
    if user_input == "6":
        # ask user to choose an id
        print_player_and_id()
        id = input("Now that we know a little bit about NBA players, please select a player by their number:")
        # run the query to print out info about that player
        print_player_by_id(id)
    if user_input =="7":
        break
