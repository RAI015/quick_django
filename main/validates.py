from datetime import date

from django import forms


def compare_today(value):
    if date.today() < value:
        raise forms.ValidationError('刊行日は今日以前の日付で入力してください。')
