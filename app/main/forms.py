from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, DateField, StringField
from wtforms.validators import DataRequired, Length
from flask_admin.form import DatePickerWidget
from config import type_list, priority_list, expect_days_list, actual_days_list

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
    author = StringField("完成人", validators=[DataRequired()])
    remark = TextAreaField('备注')
    submit = SubmitField('建卡')

class StatForm(FlaskForm):
    from_date = DateField('迭代开始时间',
                          validators=[DataRequired()],
                          format='%Y-%m-%d',
                          widget=DatePickerWidget())
    to_date = DateField('迭代结束时间',
                          validators=[DataRequired()],
                          format='%Y-%m-%d',
                          widget=DatePickerWidget())
    manpower = StringField('总人力', validators=[DataRequired(), Length(3, 3)])
    submit = SubmitField('统计')