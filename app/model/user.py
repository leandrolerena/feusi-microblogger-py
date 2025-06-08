from dataclasses import dataclass


@dataclass
class User:
    name: str

    def __str__(self):
        return self.name
