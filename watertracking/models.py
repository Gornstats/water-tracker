from django.db import models


class Water(models.Model):
    """
    Water consumption reported for a single day
    Default: 0
    """
    class Drunk(models.IntegerChoices):
        NONE = 0
        LITTLE = 1
        SOME = 2
        LOTS = 3
        PERFECT = 4
    
    drunk = models.IntegerField(choices=Drunk.choices, default=Drunk.NONE)

