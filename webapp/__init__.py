from flask import Flask, render_template
from webapp.forms import SearchForm


app = Flask(__name__)

@app.route("/")
def main():
    page_title = "TEST Search"
    return render_template('index.html', page_title=page_title, form=SearchForm)

if __name__ == "__main__":
    app.run(debug=True)