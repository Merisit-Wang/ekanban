from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired
from flask_admin.form import DatePickerWidget
from config import type_list, priority_list, expect_days_list, actual_days_list, author_list

class CardForm(FlaskForm):
    description = TextAreaField('名称', validators=[DataRequired()])
    type = SelectField('类别', choices=type_list)
    priority = SelectField('优先级', choices=priority_list)
    expect_day = SelectField('计划点数', choices=expect_days_list)
    start_time = DateField('开始时间',
                           validators=[DataRequired()],
                           format='%Y-%m-%d',
                           widget=DatePickerWidget())
    end_time = DateField('完成时间',
                         validators=[DataRequired()],
                         format='%Y-%m-%d',
                         widget=DatePickerWidget())
    actual_day = SelectField('实际点数', choices=actual_days_list)
    author = SelectField("完成人", choices=author_list)
    remark = TextAreaField('备注')
    submit = SubmitField('建卡')