from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField('Текст поиска', validators=[DataRequired()])
    submit = SubmitField('Искать')