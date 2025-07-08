from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        User.objects.create(email='john.doe@example.com', name='John Doe', password='password123')
        User.objects.create(email='jane.smith@example.com', name='Jane Smith', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com'])
        team2 = Team.objects.create(name='Team Beta', members=[])

        # Create test activities
        activity1 = Activity.objects.create(name='Running', description='Run 5km')
        activity2 = Activity.objects.create(name='Cycling', description='Cycle 10km')

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=150)
        Leaderboard.objects.create(team=team2, score=100)

        # Create test workouts
        user1 = User.objects.get(email='john.doe@example.com')
        user2 = User.objects.get(email='jane.smith@example.com')
        Workout.objects.create(user=user1, activity=activity1, duration=30)
        Workout.objects.create(user=user2, activity=activity2, duration=45)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
