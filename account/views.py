from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_page(request):
    return render(request, 'account/user_page.html', {'section': 'user_page'})
