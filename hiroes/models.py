from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class warrior(models.Model):
    name = models.CharField(max_length=31)
    hp = models.IntegerField(default="100")
    ap = models.FloatField(default=10.0)
    dp = models.FloatField(default=0.1)
    hit = models.IntegerField(default = 5) #this is each warrior maximum hit count in a single war.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def attack (w1,w2):
        hp_final = (w1.hit * w1.ap) - w2.hp
        if hp_final >= 0 :
             # it return the winner
            return w1
        else:
            return w2

    def __str__(self):
        return f"{self.name} ({self.user})"
    

class Spell(models.Model):
    name = models.CharField(max_length=31)
    hp_increase = models.IntegerField()
    ap_increase = models.FloatField()
    dp_increase = models.FloatField()

    def cast_spell(w, spell):
        w.dp += Spell.dp_increase
        w.hp += Spell.hp_increase
        w.ap += Spell.ap_increase


    def __str__(self):
        return f"{self.name}"



