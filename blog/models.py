from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	bio = models.TextField()

	def __str__(seft):
		return seft.name

class Category(models.Model):
	category = models.CharField(max_length=100)
	description = models.TextField()


	def __str__(seft):
		return seft.category


class Article(models.Model):
	title = models.CharField(max_length=250)
	image = models.ImageField(upload_to="static/images/")
	content = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(seft):
		return seft.title



# ====================== Restaurant Manager =========================
# from django.db import models

class Restaurants(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(seft):
        return seft.name

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    shift_details = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(seft):
        return seft.name

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    loyalty_points = models.IntegerField(default=0)

    def __str__(seft):
        return seft.name

class MenuItems(models.Model):
    item_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    availability_status = models.CharField(max_length=50)

    def __str__(seft):
        return seft.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(seft):
        return seft.order_type

class OrderDetails(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(seft):
        return seft.quantity

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    current_quantity = models.PositiveIntegerField()
    threshold_quantity = models.PositiveIntegerField()
    supplier_details = models.TextField()

    def __str__(seft):
        return seft.item_name

class ThirdPartyPlatforms(models.Model):
    platform_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    api_details = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(seft):
        return seft.name

class ThirdPartyOrders(models.Model):
    third_party_order_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    platform = models.ForeignKey(ThirdPartyPlatforms, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(seft):
        return seft.platform

class TableReservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    table_number = models.PositiveIntegerField()
    reservation_time = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(seft):
        return seft.reservation_time

class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(seft):
        return seft.amount

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(seft):
    return seft.comment
