from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def test_vue(request):
    return render(request, 'vue_app/test.html')