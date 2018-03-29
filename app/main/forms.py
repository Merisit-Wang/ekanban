from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, DateField, StringField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_admin.form import DatePickerWidget


type_list = [('1', '开发-代码开发'), ('2', '测试-手工测试'), ('3', '故障')]
priority_list = [('1', '必须完成'), ('2', '尽量完成'), ('3', '尝试完成')]
expect_days_list = [('1', '1'), ('2', '2'), ('3', '3'), ('5', '5')]
actual_days_list = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
author_list = [("1", "aaaaaaa"),
               ("2", "bbbbbbb")]

class CardForm(FlaskForm):
    description = TextAreaField('名称', validators=[DataRequired()])
    type = SelectField('类别', choices=type_list)
    priority = SelectField('优先级', choices=priority_list)
    expect_days = SelectField('计划点数', choices=expect_days_list)
    start_time = DateField('开始时间',
                           validators=[DataRequired()],
                           format='%Y-%m-%d',
                           widget=DatePickerWidget())
    end_time = DateField('完成时间',
                         validators=[DataRequired()],
                         format='%Y-%m-%d',
                         widget=DatePickerWidget())
    actual_days = SelectField('实际点数', choices=actual_days_list)
    author = SelectField("完成人", choices=author_list)
    remark = TextAreaField('备注')
    submit = SubmitField('建卡')