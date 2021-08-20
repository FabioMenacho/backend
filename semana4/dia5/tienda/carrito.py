class Cart:
    def __init__(self,request):
        self.request = request
        # session esta dentro de request
        self.session = request.session
        # consulta la session y almacena en cart el objeto cart q tiene
        cart = self.session.get("cart")
        # si no hay carrito almacena la session en cart y crea carrito vacio
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
        
    def add(self, producto,qty):
        # si el producto no se encuentra lo crea 
        if str(producto.id) not in self.cart.keys():
            # cart es el objeto, producto.id el key y lo q esta dentro es el value
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": qty,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url,
                "total": str(qty * producto.precio)
            }
        # si existe el producto se actualiza la cantidad y el total
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