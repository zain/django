from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    order = models.OrderField()
    
    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.choice
