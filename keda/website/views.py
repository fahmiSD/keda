from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from website.forms import *

# Create your views here.
def index(request):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriptionForm()
            message = "berhasil"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'index.html', context)

        else:
            form = SubscriptionForm()
            message = "error"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'index.html', context)

    else:
        form = SubscriptionForm()
        context = {
            'form' : form,
        }
        return render(request, 'index.html', context)
    

def solution(request):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriptionForm()
            message = "berhasil"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'solution.html', context)

        else:
            form = SubscriptionForm()
            message = "error"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'solution.html', context)

    else:
        form = SubscriptionForm()
        context = {
            'form' : form,
        }
        return render(request, 'solution.html', context)

def aboutCareer(request):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            careers = Career.objects.all()
            form.save()
            form = SubscriptionForm()
            message = "berhasil"
            context = {
                'form' : form,
                'message' : message,
                'careers' : careers
            }
            return render(request, 'aboutCareer.html', context)

        else:
            form = SubscriptionForm()
            message = "error"
            careers = Career.objects.all()
            context = {
                'form' : form,
                'message' : message,
                'careers' : careers
            }
            return render(request, 'aboutCareer.html', context)

    else:
        form = SubscriptionForm()
        careers = Career.objects.raw('''SELECT website_career_tag.career_tag_name,website_color.hex_code, website_career.* 
from website_career INNER JOIN website_career_tag on website_career_tag.id = website_career.career_tag_id_id 
LEFT JOIN website_color on  website_career_tag.color_id_id = website_color.ID''')
        # tag_colors = Career_tag.objects.all()
        # careers = Career.objects.all()
        context = {
            'form' : form,
            'careers' : careers,
            # 'tag_colors' : tag_colors,
        }
        return render(request, 'aboutCareer.html', context)

def detailCareer(request, id_career):
    if request.method == 'POST':
        if request.POST.get("form_type") == 'form_candidate':
            form_candidate = CandidateForm(request.POST, request.FILES)
            if form_candidate.is_valid():
                form_candidate.save()
                career = Career.objects.get(id=id_career)
                form_candidate = CandidateForm()
                form_subs = SubscriptionForm()
                context = {
                    'form_candidate' : form_candidate,
                    'form_subs' : form_subs,
                    'career' : career,
                    'success' : 'Lamaran Anda telah terkirim!'
                }
                return render(request, 'detailCareer.html', context)

            else:
                career = Career.objects.get(id=id_career)
                form_candidate = CandidateForm(request.POST)
                form_subs = SubscriptionForm()
                context = {
                    'form_candidate' : form_candidate,
                    'form_subs' : form_subs,
                    'career' : career,
                    'errors' : form_candidate.errors,
                }
                
                return render(request, 'detailCareer.html', context)
            
        
        elif request.POST.get("form_type") == 'form_subs':
            form_subs = SubscriptionForm(request.POST)
            if form_subs.is_valid():
                form_subs.save()
                career = Career.objects.get(id=id_career)
                form_candidate = CandidateForm()
                form_subs = SubscriptionForm()
                message = "berhasil"
                context = {
                    'form_candidate' : form_candidate,
                    'form_subs' : form_subs,
                    'message' : message,
                    'career' : career,
                }
                return render(request, 'detailCareer.html', context)

            else:
                career = Career.objects.get(id=id_career)
                form_candidate = CandidateForm()
                form_subs = SubscriptionForm()
                message = "error"
                context = {
                    'form_candidate' : form_candidate,
                    'form_subs' : form_subs,
                    'message' : message,
                    'career' : career,
                }
                return render(request, 'detailCareer.html', context)
        
    else:
        career = Career.objects.get(id=id_career)
        form_candidate = CandidateForm()
        form_subs = SubscriptionForm()
        context = {
            'career' : career,
            'form_candidate' : form_candidate,
            'form_subs' : form_subs,
        }
        return render(request, 'detailCareer.html', context)

def detailBlog(request, id_blog):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriptionForm()
            blog = Blog.objects.get(id=id_blog)
            related_blogs = Blog.objects.all().exclude(id=id_blog).order_by("?")[:4]
            message = 'berhasil'
            context = {
                'blog' : blog,
                'form' : form,
                'message' : message,
                'related_blogs' : related_blogs,
            }
            return render(request, 'detailBlog.html', context)

        else:
            form = SubscriptionForm()
            blog = Blog.objects.get(id=id_blog)
            related_blogs = Blog.objects.all().exclude(id=id_blog).order_by("?")[:4]
            message = 'error'
            context = {
                'blog' : blog,
                'form' : form,
                'message' : message,
                'related_blogs' : related_blogs,
            }
            return render(request, 'detailBlog.html', context)

    else:
        form = SubscriptionForm()
        blog = Blog.objects.get(id=id_blog)
        related_blogs = Blog.objects.all().exclude(id=id_blog).order_by("?")[:4]
        context = {
            'blog' : blog,
            'form' : form,
            'related_blogs' : related_blogs,
        }
        return render(request, 'detailBlog.html', context)

def project(request):
    return render(request, 'project.html')

def aboutStory(request):
    return render(request, 'aboutStory.html')

def aboutTeam(request):
    return render(request, 'aboutTeam.html')

def aboutTechnologies(request):
    return render(request, 'aboutTechnologies.html')

def consultation(request):
    return render(request, 'consultation.html')

def blog(request):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriptionForm()
            blogs = Blog.objects.all()
            trendings = Blog.objects.all().order_by("?")[:4]
            message = 'berhasil'
            context = {
                'blogs' : blogs,
                'form' : form,
                'trendings' : trendings,
                'message' : message,
            }
            return render(request, 'blog.html', context)

        else:
            form = SubscriptionForm()
            blogs = Blog.objects.all()
            trendings = Blog.objects.all().order_by("?")[:4]
            message = 'error'
            context = {
                'blogs' : blogs,
                'form' : form,
                'trendings' : trendings,
                'message' : message,
            }
            return render(request, 'blog.html', context)

    else:
        form = SubscriptionForm()
        blogs = Blog.objects.all()
        trendings = Blog.objects.all().order_by("?")[:4]
        context = {
            'blogs' : blogs,
            'trendings' : trendings,
            'form' : form,
        }
        return render(request, 'blog.html', context)


def blog_detail(request, id_blog):

    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriptionForm()
            blog = Blog.objects.get(id=id_blog)
            message = "berhasil"
            context = {
                'form' : form,
                'blog' : blog,
                'message' : message,
            }
            return render(request, 'blog_detail.html', context)

        else:
            form = SubscriptionForm()
            blog = Blog.objects.get(id=id_blog)
            message = "error"
            context = {
                'form' : form,
                'blog' : blog,
                'message' : message,
            }
            return render(request, 'blog_detail.html', context)

    else:
        form = SubscriptionForm()
        blog = Blog.objects.get(id=id_blog)
        context = {
            'form' : form,
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