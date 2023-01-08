from django.db import models
import math
 
class SneakerImgs (models.Model):
    # image1 = models.ImageField(upload_to="sneakers/images") or models.URLField()
    # image2 = models.ImageField(upload_to="sneakers/images") or models.URLField()
    # image3 = models.ImageField(upload_to="sneakers/images") or models.URLField()
    # image4 = models.ImageField(blank=True, null=True, upload_to="sneakers/images") or models.URLField(blank=True)


    image1 = models.URLField()  
    image2 = models.URLField()  
    image3 = models.URLField()  
    image4 = models.URLField(blank=True)  

    class Meta:
        verbose_name = "images"
        verbose_name_plural = "images"

    def __str__(self):
        return f"{self.image1[:50]}..."


class Color (models.Model):
    color = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.color}"


# class Gender (models.Model):
#     GENDER = [
#         ('men', 'men'),
#         ('women', 'women'),
#         ('all', 'all'),
#     ]
#     genders = models.CharField(max_length=20, choices=GENDER, default='all')
#     # color = models.CharField(max_length=250)
#     # colors = models.ManyToManyField(to=Color)

#     def __str__(self):
#         return f"Gender: {self.gender}"


class Sizes (models.Model):
    SIZES = [
        ('sm', 'sm'),
        ('md', 'md'), 
        ('l', 'l'),
        ('xl', 'xl')
    ]
    size = models.CharField(max_length=4, choices=SIZES, default="sm", unique=True)

    def __str__(self):
        return self.size

# Create your models here.
class Sneaker(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    imgs = models.ForeignKey(SneakerImgs, on_delete=models.CASCADE)
    alt = models.TextField(default="sneaker image")
    GENDER = [
        ('men', 'men'),
        ('women', 'women'),
        ('all', 'all'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER, default='all')
    colors = models.ManyToManyField(Color, max_length=2)
    # categories = models.ManyToManyField(Categories)
    sizes = models.ManyToManyField(Sizes)
    price = models.FloatField()
    discount_price = models.FloatField()

    # GET PERCENTAGE FROM PRICE AND DISCOUNT PRICE
    def percentage(self):
        return  math.floor(round((self.price / self.price -   self.discount_price / self.price) *   100, 0))

    # GET IMAGES IN A LIST
    def images(self):
        if self.imgs.image4:
            return list((self.imgs.image1, self.imgs.image2, self.imgs.image3, self.imgs.image4))
        else:
            return list((self.imgs.image1, self.imgs.image2, self.imgs.image3))

    class Meta:
        verbose_name = "Sneaker"
        verbose_name_plural = "Sneakers"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Sneaker_detail", kwargs={"pk": self.pk})


# class ImageModel(models.Model):
#     img = models.ImageField()
#     # name ...




# CODE FOR IMAGES 
# class Item(models.Model):
#     image_file = models.ImageField(upload_to='images')
#     image_url = models.URLField()

# ...

# def get_remote_image(self):
#     if self.image_url and not self.image_file:
#         result = urllib.urlretrieve(self.image_url)
#         self.image_file.save(
#                 os.path.basename(self.image_url),
#                 File(open(result[0]))
#                 )
#         self.save()