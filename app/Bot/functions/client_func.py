from wildberries.models import Accounting_Records,Products
from asgiref.sync import sync_to_async  
from Bot.config.config import URL

@sync_to_async
def exists_user(user_id):
    data=Accounting_Records.objects.filter(user_id=user_id)
    return data.exists()

@sync_to_async
def create_user_record(user_id,username,profile_name):
    data=Accounting_Records.objects.create(user_id=user_id,username=username,profile_name=profile_name)
    data.save()
    

@sync_to_async
def create_product(name, article, price, rating, quantity):
    data = Products.objects.filter(article=article)
    if data.exists():
        # Update the existing product
        product = data.first()  # Assuming you want to update the first match
        product.name = name
        product.price = price
        product.rating = rating
        product.quantity = quantity
        product.save()
    else:
        # Create a new product if it doesn't exist
        product = Products.objects.create(
            name=name,
            article=article,
            price=price,
            rating=rating,
            quantity=quantity
        )
    return product

