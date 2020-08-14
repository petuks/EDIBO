class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)
print("Before an = PartyAnimal()")
print(vars())
an = PartyAnimal()
print("After an = PartyAnimal()")
print(vars())
print("\nBefore first an.party()")
an.party()
print("After first an.party()")
print("\nBefore second an.party()")
an.party()
print("After second an.party")
print("\nBefore third an.party()")
an.party()
print("After third an.party()")
print("\nBefore one more party()")
PartyAnimal.party(an)
print("After one more party()")

# Code: http://www.py4e.com/code3/party2.py
