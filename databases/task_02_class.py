class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.price * self.qty

    def info(self):
        total_cost = self.total()
        return f"{self.name}: {self.price} × {self.qty} = {total_cost} руб."


# Создаём 3 объекта
sneakers = Product("Кроссовки", 8500, 3)
boots = Product("Ботинки", 15000, 1)
shoes = Product("Туфли", 12000, 5)

# Выводим информацию о каждом
print(sneakers.info())
print(boots.info())
print(shoes.info())
