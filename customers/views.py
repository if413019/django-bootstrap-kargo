from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import render, redirect
from customers.forms import ODCustomerForm
from customers.models import ODCustomer


def index(request):
    """
    Handle index page for customer
    """

    return render(request, 'customer/index.html')


def customers(request):
    """
    Showing list of customer in management home page
    """

    # query on all customer records
    customers = ODCustomer.objects.all()

    # structured customer into simple dict, 
    # later on, in template, we can render it easily, ex: {{ customers }}
    data = {'customers': customers}

    return render(request, 'customer/customers.html', data)


def create_customer(request):
    """
    Handle new customer creation
    """

    # Initial form and data
    data = {
        'form': ODCustomerForm(),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        form = ODCustomerForm(request.POST, request.FILES)

        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            # wrap form result into dict ODCustomer model fields structure 
            customer_data = {
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'phone': form.cleaned_data.get('phone'),
                'address': form.cleaned_data.get('address'),
                'picture': form.cleaned_data.get('picture'),
            }

            try:
                ODCustomer.objects.create(**customer_data)
                messages.info(request, "A new record of customer has been created!")
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")
        else:
            messages.error(request, "form invalid")
    return render(request, 'customer/create_customer.html', data)


def edit_customer(request, uuid=None):
    """
    How to edit customer
    """
    if not uuid:
        return redirect(reverse('customer:customers'))

    # validate given UUID match with record in database
    try:
        customer = ODCustomer.objects.get(uuid=uuid)
    except ODCustomer.DoesNotExist:
        messages.error(request, "Record not found!")
        return redirect(reverse('customer:customers'))

    data = {
        'form': ODCustomerForm(instance=customer),
    }

    # if user submit data from this page, we capture the POST data and save it
    if request.method == 'POST':

        # wrap POST data with the form
        #form = ODCustomerForm(request.POST, instance=customer)
        form = ODCustomerForm(request.POST, request.FILES ,instance=customer)
        # Transaction savepoint (good to provide rollback data)
        sid = transaction.savepoint()

        if form.is_valid():

            try:
                form.save()
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")

            messages.info(request, "Record has been updated!")  
        else:
            messages.info(request, "Form is Invalid!")

    return render(request, 'customer/edit_customer.html', data)


def delete_customer(request, uuid=None):
    """
    How to remove customer
    """
    if uuid:
        # finding given UUID to match customer in database
        try:
            customer = ODCustomer.objects.get(uuid=uuid)
        except ODCustomer.DoesNotExist:
            messages.error(request, "Customer not found")
        else:
            # delete customer from database
            customer.delete()
            messages.success(request, 'Customer "{}" has been deleted'.format(customer.name))

    return redirect(reverse('customer:customers'))
