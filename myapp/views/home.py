from django.shortcuts import render
from django.views import View
from myapp.models import Notice, News


class HomeView(View):
    def get(self, request):

        notice = Notice.objects.all()[:6]
        news = News.objects.all()[:10]
        return render(request, 'home.html', {'notice': notice, 'news': news})


def shownotice(request, id):
    shownot = Notice.objects.get(pk=id)

    return render(request, 'shownotice.html', {'shownot': shownot})


def shownews(request, id):
    shownews = News.objects.get(pk=id)
    return render(request, 'shownews.html', {'shownews': shownews})
