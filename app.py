from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route("/")
def home(): 
    '''home route'''
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("""SELECT Player.id, Player.Firstname,
                            Player.Lastname, Player.Imagefilename, Team.teamname FROM Player JOIN Team ON Player
                            .Teamid=Team.team_id;""").fetchall()
    connect.close()
    return render_template('home.html', players=players)


@app.route("/allplayers")
def allplayers():
    '''display all players'''
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    #selecting all players from specific id
    players = c.execute("""SELECT Player.id, Player.Firstname,
                            Player.Lastname, Player.Imagefilename, Team.teamname FROM Player JOIN Team ON Player
                            .Teamid=Team.team_id;""").fetchall()
    connect.close()
    return render_template('allplayers.html', players=players)


@app.route('/player/<int:id>')
def player(id):
    '''Joining Team and Position ID on Player'''
    connect = sqlite3.connect('Bball.db')
    c = connect.cursor()
    player = c.execute("""SELECT * FROM Player 
JOIN Team ON Player.Teamid=Team.team_id
Join Position ON Player.Position=Position.ID
WHERE Player.id=? ;""",(id,)).fetchone()
    connect.close()
    return render_template('player.html', player=player)


@app.route("/teams")
def teams():
    '''Display all Teams'''
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    teams = c.execute("""SELECT * FROM Team;""").fetchall()
    connect.close()
    return render_template('teams.html', teams=teams)


@app.route('/teams/<int:id>')
def team(id):
    '''Joining Team ID on Player'''
    connect = sqlite3.connect('Bball.db')
    c = connect.cursor()
    teams = c.execute("""SELECT * FROM Player JOIN Team ON Player.Teamid=Team.team_id
                        WHERE Team.id=?;""",(id,)).fetchone()
    connect.close()
    return render_template('teams.html', teams=teams)

# Error handling for page not found errors 
@app.errorhandler(500)
def page_not_found(error):
    return render_template('error.html', error='Page not found'), 404

# Error handling for 500 (Internal Server) error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error='Internal server error'), 500

# Error handling for unexpected errors 
@app.errorhandler(Exception)
def unexpected_error(error):
    return render_template('error.html', error='Something went wrong'), 500


if __name__ == "__main__":
    app.run(debug=True)