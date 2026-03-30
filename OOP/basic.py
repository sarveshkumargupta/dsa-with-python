
class Members:
    def __init__(self, name, age, weight, join_date):
        self.name = name
        self._age = age
        self.weight = weight
        self.join_data = join_date

    @classmethod
    def create_trainer(cls, name):
        return cls(name, "NA", "NA", "NA")

    @staticmethod
    def min_age(age):
        return "Not Allowed" if age < 18 else "Allowed"

    def __repr__(self):
        return f"Name: {self.name} and Age: {self._age}"

    # Getter
    @property
    def age(self):
        return f"Age: {self._age}"

    # Setter
    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Age must be greater than 18.")
        self._age = age


member1 = Members("Nilesh", 26, 72, "29/03/2026")

print(member1)

member1.age = 20

print(member1)


