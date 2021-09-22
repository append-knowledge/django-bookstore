from django.db import models
from datetime import timedelta,date

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=80)
    price=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    image=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.book_name

#first open shell and import this

#reference=model_name(book_refernce='value'.......)
#book=Book(book_name='half girl friend',author='mt',price=250,copies=300)
#reference.save()

#orm(object relation mapped) to get all the values
#reference=model_name.objects.all()
#book=Book.objects.all()


#orm for fetching a specific record
#reference=model_name.objects.get(field_name=value)
#book=Book.objects.get(id=value)

#orm query for updating a specific record
#book=Book.objects.get(id=value)
#book.price=new value
#book.save()


#to get specific catrgory values
#for price less than 300
#ref=model_name.objects.filter(pricr__lt=300)
#for less than or equal to 300
#ref=model_name.objects.filter(price__lte=300)
#greater than or equal to 300
#ref=model_name.objects.filter(price__gte=300)

#to search a keyword using unsensitive of weather capital or small letter
#ref=model_name.objects.filter(book_name__iexact='letter')

#to search using only some words
#ref=model_name.objects.filter(book_name__container='letter')

#to list according to desending order of price
#ref=model_name.objects.all().order_by('-price)'

#by ascending order
#ref=model_name.objects.all().order_by('price')


class Order(models.Model):

    products=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    address=models.CharField(max_length=120)
    option=(('delivered','delivered'),('cancel','cancel'),('intransit','intransit'),('ordered','ordered'))
    status=models.CharField(max_length=20,choices=option,default='ordered')
    phone_number=models.CharField(max_length=10)
    edd=date.today()+timedelta(days=5)
    delivery_date=models.DateField(null=True,default=edd)




