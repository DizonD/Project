from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route("/")
def hello_world(): 
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("""SELECT Player.id, Player.Firstname,
                            Player.Lastname, Player.Imagefilename, Team.teamname FROM Player JOIN Team ON Player
                            .Teamid=Team.team_id;""").fetchall()
    connect.close()
    return render_template('home.html', players=players)


@app.route("/allplayers")
def allplayers():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    players = c.execute("""SELECT Player.id, Player.Firstname,
                            Player.Lastname, Player.Imagefilename, Team.teamname FROM Player JOIN Team ON Player
                            .Teamid=Team.team_id;""").fetchall()
    connect.close()
    return render_template('allplayers.html', players=players)


@app.route('/player/<int:id>')
def player(id):
    connect = sqlite3.connect('Bball.db')
    c = connect.cursor()
    player = c.execute("""SELECT * FROM Player JOIN Team ON Player.Teamid=Team.team_id
                        WHERE Player.id=?;""",(id,)).fetchone()
    connect.close()
    return render_template('player.html', player=player)


@app.route("/teams")
def teams():
    connect = sqlite3.connect("Bball.db")
    c = connect.cursor()
    teams = c.execute("""SELECT * FROM Team;""").fetchall()
    connect.close()
    return render_template('teams.html', teams=teams)


if __name__ == "__main__":
    app.run(debug=True)