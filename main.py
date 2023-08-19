class Ten_Multi:

  def __init__(self, v):
    self.value = v

  def see(self):
    print(f"Value is {self.value}")

  @property  # property is used for GETTERS
  def action(self):
    # print(f"{self.value} * 10 = {10 * self.value}")
    return 10 * self.value

  @action.setter  # .setter is used for SETTERS
  def action(self, newv):
    self.value = newv / 10


a = Ten_Multi(67)
# a.action()
a.action = 14
print(a.action)
a.see()