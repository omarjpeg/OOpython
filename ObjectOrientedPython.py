class EstateDeveloper:
    """
    A class to represent an Estate Development company that keeps track of it's built properties

    Attributes:
        name(str): Name of the agency's instance
        address(str): Address of the agency's instance
        __property_list(list): List of the agency's properties, stored as Building objects


    """

    def __init__(self, name: str, address: str):
        """
        Initialization method for an agency

        :param name: Name of this agency's instance
        :param address: Address of this agency's instance
        """
        self.name = name
        self.address = address
        self.__property_list = []

    def _add_property(self, estate_property):
        """
        A method which adds a property to the instance's name, recording it in the list of properties the estate
        developer owns

        :param estate_property: The Building object you want to add to the list of properties the estate developer owns
        """
        self.__property_list.append(estate_property)

    def remove_property(self, estate_property):
        """
        A method which removes a property from the instance's name, removing it from the list of properties the estate
        developer owns

        :param estate_property: The Building object you want to remove from the list of properties the estate
        developer owns
        """
        if estate_property in self.__property_list:
            self.__property_list.remove(estate_property)


class Building:
    """
    A class to represent a generic building as a base class, meant to be inherited from

    Attributes:
        address: Address of a building's instance
        number_of_floors: The number of floors of this instance of a building
        type: Type of building, either commercial or personal
        estate_developer: The estate developer responsible for the construction of said building's instance

    """

    def __init__(self, address: str, number_of_floors: int, property_type: str, estate_developer: EstateDeveloper):
        """
        Initialization method for the base class building, this method automatically adds the building to the estate
        developer's list of property

        :param address: Address of a building's instance
        :param number_of_floors: The number of floors of this instance of a building
        :param property_type: Type of building, either commercial or personal
        :param estate_developer: The estate developer responsible for the construction of said building's instance
        """
        self.address = address
        self.number_of_floors = number_of_floors
        self.type = property_type
        self.estate_developer = estate_developer
        estate_developer._add_property(self)

    def get_address(self):
        """
        A method that returns the address of the building in str format

        """
        return self.address


class House(Building):
    """
    A class to represent an average house, this class inherits from the building class

    Attributes:
        address(str): Address of this house's instance
        width(float): Width of this house's instance
        length(float): Length of this house's instance
        paint_color(str): Color of the paint applied to this house
        estate_developer(EstateDeveloper): The estate developement company that built this house
    """

    def __init__(self, address: str, width: float, length: float, paint_color: str, estate_developer: EstateDeveloper):
        """
        House initialization method that takes house address, width, length, paint color and estate developer and associates them with created instance

        :param address: Address of this house's instance
        :param width: Width of this house's instance
        :param length: Length of this house's instance
        :param paint_color: Color of the paint applied to this house
        :param estate_developer: The estate developement company that built this house
        """
        super().__init__(address=address, number_of_floors=1, property_type="Personal",
                         estate_developer=estate_developer)
        self.width = width
        self.length = length
        self._paint_color = paint_color
        self.__shape = "Long" if length > width else "Rectangular"
        self.__furniture_list = []
        self.occupied = False

    def add_furniture(self, piece: str):
        """
        Adds name of piece of furniture passed as a string to the list of furniture in this instance of the house

        :param piece: Name of object to be added
        :return: None 
        """
        self.__furniture_list.append(piece)

    def remove_furniture(self, piece: str):
        """
        Adds name of piece of furniture passed as a string to the list of furniture in this instance of the house

        :param piece: Name of object to be added
        :return: None
        """
        if piece in self.__furniture_list:
            self.__furniture_list.remove(piece)
        else:
            "This house does not have this piece of  furniture"

    def get_furniture_list(self):
        """
        A getter function that return a copy of the list of furniture to enforce mutability only through add and
        remove furniture methods

        :return: A copy of the current furniture string objects that are held in by this instance of a house in the
        form of a list
        """
        return self.__furniture_list.copy()

    def get_shape(self):
        """
        A getter function that return a string of the current shape of this house according to it's provided initial
        dimensions

        :return: The shape of this house, either rectangular or long in the form of a string
        """
        return self.__shape

    def _set_paint_color(self, paint_color: str):
        """
        A private method that sets the instance's paint color with the color passed to it, made to be used with a property

        """

        self._paint_color = paint_color.capitalize()

    def _get_paint_color(self):
        """
        A private method that gets the instance's paint color, made to be used with a property

        :return: The instance's paint color attribute
        """
        return self._paint_color

    def _remove_paint_color(self):
        """
        A private method that deletes the instance's paint color and defaults it to value indicating a non painted
        state, made to be used with a property

        """
        self._paint_color = "Bare Bricks / To be painted"

    def __str__(self):
        """
        An overriding str method to the object superclass to print information about a particular instance of a house
        in a nicer manner

        :return: A string representing information about the house instance

        """
        return f"A house  with the dimensions {self.width} by {self.length} , with {len(self.__furniture_list)} " \
               f"pieces of furniture in it. It's walls are {self.paint_color} "

    def set_house_occupied_status(self, status: bool):
        """
        A method to change the current occupation status of the current instance of the class 'House'

        :param status: A boolean variable to set as the current occupation status of this instance of a house

        """
        self.occupied = status

    def get_address(self):
        """
        A method that returns the house's instance's address
        """
        return "House at " + super().get_address() + "built by {0.name}".format(self.estate_developer)

    paint_color = property(_get_paint_color, _set_paint_color, _remove_paint_color)


class SkyScraper(Building):
    """
    A class to represent an average commercial skyscraper, this class inherits from the building superclass

    Attributes:
        address(str): Address of this skyscraper's instance
        height(float): Height of this skycraper's instance
        number_of_floors(int): Number of floors in this skyscraper
        estate_developer(EstateDeveloper): The estate development company that built this skyscraper
    """

    def __init__(self, height: float, address: str, number_of_floors: int, estate_developer: EstateDeveloper):
        """
        An initialization method for the skyscraper class

        :param height: Height of this skycraper's instance
        :param address: Address of this skyscraper's instance
        :param number_of_floors: Number of floors in this skyscraper
        :param estate_developer: The estate development company that built this skyscraper
        """
        super().__init__(address, number_of_floors, "Commercial", estate_developer)
        self.height = height

    def get_address(self):
        """
        A method that returns the skyscraper's instance's address


        """
        return "Skyscraper at " + super().get_address() + "built by {0.name}".format(self.estate_developer)


