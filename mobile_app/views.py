from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Home page - render index.html
def home(request):
    return render(request, 'mobile_app/index.html')


# Mobile validation API (already ready)
@csrf_exempt
def validate_mobile(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        if mobile and len(mobile) == 10 and mobile.isdigit():
            return JsonResponse({'message': 'Valid mobile number'})
        else:
            return JsonResponse({'message': 'Invalid mobile number'})
    return JsonResponse({'message': 'Invalid request'})
