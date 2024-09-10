from django.shortcuts import render
from subprocess import run, CalledProcessError
from django.views.decorators.csrf import csrf_exempt
from .main import main
from django.http import JsonResponse

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        topics = request.POST.get('topics')
        keywords = request.POST.get('keywords')  # Correct 'keyword' to 'keywords' if that was a typo
        print(topics,keywords)

        try:
            # Call the function and pass the parameters
            result = main(topics, keywords)  # Adjust depending on how you've structured your main.py
            # Print script output and return a JsonResponse
            print("Script output:", result)
            return JsonResponse({'status': 'success', 'output': result})

        except Exception as e:
            # Handle exceptions that might occur during the function execution
            print("Error during script execution:", e)
            return JsonResponse({'status': 'error', 'error': str(e)})

    # Return a response for non-POST requests as well
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

