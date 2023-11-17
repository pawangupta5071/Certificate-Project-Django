def generate_certificate(request):
    from django.shortcuts import render, redirect
    from cert_app.forms import CertificateForm

    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm()
    return render(request, 'generate_certificate.html', {'form': form})