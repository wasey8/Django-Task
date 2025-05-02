from celery import shared_task
from django.core.mail import send_mail
import csv
from .models import Product

@shared_task
def import_csv():
    with open('mock_products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

@shared_task
def validate_data(data):
    updates = []
    for item in data:
        sku = item['sku']
        qty = int(item['inventory_quantity'])
        try:
            product = Product.objects.get(sku=sku)
            product.inventory_quantity = qty
            product.save()
            updates.append(f"{sku} -> {qty}")
        except Product.DoesNotExist:
            continue
    return updates

@shared_task
def send_summary_email(updates):
    message = "Inventory Update Summary:\n" + "\n".join(updates)
    send_mail(
        subject="Nightly Inventory Update",
        message=message,
        from_email="no-reply@example.com",
        recipient_list=["admin@example.com"],
        fail_silently=False
    )