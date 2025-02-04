from django.shortcuts import render
from .forms import FeedbackForm
# Create your views here.
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            return render(request, 'thankyou.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form':form})
