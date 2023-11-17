def certificate_list(request):
    from django.shortcuts import render
    from cert_app.models import Certificate

    certificates = Certificate.objects.all()
    return render(request, 'certificate_list.html', {'certificates': certificates})