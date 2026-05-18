class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough"]

    def display_flavors(self):
        print("Ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_icecream_stand = IceCreamStand("Sweet Treats", "Ice Cream")

my_icecream_stand.display_flavors()