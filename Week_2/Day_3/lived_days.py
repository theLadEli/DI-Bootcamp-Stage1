from datetime import date
class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    @property   # Getter
    def birthday(self):
        return(self._birthday)
    
    @birthday.setter    # Setter
    def birthday(self, value):
        if not isinstance(value, date):
            raise ValueError('Birthday argument has to be a datetime object.')
        self._birthday = value

    def lived_days(self):
        return(date.today() - self.birthday).days

        
# p1 = Person('Eli Cohen', date(2006,3,6))
p1 = Person('Eli Cohen', '2006/03/06')
print(p1.birthday)
print(p1.lived_days())