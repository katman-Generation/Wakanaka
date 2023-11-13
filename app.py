from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    """rendering the home page"""
    return(render_template('index.html'))

@app.route("/about")
def about():
    """the url for about page"""
    return(render_template('about.html'))

@app.route("/events")
def events():
    """the url for the events page"""
    return(render_template('events.html'))

@app.route("/inspiration")
def inspiration():
    """the url for the inspiration page"""
    return(render_template('inspiration.html'))

@app.route("/contacts")
def contacts():
    """the url for the contact page"""
    return(render_template('contacts.html'))

@app.route("/board")
def board():
    """the url for the board page"""
    return(render_template('board.html'))

@app.route("/Donations")
def donations():
    """the url for the Donation function"""
    return(render_template('Donations.html'))

if __name__ == "__main__":
    app.run(debug=True)