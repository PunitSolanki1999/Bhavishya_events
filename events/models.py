from django.db import models

# Create your models here.

class Birthday(models.Model):
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
        (bachlor_party,"DJ Night"),
        (welcome_farewell,"Welcome and Farewell Party"),
        (fashion_show,"Fashion Show"),
    )

    party_theme = models.CharField(max_length=100,choices=THEME_CHOICE)
    description = models.CharField(max_length=500,default=None,blank=True)
    party_file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.party_theme

class Decoration(models.Model):
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
    decoration = models.CharField(choices=DECORATION_CHOICE,max_length=100)
    description = models.CharField(max_length=500,default=None,blank=True)
    decoration_file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.decoration

class User_request(models.Model):
    first_name = models.CharField(max_length=100,default=None)
    last_name = models.CharField(max_length=100,default=None)
    mobile_number = models.BigIntegerField()
    gmail = models.EmailField(max_length=250,default=None)
    description = models.CharField(max_length=2000)
    seen = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.first_name