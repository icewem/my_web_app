from flask import Flask, render_template, request
from webapp.forms import SearchForm


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def main():
    myFormObject = SearchForm

    if request.method == 'GET':
        return render_template('index.html', page_title="Форма Работает", form=myFormObject)

    return render_template('index.html', page_title="Обошли форму")


if __name__ == "__main__":
    app.run(debug=True)