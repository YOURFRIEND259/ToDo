from django.db import models
import uuid
import bcrypt
# Create your models here.


class Users(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Tasks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title=models.CharField(max_length=255)
    desription=models.TextField()
    created_by=models.ForeignKey(Users,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)

class TaskAssignments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task=models.ForeignKey(Tasks, on_delete=models.CASCADE)
    user=models.ForeignKey(Users, on_delete=models.CASCADE)