from django.shortcuts import render
from django.http import Http404

def service_detail(request, id):
    # Mapping of service IDs to static page names
    service_pages = {
        1: 'services/mortgage_advice.html',
        2: 'services/financial_health_check.html',
        3: 'services/investment_planning.html',
        4: 'services/retirement_strategies.html',
       
    }
    
    # Get the corresponding page for the service ID
    service_page = service_pages.get(id)
    
    if not service_page:
        raise Http404("Service not found")
    
    # Render the corresponding static page
    return render(request, service_page)
