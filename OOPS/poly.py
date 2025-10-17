class family:
    def color(self):
      return " something color is found"
    def hair (self):
      return "something hair is found"
    def height(self):
      return "something height is found"
    def weight(self):
      return "something weight is found"
class mother(family):
    def color(self):
      return "white"
    def hair(self):
      return "long"
    def height(self):
      return "tall"
    def weight(self):
       return "heavy"
class daughter(family):
    def color(self):
      return "black"
    def hair(self):
       return "short"
    def height(self):
       return "short"
    def weight(self):
       return "light"
families=[mother(),daughter()]
for member in families:
   print(member.color())
   print(member.hair())   
   print(member.height())
   print(member.weight())
