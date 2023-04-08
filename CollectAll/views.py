from.models import Collection, CollectionItem, CollectionType, UserComment
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


def index(request):
	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
		'num_visits': num_visits,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'CollectAll/index.html', context=context)



class MyCollectionsView(LoginRequiredMixin, generic.DetailView):
	model = Collection



