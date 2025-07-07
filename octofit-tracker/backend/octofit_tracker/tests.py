from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='password')
        self.assertEqual(user.email, 'test@example.com')

class TeamTestCase(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', members=[])
        self.assertEqual(team.name, 'Test Team')

class ActivityTestCase(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(name='Test Activity', description='Description')
        self.assertEqual(activity.name, 'Test Activity')

class LeaderboardTestCase(TestCase):
    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', members=[])
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutTestCase(TestCase):
    def test_workout_creation(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='password')
        activity = Activity.objects.create(name='Test Activity', description='Description')
        workout = Workout.objects.create(user=user, activity=activity, duration=60)
        self.assertEqual(workout.duration, 60)
