class Human:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age
    
  def check_age(self, age):
    if age >= 18:
      print(f"{self.name.title()} {self.surname.title()} is old enough to work.")
    else:
      print(f"{self.name.title()} {self.surname.title()} is a minor.")
  
human = Human('mvano', 'mgam', 20)
human.check_age(20)