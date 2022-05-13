from django.db import models


# Create your models here.
class User(models.Model):
    # id
    name = models.CharField(max_length=50, default='Danil')


class Message(models.Model):
    # id
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    # user_id = models.IntegerField()
    message = models.TextField()
    status = models.CharField(max_length=10, default='review')


class MessageConfirm(models.Model):
    # id
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE)
    success = models.BooleanField(default=None, null=True)

# update Message
# set status = case when MC.success = True then 'blocked' else 'correct' end
# from MessageConfirm as MC
# where Message.id = MS.message_id
