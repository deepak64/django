from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from article.forms import ArticleForm


def articles(request):
    language="en-gb"
    session_language="en-gb"
    if 'lang' in request.COOKIES:
        language=request.COOKIES['lang']
    return render_to_response('articles.html',
        {'articles':Article.objects.all(),
         'language':language,
         'session_language':session_language})

def article(request,article_id=1):
    return render_to_response('article.html',
        {'article':Article.objects.get(id=article_id)})

def language(request,language='en-gb'):
    response=HttpResponse("setting language to %s" % language)

    response.set_cookie('lang',language)

    request.session['lang']=language

    return response

def create(request):
    if request.POST:
        form=ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')

    else:
        form=ArticleForm()

    args={}
    args.update(csrf(request))
    args['form']=form

    return render_to_response('create_article.html',args)

def like_article(request,article_id):
    if article_id:
        a=Article.objects.get(id=article_id)
        count=a.likes
        count+=1
        a.likes=count
        a.save()
    return HttpResponseRedirect('/articles/get/%s' % article_id)























# OLD TILL VIDEO 3
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
# Create your views here.
def hello(request):
    name="vijay"
    html="<html><boby>Hi %s,this seems to have worked!</body></html>" % name
    return HttpResponse(html)

def vijay(request):
    ln="batham"
    nm="vijay"
    html="<html><boby>Hello hello hello %s,this seems to have worked!</body></html>"%ln
    return HttpResponse(html)

def hello_template(request):
    name="Vijay Batham"
    college="IIIT Allahabad"
    city="Kanpur"
    t=get_template('hello.html')
    html=t.render(Context({'name':name,'college':college,'city':city}))
    return HttpResponse(html)

def hello_template_simple(request):
    name="Vijay K. Batham"
    city="Bangalore"
    return render_to_response('hello.html',{'name':name,'city':city})

class HelloTemplate(TemplateView):
    template_name='hello_class.html'
    def get_context_data(self,**kwargs):
        context=super(HelloTemplate,self).get_context_data(**kwargs)
        context['name']='Vijay Batham'
        return context
"""






































