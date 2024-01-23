from django import forms
from django.core.exceptions import ValidationError

from women.models import Women


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Категория не выбрана"
        self.fields["is_published"].initial = True

    class Meta:
        model = Women
        fields = "__all__"

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 10:
    #         raise ValidationError("Длина превышает 10 символов")
    #     return title
