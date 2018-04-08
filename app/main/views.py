from flask import render_template, redirect, request, url_for
from . import main
from .forms import CardForm
from ..models import Card
from .. import db
import json

dataxx = [{"value": 335, "name": '代码开发'},
{"value": 310, "name": '邮件营销'},
{"value": 274, "name": '联盟广告'},
{"value": 235, "name": '视频广告'},
{"value": 400, "name": '搜索引擎'}]

def card_map(cards):
    card_col = []
    card_row = []
    row = 1
    for card in cards:
        if row % 5 is not 0:
            card_col.append(card)
            row += 1
        if row % 5 is 0:
            card_row.append(card_col)
            card_col=[]
            row += 1
    card_row.append(card_col)
    return card_row

@main.route('/')
def home():
    cards = Card.query.all()
    return render_template('home.html', card_map=card_map(cards))

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

@main.route('/stat')
def stat():
    return render_template('stat.html',
                           task_dis_data=json.dumps(dataxx),
                           plan_acc_data=json.dumps(dataxx),
                           plan_comp_date=json.dumps(dataxx),
                           manpower_data=json.dumps(dataxx))
