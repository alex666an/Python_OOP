from typing import List
from project.dvd import DVD

class Customer:

    def __init__(self, name, age, _id):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({', '.join(d.name for d in self.rented_dvds)})")


