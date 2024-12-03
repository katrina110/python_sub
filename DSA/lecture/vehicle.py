class Car:
    def __init__(self, color, model, brand):
        self._color = color
        self._model = model
        self._brand = brand

    # Getter for color
    # @property
    def getColor(self):
        return self._color

    # Setter for color
    # @color.setter
    def setColor(self, value):
        self._color = value

    # Getter for model
    @property
    def model(self):
        return self._model

    # Setter for model
    @model.setter
    def model(self, value):
        self._model = value

    # Getter for brand
    @property
    def brand(self):
        return self._brand

    # Setter for brand
    @brand.setter
    def brand(self, value):
        self._brand = value

# # Example usage
# car = Car("Red", "Sedan", "Toyota")
# print(car.color)  # Red
# car.color = "Blue"
# print(car.color)  # Blue
