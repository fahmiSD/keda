from django.shortcuts import render
from website.forms import *
from django.http import HttpResponse

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
            careers = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').filter(status=1)
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
            careers = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').filter(status=1)
            context = {
                'form' : form,
                'message' : message,
                'careers' : careers
            }
            return render(request, 'aboutCareer.html', context)

    else:
        form = SubscriptionForm()
        careers = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').filter(status=1)
        context = {
            'form' : form,
            'careers' : careers,
        }
        return render(request, 'aboutCareer.html', context)

def detailCareer(request, slug_career):
    if request.method == 'POST':
        if request.POST.get("form_type") == 'form_candidate':
            form_candidate = CandidateForm(request.POST, request.FILES)
            if form_candidate.is_valid():
                form_candidate.save()
                career = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').get(slug_career=slug_career)
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
                career = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').get(slug_career=slug_career)
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
                career = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').get(slug_career=slug_career)
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
                career = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').get(slug_career=slug_career)
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
        career = Career.objects.select_related('career_tag_id', 'career_tag_id__color_id').get(slug_career=slug_career)
        form_candidate = CandidateForm()
        form_subs = SubscriptionForm()
        context = {
            'career' : career,
            'form_candidate' : form_candidate,
            'form_subs' : form_subs,
        }
        return render(request, 'detailCareer.html', context)

def detailBlog(request, slug_blog):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            
            form.save()
            form = SubscriptionForm()
            blog = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').get(slug_blog=slug_blog)
            related_blogs = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').exclude(id=slug_blog).order_by("?")[:4]
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
            blog = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').get(slug_blog=slug_blog)
            related_blogs = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').exclude(slug_blog=slug_blog).order_by("?")[:4]
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
        blog = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').get(slug_blog=slug_blog)
        related_blogs = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').exclude(slug_blog=slug_blog).order_by("?")[:4]
        context = {
            'blog' : blog,
            'form' : form,
            'related_blogs' : related_blogs,
        }
        return render(request, 'detailBlog.html', context)

def project(request):
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
            return render(request, 'project.html', context)

        else:
            form = SubscriptionForm()
            message = "error"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'project.html', context)

    else:
        form = SubscriptionForm()
        context = {
            'form' : form,
        }
        return render(request, 'project.html', context)

def aboutStory(request):
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
            return render(request, 'aboutStory.html', context)

        else:
            form = SubscriptionForm()
            message = "error"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'aboutStory.html', context)

    else:
        form = SubscriptionForm()
        context = {
            'form' : form,
        }
        return render(request, 'aboutStory.html', context)

def aboutTeam(request):
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
            return render(request, 'aboutTeam.html', context)

        else:
            form = SubscriptionForm()
            message = "error"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'aboutTeam.html', context)

    else:
        form = SubscriptionForm()
        context = {
            'form' : form,
        }
        return render(request, 'aboutTeam.html', context)

def aboutTechnologies(request):
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
            return render(request, 'aboutTechnologies.html', context)

        else:
            form = SubscriptionForm()
            message = "error"
            context = {
                'form' : form,
                'message' : message,
            }
            return render(request, 'aboutTechnologies.html', context)

    else:
        form = SubscriptionForm()
        context = {
            'form' : form,
        }
        return render(request, 'aboutTechnologies.html', context)

def blog(request):
    if request.POST:
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscriptionForm()
            blogs = Blog.objects.select_related('blog_tag', 'blog_tag__color_id')
            trendings = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').order_by("?")[:4]
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
            blogs = Blog.objects.select_related('blog_tag', 'blog_tag__color_id')
            trendings = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').order_by("?")[:4]
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
        blogs = Blog.objects.select_related('blog_tag', 'blog_tag__color_id')
        trendings = Blog.objects.select_related('blog_tag', 'blog_tag__color_id').order_by("?")[:4]
        context = {
            'blogs' : blogs,
            'trendings' : trendings,
            'form' : form,
        }
        return render(request, 'blog.html', context)

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

def process(request):
     return render(request, 'processOverview.html')

def consultation(request):
    if request.method == "POST":
        if request.POST.get("form_type") == "form_consult":
            form_consult = ConsultForm(request.POST)
            if form_consult.is_valid():
                form_consult.save()
                form_consult = ConsultForm()
                form_subs = SubscriptionForm()
                context = {
                    "form_consult" : form_consult,
                    "form_subs" : form_subs,
                    "success" : "Pertanyaan Anda telah terkirim!"
                }
                return render(request, "consultation.html", context)
            else:
                form_consult = ConsultForm(request.POST)
                form_subs = SubscriptionForm()
                context = {
                    "form_consult" : form_consult,
                    "form_subs" : form_subs,
                    "errors" : form_consult.errors,
                }
                return render(request, "consultation.html", context)
        elif request.POST.get("form_type") == "form_subs":
            form_subs = SubscriptionForm(request.POST)
            if form_subs.is_valid():
                form_subs.save()
                form_consult = ConsultForm()
                form_subs = SubscriptionForm()
                message = "berhasil"
                context = {
                    "form_consult" : form_consult,
                    "form_subs" : form_subs,
                    "message" : message,
                }
                return render(request, "consultation.html", context)
            else:
                form_consult = ConsultForm()
                form_subs = SubscriptionForm()
                message = "error"
                context = {
                    "form_consult" : form_consult,
                    "form_subs" : form_subs,
                    "message" : message,
                }
                return render(request, "consultation.html", context)
    else:
        form_consult = ConsultForm()
        form_subs = SubscriptionForm()
        context = {
            "form_consult" : form_consult,
            "form_subs" : form_subs,
        }
        return render(request, "consultation.html", context)

def processOverview(request):
    return render(request, 'processOverview.html')

def processBrief(request):
    return render(request, 'processBrief.html')

def processScope(request):
    return render(request, 'processScope.html')

def processEstimation(request):
    return render(request, 'processEstimation.html')

def processDevelopment(request):
    return render(request, 'processDevelopment.html')

def processSupport(request):
    return render(request, 'processSupport.html')

def processNextSteps(request):
    return render(request, 'processNextSteps.html')

def detailProject(request):
    return render(request, 'detailProject.html')
