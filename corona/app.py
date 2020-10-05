from flask import Flask, render_template, flash, request
import pandas as pd
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

df = pd.read_csv('data1.csv')
try:
    row = df[df['District'] == 'Delhi'].index[0]
except:
    print("now city found")

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

class ReusableForm(FlaskForm)
    name = StringField('name', validators=[validators.required()])
    submit = SubmitField('Enter')

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(    )

    if form.is_submitted():
        city = request.form['name'].capitalize()
        try:
            row = df[df['District'] == city].index[0]
            print(city)
            cases = df.at[row, 'count(district)']
            print(cases)
        except:
            cases = -1
            print("cases are", cases)
        flash("cases are " +  str(cases))

	 return render_template('data.html', form=form)

if __name__ == "__main__":
    app.run()
