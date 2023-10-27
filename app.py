from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static') 


@app.route("/")
def home():
    return(render_template('index.html'))

@app.route("/about")
def about():
    return(render_template('about.html'))

@app.route("/mission")
def mission():
    return(render_template('mission.html'))

@app.route("/events")
def events():
    return(render_template('events.html'))

@app.route("/inspiration")
def inspiration():
    return(render_template('inspiration.html'))

@app.route("/contacts")
def contacts():
    return(render_template('contacts.html'))

@app.route("/board")
def board():
    return(render_template('board.html'))

@app.route("/Donations")
def Donations():
    return(render_template('Donations.html'))

if __name__ == "__main__":
    app.run(debug=True)