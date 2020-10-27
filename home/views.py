from django.shortcuts import render
#from django.views.generic.list import
#from posts.models import
#from posts.forms import
#from django.contrib.auth.decorators import login_required
#from django.utils import timezone

def HomeIndex(request):
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits +1

    context = {
            "num_visits": num_visits,
            }
    return render(request, "index.html", context)
