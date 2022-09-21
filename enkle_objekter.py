""" rectangle = {
    "width": 3,
    "length": 5,
    "color": "blue"
}

def rectangle_area(rectangle):
    area = rectangle["width"] * rectangle["length"]
    return area

rectangle["width"] = 10
print(rectangle["color"])
print(rectangle_area(rectangle))  """


class Rectangle:
    width = 3
    length = 5
    color = "blue" 

    def area(self):
        area = self.width * self.length
        return area


rectangle = Rectangle()

print(rectangle.color) 

rectangle.width = 4
rectangle.length = 10
print(rectangle.area())


# class Rectangle:

#     def __init__(self, width, length, color):

#         self.width = width
#         self.length = length
#         self.color = color

#     def area(self):
#         area = self.width * self.length
#         return area
        

# rectangle = Rectangle(3,5, "blue")

# print(rectangle.color)

# print(rectangle.area())