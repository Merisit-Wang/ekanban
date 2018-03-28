from flask import render_template
from . import main
from .forms import CardForm

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/card_form', methods=['GET', 'POST'])
def new_card():
    form = CardForm()
    if form.validate_on_submit():
        return render_template('new_card.html', form=form)
    return render_template('new_card.html', form=form)