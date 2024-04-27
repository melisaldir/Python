a = 0
def selamla():
    global a 
    a += 1
    print("merhaba",a)
    print("nasılsın\n")
    if a != 3 : selamla()

selamla()