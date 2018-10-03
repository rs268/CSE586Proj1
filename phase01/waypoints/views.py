from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class AppView(View):
    template_name = 'addresses.html'

    def get(self, request):
        return render(request, self.template_name, None)

    def post(self, request):
        print(request.POST)
        return HttpResponse('SUCCESS')