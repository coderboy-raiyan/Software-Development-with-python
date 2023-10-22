import abc


class User(abc.ABC):
    def __init__(self, name, email, phone_number) -> None:
        self.name = name
        self.email = email
        self.phone_number = phone_number

    @abc.abstractmethod
    def display_profile():
        raise NotImplementedError


class Cook(User):
    def __init__(self, name, email, phone_number, nid, address, experience) -> None:
        super().__init__(name, email, phone_number)
        self.__id = 0
        self.__nid = nid
        self.address = address
        self.expertise = "beginner"
        self.experience = experience
