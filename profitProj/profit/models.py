from django.db import models

#Masters
class Category(models.Model):
    name = models.CharField(max_length=51)
    exertion = models.IntegerField(max_length=5)

    def __unicode__(self):
        return self.name

class SubCat(models.Model):
    name = models.CharField(max_length=51)
    cat = models.ForeignKey(Category)
    exertion = models.IntegerField(max_length=5)

    def __unicode__(self):
        return self.cat.name + "->" + self.name

class Goal(models.Model):
    name = models.CharField(max_length=51)
    perCatFitons = models.CharField(max_length=51)

    def __unicode__(self):
        return self.name


#Slaves
class FitUser(models.Model):
    gcm = models.CharField(max_length=512,default=None, null=True, blank=True)
    uuid = models.CharField(max_length=32)
    name = models.CharField(max_length=51, default="")
    height = models.IntegerField(max_length=4,default=None, null=True, blank=True)
    age = models.IntegerField(max_length=3,default=None, null=True, blank=True)
    weight = models.IntegerField(max_length=3,default=None, null=True, blank=True)
    diseases = models.CharField(max_length=1024,default=None, null=True, blank=True)
    BODY_CHOICES = ((0, 'Slim'), (1, 'Fit'), (2, 'Plum'), (3, 'Obese'))
    bodytype = models.IntegerField(choices=BODY_CHOICES,default=None, null=True, blank=True)
    fitons = models.IntegerField(max_length=7,default=None, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(FitUser)
    duration = models.IntegerField(max_length=3)
    subcat = models.ForeignKey(SubCat)
    intensity = models.IntegerField(max_length=2)
    fitons = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.user.name +"'s "+ self.subcat.name

class WeightLog(models.Model):
    user = models.ForeignKey(FitUser)
    date = models.CharField(max_length=12)
    weight = models.IntegerField(max_length=3)

    def __unicode__(self):
        return self.user.name + "'s weight Log"

class Suggestions(models.Model):#Used to send server suggestions to fituser
    goal = models.ForeignKey(Goal)
    subcat = models.ForeignKey(SubCat)
    duration = models.IntegerField(max_length=3)
    intensity = models.IntegerField(max_length=2)

    def __unicode__(self):
        return self.subcat.name + " for " + self.goal.name

class Session(models.Model):
    name = models.CharField(max_length=51)
    user = models.ForeignKey(FitUser)

    def __unicode__(self):
        return self.user.name + "'s Session "+ self.name

class SessionActivity(models.Model):
    session = models.ForeignKey(Session)
    subcat = models.ForeignKey(SubCat)
    duration = models.IntegerField(max_length=4)

    def __unicode__(self):
        return self.session.user.name + "'s Session " + self.session.name + "'s " + self.subcat.name + " Activity"