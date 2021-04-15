from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TeamSerializer, ResultSerializer
from .models import Team, Result


# Create your views here.

class PostTeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        team = Team.objects.all()
        return team

    def create(self, request, *args, **kwargs):
        post_data = request.data
        new_team = Team.objects.create(
            team=post_data["team"],
            team_log=post_data["team_log"]
        )
        new_team.save()
        serializer = TeamSerializer(new_team)
        return Response(serializer.data)


class PostTeamResultsViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSerializer

    def get_queryset(self):
        team = Team.objects.all()
        return team

    def create(self, request, *args, **kwargs):
        post_data = request.data
        if post_data["homeTeam"] > post_data["awayTeam"]:
            new_team = Result.objects.create(
                win=,
                team_log=post_data["team_log"]
            )
            new_team.save()
            serializer = TeamSerializer(new_team)


        return Response(serializer.data)


class PostsRatesViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        rates = Team.objects.all()
        return rates
