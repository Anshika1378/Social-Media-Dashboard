from .firebase import db
from .forms import User_Registration_Form,Login_Form,PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .firebase import db, bucket
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Post
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse





# ✅ Login View
def Login(request):

    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            password = form.cleaned_data['password']

            users_ref = db.reference('users')
            users = users_ref.get()

            for key, user in users.items():
                if user['email'] == account and user['password'] == password:
                    request.session['user_email'] = user['email']
                    return redirect('socialdashboard')

            form.add_error(None, 'Invalid email or password')
    else:
        form = Login_Form()

    return render(request, 'login.html', {'form': form})

# ✅ Register View


def Register(request):
    if request.method == "POST":
        form = User_Registration_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # ✅ Create Django user
            user = User.objects.create_user(
                username=email,  # using email as username
                email=email,
                password=password,
                first_name=name  # saving "name" to first_name
            )

            # ✅ Also store user in Firebase (optional)
            ref = db.reference('users')  # Firebase node
            ref.push({
                'name': name,
                'email': email
                # Do NOT store raw password ideally
            })

            return redirect('login-file')
    else:
        form = User_Registration_Form()

    return render(request, 'auth/register.html', {'form': form})


# ✅ Dashboard View

@login_required(login_url='login-file')
def social_dashboard(request):
    user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('socialdashboard')
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'dashboard/socialdashboard.html', {
        'form': form,
        'posts': posts,
        'user': user,
    })




@login_required(login_url='login-file')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Allow deletion only if the post belongs to the logged-in user
    if post.user == request.user:
        post.delete()

    return HttpResponseRedirect(reverse('socialdashboard'))
