from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    state = models.CharField(_('State'), max_length=256)
    city = models.CharField(_('City'), max_length=256)
    address = models.CharField(_('Address'), max_length=256)
    closest_bstop = models.CharField(_('Closest Bustop'), max_length=256)

    def __str__(self):
        return self.city + " , " + self.state


class Product(models.Model):
    name = models.CharField(_('Product name'), max_length=256)
    sku = models.CharField(_('Stock keeping unit'), max_length=256)
    price = models.IntegerField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))
    date_added = models.DateTimeField(_('Date added'), auto_now=True)

    def __str__(self):
        return self.sku + " - " + self.name


class Warehouse(models.Model):
    name = models.CharField(_('Name'), max_length=256)
    location = models.ForeignKey(Location)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name + " at " + self.location.city


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(_('Phone number'), max_length=15)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(_('Quantity'))
    date_added = models.DateTimeField(_('date added'), auto_now=True)
    warehouse = models.ManyToManyField(Warehouse,verbose_name=_('Pick up from'),blank=True)

    def __str__(self):
        return self.product.name + " - " + str(self.quantity)

    def total(self):
        return self.product.price * self.quantity

    def pick_up_from(self):
        return "\n, ".join([p.name for p in self.warehouse.all()])


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    date_added = models.DateTimeField(_('date added'), auto_now=True)
    extra_details = models.TextField(_('extra details'), blank=True)
    total_amount = models.CharField(_('total amount'), max_length=250)
    invoice_number = models.CharField(_('invoice number'), max_length=250, unique=True)
    choices = (('Processing', 'Processing'),
               ('Shipped', 'Shipped'),
               ('Canceled', 'Canceled'),
               ('Complete', 'Complete'),
               ('Confirmed', 'Confirmed'),
               ('Denied', 'Denied'),
               ('Canceled Reversal', 'Canceled Reversal'),
               ('Failed', 'Failed'),
               ('Refunded', 'Refunded'),
               ('Reversed', 'Reversed'),
               ('Chargeback', 'Chargeback'),
               ('Pending', 'Pending'),
               ('Voided', 'Voided'),
               ('Processed', 'Processed'),
               ('Expired', 'Expired'),
               )
    tracking = models.CharField(_('tracking'), max_length=250, choices=choices,default="Pending")
    payment_methods = (('Card', 'Card'), ('Pay On Delivery', 'Pay On Delivery'), ('Bank Deposit', 'Bank Deposit'),
                       ('Bank Transfer', 'Bank Transfer'))
    payment_method = models.CharField(_('payment method'), max_length=250, choices=payment_methods)
    address = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, verbose_name=_('Location of order'), related_name="location_of_order",
                                 on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.invoice_number

    def get_absolute_url(self):
        return "/orders/%i" % self.pk

class Delivery(models.Model):
    orders = models.ManyToManyField(Order)
    date_added = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location,verbose_name=_("Current Location"))

    choices = (
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('En Route', 'En Route'),
    )

    status = models.CharField(max_length=256, choices=choices)

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')


    def __str__(self):
        return self.location.address

