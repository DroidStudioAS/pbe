from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def test_view(request):
    if request.method == 'GET':
        return JsonResponse({
            "message": "Hello from the API! The server is working correctly.",
            "status": "success"
        })
    return JsonResponse({
        "message": "Method not allowed",
        "status": "error"
    }, status=405)
