# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def session_operate(request):
    if 'post1' and 'post2' in request.POST:
        if request.POST['post1'] and request.POST['post2']:
            post1 = request.POST['post1']
            post2 = request.POST['post2']
            request.session['session_test1'] = post1
            request.session['session_test2'] = post2
            # save the session...
            return render_to_response('session_operate.html',
                                      {'session_post': False},
                                      context_instance=RequestContext(request),
                                      )
        else:
            return HttpResponse('you have submit a blank form....^~^')
    else:
        return render_to_response('session_operate.html',
                                  {'session_post': True},
                                  context_instance=RequestContext(request))


def session_operate_1(request):
    if 'session_test1' and 'session_test2' in request.session:
        session_test_1 = request.session['session_test1']
        session_test_2 = request.session['session_test2']
        # withdraw the session.
        return render_to_response('session_operate_1.html',
                                  {'session_test1': session_test_1, 'session_test2': session_test_2},
                                  )
    else:
        return HttpResponse('you did not have any session to show')





# Create your views here.
