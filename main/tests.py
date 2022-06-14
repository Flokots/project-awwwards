from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project

# Create your tests here.

class ProjectTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.new_user = User(id=1, username='new_user')
        self.new_project = Project(id=1, title='First Project', description='Test Project', link='https://link.com', landing_page='../media/landing_pages/mario-less.png', developer=self.new_user)

    def tearDown(self):
        User.objects.all().delete()
        Project.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    # Testing save method
    def test_save(self):
        self.new_project.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    
    def test_delete(self):
        self.new_project.delete()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)
    

    def test_update(self):
        self.new_project.title = 'New Project'
        self.new_project.save()
        self.assertEqual(self.new_project.title, 'New Project')

    
    def test_search_by_title(self):
        self.project = Project.search_by_title('First Project')

        self.assertEqual(self.new_project.title, 'First Project')