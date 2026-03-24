from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .bot_engine import super_ai

def home(request):
    return render(request, 'index.html')

def admin_dashboard(request):
    return render(request, 'admin.html')

def delivery_dashboard(request):
    return render(request, 'deliveryman.html')

# ADD THESE NEW VIEWS:
def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def categories_view(request):
    return render(request, 'categories.html')

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            image_data = data.get('image', None)
            
            if not message and not image_data:
                return JsonResponse({'error': 'No input provided'}, status=400)
            
            # Use the Super AI logic with image context if provided
            response_text = super_ai(message, has_image=bool(image_data))
            return JsonResponse({'response': response_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)