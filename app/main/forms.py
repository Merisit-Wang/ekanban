from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired
from flask_admin.form import DatePickerWidget


class CardForm(FlaskForm):
    description = TextAreaField('名称', validators=[DataRequired()])
    type = SelectField('类别', choices=[('1', '开发-代码开发'), ('2', '测试-手工测试'), ('3', '故障')])
    priority = SelectField('优先级', choices=[('1', '必须完成'), ('2', '尽量完成'), ('3', '尝试完成')])
    expect_time = SelectField('计划点数', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('5', '5')])
    start_time = DateField('开始时间', format='%Y-%m-%d', widget=DatePickerWidget())
    submit = SubmitField('建卡')