from dataclasses import dataclass


@dataclass
class User:
    """
    User model representing a user in the application.
    Currently, it only contains a name attribute.
    It could be extended to include more user-related information in the future (like e-mail and other profile information).
    """
    name: str

    """
    Returns a string representation of the User object.
    This method is called whenever a User object is printed or converted to a string.
    e.g. print(user) or str(user).
    """
    def __str__(self):
        return self.name
