from django import forms
from .models import Birthday,Decoration,User_request

class Birthday_file_form(forms.ModelForm):
    birthday_party = "birthday party"
    cocktail_party = "cocktail party"
    kitty_party = "kitty party"
    pool_party = "pool party"
    dj_night = "dj night"
    bachlor_party = "bachlor party"
    welcome_farewell = "welcome and farewell party"
    fashion_show = "fashion show"

    THEME_CHOICE = (
        (birthday_party,"Birthday Party"),
        (cocktail_party,"Cocktail Party"),
        (kitty_party,"Kitty Party"),
        (pool_party,"Pool Party"),
        (dj_night,"DJ Night"),
        (bachlor_party,"Bachlor Party"),
        (welcome_farewell,"Welcome and Farewell Party"),
        (fashion_show,"Fashion Show"),
    )


    party_theme = forms.ChoiceField(label='',choices=THEME_CHOICE,widget=forms.Select(attrs={}))
    party_file = forms.FileField(label='',widget=forms.FileInput(attrs={'accept':'image/*,video/*'}))
    description = forms.CharField(label='',widget=forms.TextInput(),required=False)
    class Meta:
        model = Birthday
        fields = [
            'party_theme',
            'party_file',
            'description',
        ]

class Decoration_file(forms.ModelForm):
    balloon_d = "balloon decoration"
    flower_d  = "flower decoration"
    mall_d = "mall decoration"
    showroom_d = "showroom decoration"
    festival_d = "festival theme decoration"
    stage_d = "stage decoration"

    DECORATION_CHOICE = (
        (balloon_d,"Balloon Decoration"),
        (flower_d,"Flower Decoration"),
        (mall_d,"Mall Decoration"),
        (showroom_d,"Showroom Decoration"),
        (festival_d,"Festival Theme Decoration"),
        (stage_d,"Stage Decoration"),
    )

    decoration = forms.ChoiceField(label='',choices=DECORATION_CHOICE,widget=forms.Select(attrs={}))
    decoration_file = forms.FileField(label='',widget=forms.FileInput(attrs={'accept':'image/*,video/*'}))
    description = forms.CharField(label='',widget=forms.TextInput(),required=False)
    class Meta:
        model = Decoration
        fields = [
            'decoration',
            'decoration_file',
            'description',
        ]


class User_request_form(forms.ModelForm):
    first_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'First Name','class':"form-control mb-30",'id':"name"}))
    last_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'last Name','class':"form-control mb-30",'id':"name2"}))
    mobile_number = forms.IntegerField(label='',widget=forms.NumberInput(attrs={'placeholder':'Mobile Number','class':"form-control mb-30",'id':"subject"}))
    gmail = forms.EmailField(label='',max_length=250,widget=forms.EmailInput(attrs={'class':"form-control mb-30", 'id':"email", 'placeholder':"E-mail"}))
    description = forms.CharField(label='',max_length=2000,widget=forms.Textarea(attrs={'class':"form-control mb-30", 'id':"message", 'placeholder':"Your Event Details"}))


    class Meta:
        model = User_request
        fields = [
            'first_name',
            'last_name',
            'gmail',
            'mobile_number',
            'description',
        ]
    
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        count = 0
        number = mobile_number
        while number != 0:
            number = number // 10
            count = count + 1
        if count != 10:
            raise forms.ValidationError("Entered mobile number is not valid")
        return mobile_number
    
    def clean_gmail(self):
        gmail = self.cleaned_data.get('gmail')
        if '@gmail.com' not in gmail:
            raise forms.ValidationError("Entered gmail is not valid")
        return gmail

class Admin_auth_form(forms.Form):
    username = forms.CharField(label='',max_length=100)
    password = forms.CharField(label='',max_length=20,widget=forms.PasswordInput())

    class Meta:
        fields = [
            'username',
            'description',
        ]

