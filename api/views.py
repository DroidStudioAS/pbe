from django.http import JsonResponse

def test_view(request):
    return JsonResponse({
        "message": "Hello from the API! The server is working correctly.",
        "status": "success"
    })
