from decimal import Decimal
from django.conf import settings
from mitienda.models import Producto
class Cart:
    #Inicializa el carrito de compras
    def __init__(self, request):
        self.session = request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
    #Este metodo agrega un producto al carrito o actualiza su cantidad
    def add(self,product,quantity=1,override_quantity=False):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0, 'price':str(product.price)}
        if override_quantity:
            self.cart[product_id][quantity]=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.save()
    #Este metodo guarda el carrito en la sesion
    def save(self):
        # Guarda el carrito en la sesión
        self.session.modified=True
    #Este metodo elimina un producto del carrito
    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    #este metodo itera sobre los elementos del carrito y obtiene los productos de la base de datos
    def __iter__(self):
        products_ids=self.cart.keys()
        products = Producto.objects.filter(id__in=products_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        # Es el conteo total de cada producto
        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price']*item['quantity']
            yield item
    #este metodo devuelve el numero total de articulos en el carrito        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    #costo total del carrito
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    # Vaciar el carrito
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()