from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=30, distance=5)
        self.workout = Workout.objects.create(user=self.user, description='Test Workout', duration=45)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')
    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')
    def test_workout(self):
        self.assertEqual(self.workout.description, 'Test Workout')
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
