class Model:
    def validate(self):
        return True

    def save(self):
        if self.validate():
            print(f"[{self.__class__.__name__}]: Данные прошли валидацию и сохранены.")
        else:
            pass

class User(Model):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def validate(self):
        if not self.username:
            print(f"[{self.__class__.__name__}]: Ошибка: имя не может быть пустым")
            return False
        if "@" not in self.email:
            print(f"[{self.__class__.__name__}]: Ошибка: некорректный email")
            return False
        return True

class Product(Model):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def validate(self):
        if self.price < 0:
            print(f"[{self.__class__.__name__}]: Ошибка: цена должна быть положительной")
            return False
        return True

valid_user = User("Мария", "maria@example.com")
invalid_user = User("", "invalid-email")

valid_product = Product("Телефон", 20000)
invalid_product = Product("Битая ссылка", -1)

valid_user.save()
invalid_user.save()
valid_product.save()
invalid_product.save()
