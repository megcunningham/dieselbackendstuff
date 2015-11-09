from django.test import TestCase
form workouts.models import Site

class SiteTest(TestCase):
    #This is the fixture:
    #-   fields: {content: lots of stuff, query: test, title:
     test, url: 'http://google.com'}
    #model: workouts.site
    #pk: 1
    fixtures = ['workouts']

    def TestFluffyAnimals(self):
        s = Site.objects.get(pk=1)
        self.assertEquals(s.query, 'test')
        s.query = 'who cares'
        s.save()