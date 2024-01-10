from django.db import models

# this for validation
class CourseManger(models.Manager):
    def validate(self, post_data):
        errors = {}
        if len(post_data['name']) < 5:
            errors['name'] = 'Name should be at least 5 charters'
        if len(post_data['description']) < 15:
            errors['description'] = 'Description should be at least 15 charters'
        return errors


class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)
    actions= models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    objects = CourseManger()



    def __str__(self):
        return str({ self.name})
    
    
    