from django.db import models

"""
Columns
- Date of offer: postdate
- Supermarket company name: company_name
- Price: price
- Condition: deal
- Brand: brand_name
- Item name: item_name

"""

class Groceryitems(models.Model):
  post_date = models.DateField()
  company_name = models.CharField(max_length=30)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  condition = models.CharField(max_length=30)
  brand_name = models.CharField(max_length=30)
  item_name = models.CharField(max_length=50)
