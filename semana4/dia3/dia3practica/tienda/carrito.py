class Cart:
    def __init__(self,request):
        # recibe los datos enviados
        self.request = request
        # session esta dentro de request
        self.session = request.session
        # session se almacena en cart
        cart = self.session.get("cart")
        # si no hay carrito lo crea
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
        
    def add(self, producto,qty):
        # si el producto no se encuentra lo crea 
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": qty,                
                "precio": str(producto.precio),
                "imagen": producto.imagen.url,
                "total": str(qty * producto.precio)
            }
        # si existe el producto se le suma 1
        else:
            for key,value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = str(int(value["cantidad"]) + qty)
                    value["total"] = str((float(value["cantidad"])) * float(value["precio"]))
                    break
        self.save()
        
    def save(self):
        self.session["cart"] = self.cart
        # para modificarlo
        self.session.modified = True
        
    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
            
    def clear(self):
        self.session["cart"] = {}