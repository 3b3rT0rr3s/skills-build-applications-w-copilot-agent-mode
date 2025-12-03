from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Usuarios
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel'),
            User(email='batman@dc.com', name='Batman', team='DC'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Actividades
        activities = [
            Activity(user='Iron Man', type='Running', duration=30),
            Activity(user='Spider-Man', type='Cycling', duration=45),
            Activity(user='Batman', type='Swimming', duration=60),
            Activity(user='Wonder Woman', type='Yoga', duration=50),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)

        # Workouts
        workouts = [
            Workout(name='Cardio Blast', difficulty='Medium'),
            Workout(name='Strength Training', difficulty='Hard'),
            Workout(name='Yoga Flow', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
