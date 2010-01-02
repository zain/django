from django.test import TestCase
from modeltests.orderfield.models import Poll, Choice

class OrderFieldTests(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(question="What's your favorite number?")
        self.c1 = Choice.objects.create(poll=self.poll, choice="One")
        self.c2 = Choice.objects.create(poll=self.poll, choice="Ichi")
        self.c3 = Choice.objects.create(poll=self.poll, choice="Uno")
    
    def tearDown(self):
        self.poll.delete()
        self.c1.delete()
        self.c2.delete()
        self.c3.delete()
    
    def test_sorting(self):
        self.assertEquals(list(Choice.objects.all()), [self.c1, self.c2, self.c3])

        self.c1.order = 3
        self.c1.save()
        self.c2.order = 2
        self.c2.save()
        self.c3.order = 1
        self.c3.save()
        
        self.assertEquals(list(Choice.objects.all()), [self.c3, self.c2, self.c1])