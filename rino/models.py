from django.db import models

class PlayerStatus(models.Model):
    left_line_index = models.IntegerField()
    middle_line_index = models.IntegerField()
    right_line_index = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return f"PlayerStatus(id={self.id}, position={self.position})"
