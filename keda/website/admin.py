from django.contrib import admin
from website.models import Subscription,Color, Position, Team, Consult, Blog, Blog_tag, Career_tag, Career, Candidate, Categories

#config admin page
class SubsAdmin(admin.ModelAdmin):
    list_display = ['email']
admin.site.register(Subscription, SubsAdmin)

admin.site.register(Color)


class PositionAdmin(admin.ModelAdmin):
    list_display = ['position']
admin.site.register(Position, PositionAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['categories']
admin.site.register(Categories, CategoriesAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'categories', 'position_id', 'datetime']
admin.site.register(Team, TeamAdmin)


class ConsultAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_sector', 'phone_number', 'email', 'datetime']
admin.site.register(Consult, ConsultAdmin)


class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['blog_tag_name']
admin.site.register(Blog_tag, BlogTagAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_header','blog_tag','image_blog','datetime']
admin.site.register(Blog, BlogAdmin)


class CareerTagAdmin(admin.ModelAdmin):
    list_display = ['career_tag_name']
admin.site.register(Career_tag,CareerTagAdmin)


class CareerAdmin(admin.ModelAdmin):
    list_display = ['career_name', 'career_tag_id', 'deadline', 'datetime']
admin.site.register(Career, CareerAdmin)


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['candidate_name', 'career_tag_id', 'email', 'datetime']
admin.site.register(Candidate, CandidateAdmin)
