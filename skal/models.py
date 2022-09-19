from django.db import models

class User(models.Model):

    class Meta:

        db_table = 'users'

    email = models.EmailField(unique=True, db_index=True)

    def __str__(self):
        return self.title