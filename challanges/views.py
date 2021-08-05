from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# def january(request):
#     return HttpResponse('Eat no meat for the whole month')


# def february(request):
#     return HttpResponse('Go for a run every day')


# def march(request):
#     return HttpResponse('Be happy daily')

monthly_challanges = {
    'january': 'Eat no meat for the whole month',
    'february': 'Go for a run every day',
    'march': 'Be happy daily',
    'april': 'Drink more wine',
    'may': 'Eat less chocolate',
    'june': 'Go for more walks',
    'july': 'Sleep more',
    'august': 'Eat no meat for the whole month',
    'september': 'Go for a run every day',
    'october': 'Be happy daily',
    'november': 'Drink more wine',
    'december': 'Eat less chocolate',
}


def index(request):
    list_items = ''
    months = list(monthly_challanges.keys())
    for month in months:
        month_path = reverse('month_challange', args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</li>'
    # list of <li>s
    list_of_months = f'<ul>{list_items}</ul>'
    return HttpResponse(list_of_months)


def monthly_challange(request, month):  # <month> was the id in the angle brackets
    try:
        challange_text = monthly_challanges[month]
        response_data = f'<h1>{challange_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('This month is not supported')


def monthly_challange_by_number(request, month):
    # wrapping with list makes into real list
    months = list(monthly_challanges.keys())
    # some safety for months
    if (month > len(months)):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month_challange', args=[
                            redirect_month])  # see urls.py

    return HttpResponseRedirect(redirect_path)
