# Exercise N1
#
# import json
#
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __repr__(self):
#         return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "price": self.price,
#             "quantity": self.quantity
#         }
#
#     @staticmethod
#     def from_dict(data):
#         return Product(data["name"], data["price"], data["quantity"])
#
#
# products = [
#     Product("Laptop", 1200, 10),
#     Product("Smartphone", 800, 20),
#     Product("Headphones", 100, 50)
# ]
#
#
# file_name = "products.json"
# with open(file_name, "w") as file:
#     json.dump([product.to_dict() for product in products], file, indent=4)
#
# with open(file_name, "r") as file:
#     data = json.load(file)
#     deserialized_products = [Product.from_dict(item) for item in data]
#
# for product in deserialized_products:
#     print(product)
#
#

# Exercise N2

# import json
#
# file_name = "movies.json"
#
# with open(file_name, "r") as file:
#     movies = json.load(file)
#
# updated_movies = []
#
# for movie in movies:
#     year = movie.get("release_year", 0)
#     genre = movie.get("genre", "")
#
#     if year > 2000 and "Crime" in genre:
#         movie["genre"] = genre.replace("Crime", "New_Crime")
#         updated_movies.append(movie)
#
#     elif year < 2000 and "Drama" in genre:
#         movie["genre"] = genre.replace("Drama", "Old_Drama")
#         updated_movies.append(movie)
#
#     elif year == 2000:
#         movie["genre"] += " New_Century"
#         updated_movies.append(movie)
#
# with open(file_name, "w") as file:
#     json.dump(updated_movies, file, indent=4)
#
# print("Finished!")
