def Dict():
    passwords = {}
    ef = open("data/data.csv", 'r')
    a = ef.read()
    b = a.split("\n")
    for k in b:
        e = k.split(",")
        try:
            passwords[e[0]] = e[1]
        except:
            return passwords
    return passwords

def add(username, password):
    fileopener= open("data/data.csv", "a")
    fileopener.write(str(username) +','+ str(password) + "\n")
    fileopener.close()
