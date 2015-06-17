#coding: utf-8

from urlparse import urljoin
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from url_manager.views import get_short_id, get_long_url
from url_manager.models import WrongURL, ShortURL

BASEURL = 'http://url.hsmoa.com/'

def index(request):
    u'''메인 페이지'''
    urls = ShortURL.objects.all()
    context = {
                'BASEURL': BASEURL,
                'shortUrls': urls,
            }
    return render_to_response('index.html', context)

def long_url(request, id):
    u'''짧은 url을 입력받아 긴 url주로소 리다이렉트 해준다.'''
    long_url = get_long_url(id)
    return HttpResponseRedirect(long_url) if long_url else HttpResponse('url 이 존재하지 않습니다.')

def short_url(request):
    u'''긴 URL을 받아서 짧은 URL을 반환'''
    if request.method == "POST":
        url = get_value(request, 'POST', 'url')
    elif request.method == "GET":
        url = get_value(request, 'GET', 'url')

    short_id = get_short_id(url)
    if isinstance(short_id, WrongURL):
        return HttpResponse(short_id.error_message)

    return HttpResponse(urljoin(BASEURL, short_id))

def get_value(request, method, key, default=''):
    u'''요청메소드에서 값을 추출해 반환한다.'''
    if method == 'GET':
        return request.GET[key] if key in request.GET else default
    elif method == 'POST':
        return request.POST[key] if key in request.POST else default
    elif method == 'FILES':
        return request.FILES[key] if key in request.FILES else default
    else:
        return default
