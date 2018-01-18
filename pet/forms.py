from django import forms


class PetForm(forms.Form):
    title = forms.CharField(label='애칭', max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)


