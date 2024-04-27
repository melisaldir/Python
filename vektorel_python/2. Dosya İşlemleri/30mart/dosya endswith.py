import os
liste = os.listdir()
for a in liste:
    if a.endswith(".xx"):
        print(a)
        os.remove(a)