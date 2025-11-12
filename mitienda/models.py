from django.db import models
from django.urls import reverse

#modelo para almacenar las categorias de los productos
class Categoria(models.Model):
    name = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)

    class Meta:
        ordering=['name']
        indexes = [
            models.Index(fields=['name']), #sirve en gestores de bases de datos para mejorar la velocidad de las consultas
        ]

    def __str__(self):
        return self.name
    
    #la funcion get_absolute_url devuelve la URL canónica para un objeto dado
    def get_absolute_url(self):
        return reverse('tienda:product_list_category', args=[self.slug])

#modelo para almacenar los productos
class Producto(models.Model):
    category = models.ForeignKey(Categoria, related_name='products', on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tienda:product_detail', args=[self.id, self.slug])
    