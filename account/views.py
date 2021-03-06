from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from account.forms.profile_form import Profile_Form
from account.models import User
from account.forms.account_form import Account_Create_Form

def index(request):
    form = Account_Create_Form()
    return render(request, 'account_log_in/login.html', {
        'form': form
    })

def Profile(request):
    # The view to edit the profile
    profile = User.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = Profile_Form(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'account_info/account_info.html', {
        'form': Profile_Form(instance=profile),
    })

def register(request):
    # View to make an account
    image_link = "https://cdn.discordapp.com/attachments/834167476241301524/842356421542674462/default-user-image.png"
    # Image link to the default user image
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            profile = form.save()
            user = User(image=image_link, user_id=profile.id)
            user.save()
            return redirect('/account/login')
    return render(request, 'account_log_in/register.html', {
        'form': UserCreationForm()
    })




