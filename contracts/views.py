from django.http import HttpResponse
from django.shortcuts import render

from contracts.forms.DateFilterForm import DateFilterForm
from contracts.models import Client, Contract

def report(request):
    """
    Get a report of contracts grouped by client.
    The contracts should be filtered by creation date.
    The report records should be sorted by total price of contracts.
    The report should contain the following information:
    - Client name
    - Total number of contracts
    - Total price of contracts
    """
    form = DateFilterForm(request.GET)
    if not form.data:
        form.errors.clear()
        return render(request, 'report.html', {'form': form})
    if not form.is_valid():
        return render(request, 'report.html', {'form': form})
        
    start_date = form.cleaned_data['start_date']
    end_date = form.cleaned_data['end_date']
    
    contracts = Contract.objects.all()
    results = []
    for contract in contracts:
        # Filter by creation date
        in_date_range = contract.creation_date >= start_date and contract.creation_date <= end_date
        if not in_date_range:
            continue
        client = contract.client
        # Find the client in the results and update it
        client_found = False
        for result in results:
            if result['client'] == client:
                client_found = True
                result['contracts'] += 1
                result['total_price'] += contract.price
                break
        # If the client is not in the results, add it
        if not client_found:
            results.append({
                'client': client,
                'contracts': 1,
                'total_price': contract.price
            })
    # Sort the results by total price
    results.sort(key=lambda result: result['total_price'], reverse=True)
    return render(request, 'report.html', {
        'form': form,
        'results': results,
        'summary': {
            'contracts': sum(result['contracts'] for result in results),
            'total_price': sum(result['total_price'] for result in results),
            'clients': len(results)
        }
    })

def client_list(request):
    clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients})

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, "contract_list.html", {"contracts": contracts})
