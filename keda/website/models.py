from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
import os

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Subscription', 'Categories', 'Position')

# Create your models here.
class Subscription(models.Model):
    email = models.EmailField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Categories(models.Model):
    categories = models.CharField(max_length=200, null=True, default="")

    def __str__(self):
        return self.categories


class Position(models.Model):
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.position


class Team(models.Model):
    employee_name = models.CharField(max_length=300)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    employee_image = models.ImageField(upload_to='employee/')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_name

class Consult(models.Model):
    name = models.CharField(max_length=300)
    business_sector = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=200)
    question = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Blog_tag(models.Model):
    blog_tag_name = models.CharField(max_length=100)
    def __str__(self):
        return self.blog_tag_name

class Blog(models.Model):
    blog_header = models.CharField(max_length=300)
    blog_tag = models.ForeignKey(Blog_tag, on_delete=models.CASCADE)
    image_blog = models.ImageField(upload_to='blog/')
    description = RichTextUploadingField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_header

class Career_tag(models.Model):
    career_tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.career_tag_name

class Career(models.Model):
    career_name = models.CharField(max_length=300)
    career_tag_id = models.ForeignKey(Career_tag, on_delete=models.CASCADE)
    description = RichTextUploadingField()
    deadline = models.DateField(null=True)
    datetime= models.DateTimeField(auto_now_add=True)
    role_responsibility = RichTextUploadingField()
    requirement = RichTextUploadingField()
    plus = RichTextUploadingField()
    benefits = RichTextUploadingField()


    def __str__(self):
        return self.career_name

class Candidate(models.Model):
    candidate_name = models.CharField(max_length=300)
    career_tag_id = models.ForeignKey(Career_tag, on_delete=models.CASCADE)
    whatsapp_number = PhoneNumberField()
    email = models.EmailField(max_length=200)
    cv = models.FileField(upload_to='candidate/')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidate_name
