from flask import Flask, render_template, request
from webapp.forms import SearchForm


app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route("/", methods = ['GET', 'POST'])
def main():
    form = SearchForm()
    if form.validate_on_submit():
        return render_template('index.html', page_title="Good", form=form)
    return render_template('index.html', page_title="Форму обошли", form=form)



if __name__ == "__main__":
    app.run(debug=True)