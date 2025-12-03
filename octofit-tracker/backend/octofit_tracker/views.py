from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Listado de usuarios"})

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Listado de equipos"})

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Listado de actividades"})

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Listado de entrenamientos"})

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({"message": "Leaderboard"})
