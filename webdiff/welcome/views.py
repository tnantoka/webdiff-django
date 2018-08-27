from difflib import HtmlDiff
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def compare(request):
    fromlines = request.POST['fromlines']
    tolines = pk=request.POST['tolines']
    return render(request, 'index.html', {
        'fromlines': fromlines,
        'tolines': tolines,
        'diff': HtmlDiff().make_table(fromlines.split('\n'), tolines.split('\n')),
    })
