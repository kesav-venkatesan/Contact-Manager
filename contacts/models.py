from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator



class User(AbstractUser):
    pass

class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    file=models.FileField(upload_to='contact-docs/',validators=[FileExtensionValidator(['pdf','doc','txt','docx'])],blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="contacts")
    
    class Meta:
        unique_together=('name','email')
    def __str__(self):
        return f'{self.name} {self.email}'
    
