from django import forms


class CodePracticeForm(forms.Form):
    code = forms.CharField(
        label="コード入力",
        widget=forms.Textarea(
            attrs={
                "class": "code-editor",
                "spellcheck": "false",
                "rows": 20,
            }
        ),
    )
