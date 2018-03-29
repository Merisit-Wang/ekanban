from flask import render_template, redirect, request, url_for
from . import main
from .forms import CardForm

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/card_form', methods=['GET', 'POST'])
def new_card():
    form = CardForm()
    if form.validate_on_submit():
        return redirect(request.args.get('next') or url_for('main.home'))
    return render_template('new_card.html', form=form)