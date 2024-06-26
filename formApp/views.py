from django.shortcuts import render
from .import forms

def form_name_view(request):
    form=forms.FormName()
# check to see if we are getting a POST request back
    if request.method == "POST":
        form=forms.FormName(request.POST)
# Then we check to see if the form is valid 
        if form.is_valid():
# if form.is_valid ==True them do something
         print("Form validation successful ! See console for information:")
         print("Name:"+form.cleaned_data['name'])
         print("email:"+form.cleaned_data['email'])
         print("message:"+form.cleaned_data['text'])
    return render(request, 'home.html', {'form':form})

# Create your views here.
