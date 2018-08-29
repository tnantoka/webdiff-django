from difflib import HtmlDiff
from django.shortcuts import render

from lxml.html import fromstring, tostring

# Create your views here.
def index(request):
    return render(request, 'index.html')

def compare(request):
    fromlines = request.POST['fromlines']
    tolines = pk=request.POST['tolines']
    table = HtmlDiff().make_table(fromlines.split('\n'), tolines.split('\n'))
    html = fromstring(table)
    html.xpath('//table')[0].set('class', 'table table-sm table-bordered')
    for node in html.xpath('//colgroup'):
        node.getparent().remove(node)
    for node in html.find_class('diff_next'):
        node.getparent().remove(node)
    for node in html.find_class('diff_header'):
        node.classes.add('bg-light')
        node.classes.add('border-right-0')
        node.getnext().classes.add('border-left-0')
        node.getnext().classes.add('w-50')
    return render(request, 'index.html', {
        'fromlines': fromlines,
        'tolines': tolines,
        'diff': tostring(html).decode(),
    })
