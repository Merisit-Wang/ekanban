from flask import render_template, redirect, request, url_for
from . import main
from .forms import CardForm
from ..models import Card
from .. import db

@main.route('/')
def home():
    cards = Card.query.all()
    return render_template('home.html', cards=cards)

@main.route('/card_form', methods=['GET', 'POST'])
def new_card():
    form = CardForm()
    if form.validate_on_submit():
        card = Card(description=form.description.data,
                    type=form.type.data,
                    priority=form.priority.data,
                    expect_day=form.expect_day.data,
                    start_time=form.start_time.data,
                    end_time=form.end_time.data,
                    actual_day=form.actual_day.data,
                    author=form.author.data,
                    remark=form.remark.data)
        db.session.add(card)
        return redirect(request.args.get('next') or url_for('main.home'))
    return render_template('new_card.html', form=form)
