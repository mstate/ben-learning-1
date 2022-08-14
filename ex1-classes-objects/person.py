class Person:
  def __init__(self, passed_in_name, passed_in_age):
    print(passed_in_age)
    self.name = passed_in_name
    self.age = 12
    self.friends = []

  def sayHi(self):
    print(f"Hello my name is {self.name} and I'm {self.age} years old")

  def ageOneYear(self):
    self.age += 1

  def makeFriendsWith(self, passed_in_friend_name):
    self.friends.append(passed_in_friend_name)

  def printFriends(self):
    print("My friends are: ")
    print(", ".join(self.friends))
  