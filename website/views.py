from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    return render(request, 'website/index.html')

def skills(request):
    return render(request, 'website/skills.html')

def projects(request):
    return render(request, 'website/projects.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'New Contact from {name}'
        body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'

        try:
            send_mail(
                subject,
                body,
                'aswinvs@zohomail.in',        # your email
                ['aswinvs@zohomail.in'],      # recipient
                fail_silently=False,
            )

            # ✅ Django success message
            messages.success(request, "Your message has been successfully sent. I’ll get back to you soon.")
        except Exception as e:
            # ❌ Error message if sending fails
            messages.error(request, "Oops! Something went wrong. Please try again later.")

        return redirect('contact')

    return render(request, 'website/contact.html')
