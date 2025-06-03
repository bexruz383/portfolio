from django.shortcuts import render, redirect

from app.form import ContactForm
from app.models import Home, Portfoliyo, Blog, Skills, Projects


def index_wiev(request):
    homepage = Home.objects.all()
    portfoliyo = Portfoliyo.objects.all()
    blog = Blog.objects.all().order_by('-id')[:3]
    skill = Skills.objects.all()
    projects = Projects.objects.all()
    return render(request=request,
                  template_name='app/index.html',
                  context={'homepage': homepage,
                           'portfoliyo': portfoliyo,
                           'blog': blog,
                           'skill': skill,
                           'projects': projects})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        form = ContactForm()
        return render(request=request,
                      template_name='app/index.html',
                      context={"form": form})
