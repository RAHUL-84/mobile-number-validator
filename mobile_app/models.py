from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    mobile_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^9\d{9}$',  # number 9 se start hona chahiye aur total 10 digits
                message="Mobile number must start with 9 and have 10 digits."
            )
        ]
    )

    def __str__(self):
        return self.mobile_number
