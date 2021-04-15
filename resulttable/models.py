from django.db import models


# Create your models here.
# team model starting with this
class Team(models.Model):
    team = models.CharField(max_length=20)
    team_log = models.CharField(max_length=20, default="no logo")

    def __str__(self):
        return self.team


# result table for showing results
class Result(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    match_play = models.PositiveIntegerField(default=0)
    win = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)
    goal_scored = models.PositiveIntegerField(default=0)
    goal_concede = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.match_play
