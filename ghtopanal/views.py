from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods

from .tasks import *

@require_http_methods(["POST"])
def analyze(request, pair_id):
    process.delay(pair_id, request.POST)
    return HttpResponse(pair_id, mimetype='text/plain')
