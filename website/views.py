from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send Email
        send_mail(
            message_name,
            message,
            message_email,
            ['john@codemy.com'],
        )

        return render(request, 'contact.html', {'message_name': message_name,
                                                'message_email': message_email,
                                                'message': message})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def service(request):
    return render(request, 'service.html', {})


def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        # Send Email
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Day: " + your_date + " Message: " + your_message
        send_mail(
            'Appointment Request',
            appointment,
            your_email,
            ['john@codemy.com'],
        )

        return render(request, 'appointment.html', {'your_name': your_name,
                                                    'your_phone': your_phone,
                                                    'your_email': your_email,
                                                    'your_address': your_address,
                                                    'your_schedule': your_schedule,
                                                    'your_time': your_time,
                                                    'your_message': your_message})
    else:
        return render(request, 'home.html', {})
