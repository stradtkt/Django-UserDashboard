from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models


class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be 2 or more characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be 2 or more characters"
        if len(postData['first_name']) > 30:
            errors['first_name'] = "First name needs to be less then 30 characters"
        if len(postData['last_name']) > 30:
            errors['last_name'] = "Last name needs to be less then 30 characters"
        if not postData['first_name'].isalpha():
            errors['first_name'] = "First name needs to be only letters"
        if not postData['last_name'].isalpha():
            errors['last_name'] = "Last name needs to be only letters"

        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

                
        try:
            postData['username']
        except ValidationError:
            errors['username'] = "Your username is not valid"
        else:
            if User.objects.filter(username=postData['username']):
                errors['username'] = "This username already exists"


        if len(postData['password']) < 4:
            errors['password'] = "Please enter a longer password, needs to be four or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class MessageManager(models.Manager):
    def validate_message(self, postData):
        errors = {}
        if len(postData['body']) < 10:
            errors['body'] = "You need to have at least 10 characters in your message"
        return errors

class Message(models.Model):
    user_to = models.ForeignKey(User, related_name="to", on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name="messenger", on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class CommentManager(models.Manager):
    def validate_comment(self, postData):
        errors = {}
        if len(postData['body']) < 3:
            errors['body'] = "You need to have at least 3 characters in your message"
        return errors

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="commentor", on_delete=models.DO_NOTHING)
    message = models.ForeignKey(Message, related_name="message", on_delete=models.DO_NOTHING)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()