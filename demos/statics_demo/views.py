from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def statics_post(request):
    return render_to_response('the_statics_file.html', context_instance=RequestContext(request))





