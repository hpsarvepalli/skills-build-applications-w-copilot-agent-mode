from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for teams, activities, leaderboard, and workouts
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='tony', email='tony@marvel.com', password='ironman', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@marvel.com', password='cap', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@dc.com', password='batman', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@dc.com', password='superman', team=dc)

        # Create activities
        app_models.Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        app_models.Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        app_models.Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        app_models.Activity.objects.create(user=clark, type='run', duration=50, distance=10)

        # Create workouts
        app_models.Workout.objects.create(user=tony, description='Chest day', duration=40)
        app_models.Workout.objects.create(user=steve, description='Leg day', duration=50)
        app_models.Workout.objects.create(user=bruce, description='Cardio', duration=30)
        app_models.Workout.objects.create(user=clark, description='Strength', duration=60)

        # Create leaderboard
        app_models.Leaderboard.objects.create(user=tony, points=100)
        app_models.Leaderboard.objects.create(user=steve, points=90)
        app_models.Leaderboard.objects.create(user=bruce, points=80)
        app_models.Leaderboard.objects.create(user=clark, points=95)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
