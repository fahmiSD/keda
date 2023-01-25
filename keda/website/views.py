from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from website.forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, id_blog):
    blog = Blog.objects.get(id=id_blog)
    context = {
        'blog' : blog,
    }
    return render(request, 'blog_detail.html', context)

def team(request):
    Category = Categories.objects.all()
    Teams = Team.objects.all()
    WebAndApps = Team.objects.all().filter(categories_id=1)
    ContentAndMedias = Team.objects.all().filter(categories_id=2)
    BusinessAndDevelopments = Team.objects.all().filter(categories_id=3)
    ProductDesigns = Team.objects.all().filter(categories_id=4)
    context = {
        'categories' : Category,
        'teams' : Teams,
        'webAndApps' : WebAndApps,
        'contentAndMedias' : ContentAndMedias,
        'businessAndDevelopments' : BusinessAndDevelopments,
        'productDesigns' : ProductDesigns,
    }
    return render(request, 'team.html', context)

def career(request):
    careers = Career.objects.all()
    context = {
        'careers' : careers,
    }
    return render(request, 'career.html', context)

def career_detail(request, id_career ):
    if request.POST:
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            career = Career.objects.get(id=id_career)
            form = CandidateForm()
            messages.success(request, "Lamaran Anda telah terkirim!")
            context = {
                'career' : career,
                'form' : form,
            }
            return render(request, 'career_detail.html', context)

        else:
            career = Career.objects.get(id=id_career)
            form = CandidateForm()
            messages.error(request, "Tolong isi kolom dengan benar!")
            context = {
                'career' : career,
                'form' : form,
            }
            return render(request, 'career_detail.html', context)

    else:
        career = Career.objects.get(id=id_career)
        form = CandidateForm()
        context = {
            'career' : career,
            'form' : form,
        }
        return render(request, 'career_detail.html', context)

def consult(request):
    if request.POST:
        form = ConsultForm(request.POST)
        if form.is_valid():
            form.save()
            form = ConsultForm()

            messages.success(request, "Pertanyaan anda telah terkirim!")

            context = {
                'form': form,
            }
            return render(request, 'consult.html', context)

        else:
            form = ConsultForm()

            messages.error(request, "Tolong isi kolom dengan benar!")

            context = {
                'form': form,
            }
            return render(request, 'consult.html', context)

    else:
        form = ConsultForm()
        context = {
            'form': form,
        }
        return render(request, 'consult.html', context)



def subs(request):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriptionForm()

            messages.success(request, "Anda Berhasil Berlangganan!")

            context = {
                'form': form,
            }
            return render(request, 'subs.html', context)

        else:
            messages.error(request, "Format Email yang anda masukkan salah!")
            form = SubscriptionForm()
            context = {
                'form': form,
            }
            return render(request, 'subs.html', context)


    else:
        form = SubscriptionForm()
        context = {
            'form': form,
        }
        return render(request, 'subs.html', context)