from django.template import Context, loader
from metrics.dashboard.models import Heatmap
from django.http import HttpResponse

def index(request):
	title = 'Firefox Tab Heatmap'
			
	t = loader.get_template('tab.html')
	c = Context({
	    'title': title,
	})
	
	return HttpResponse(t.render(c))

def tab(request):
	title = 'Firefox Tab Heatmap'
			
	t = loader.get_template('tab.html')
	c = Context({
	    'title': title,
	})
	
	return HttpResponse(t.render(c))

def heatmap(request):
	title = 'Firefox Tab Heatmap'
			
	t = loader.get_template('heatmap.html')
	c = Context({
	    'title': title,
	})
	
	return HttpResponse(t.render(c))