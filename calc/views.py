__author__ = 'Mihail Perminov <PerminovMA@live.ru>'

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from calc.calc_logic import calculate_expression


@csrf_exempt
def calculate_response(request):
    expression = None if request.POST.get("display_field") is None else request.POST.get(
        "display_field").__str__().strip()

    result = calculate_expression(expression)

    return HttpResponse(result)