from django.template import Context, loader
from metrics.dashboard.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse

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
	items = Heatmap.objects.all()
	
	firefox_button = items[4]
	tab_scroll_left = items[43]
	tab_scroll_right = items[44]	
	new_tab_button = items[45]
	list_all_tabs = items[46]			
	
	back = items[26]
	forward = items[27]
	recent_history_drop_down = items[28]
	reload_button = items[29]
	stop = items[30]
	home = items[31]
	
	site_id_normal = items[54]
	site_id_ev = items[55]
	site_id_ssl = items[56]		

	url_enter_key = items[57]
	url_go_button = items[58]	
	url_search_enter_key = items[59]	
	url_search_go_button = items[59]		
	most_visited_drop_down = items[61]
	rss = items[32]
	bookmark_star = items[33]
	bookmarks_star_edit = items[34]
	bookmarks_star_remove = items[35]	
	
	search_drop_down = items[48]
	search_drop_down_select = items[49]	
	search_enter_key = items[50]
	search_go_button = items[51]
	
	bookmarks_button = items[68]
	feedback = items[63]
	
	scroll_up = items[36]
	scroll_down = items[37]
	scroll_vertical_bar = items[38]	
	
	scroll_left = items[39]
	scroll_right = items[40]
	scroll_horizontal_bar = items[41]
		
	tabs_on_top = items[0]
	menu_bar = items[1]
	bookmarks_bar = items[2]
	status_bar = items[3]

			
	t = loader.get_template('heatmap.html')
	c = Context({
	    'title': title,
	    'items':items,
	    'firefox_button':firefox_button,
			'firefox_button':items[4],
			'tab_scroll_left':items[43],
			'tab_scroll_right':items[44],	
			'new_tab_button':items[45],
			'list_all_tabs':items[46],	    
	})
	
	return HttpResponse(t.render(c))