class Restaurnat:
    def __init__(self, Resturnat_name, cusisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurnat(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print()

restaurnat1 = Restaurnat("Tbilisi xinkali house", "Georgian")
restaurnat2 = Restaurnat("Tokyo Sushi", "Japanese")
restaurnat3 = Restaurnat("Rome Pasta House", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

