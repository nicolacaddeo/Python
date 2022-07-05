print("================================")
print("CALCOLATRICE DI SERIE B")
print("================================")

continua = True

while continua:

    x = input("Primo numero: ")
    y = input("Secondo numero: ")
    op = input("Scegli l'operatore [+, -, *, /]")



    # Controllo dati
    res = 0
    if not (x.isdigit() and y.isdigit() and (op == "+" or op == "-" or op == "*" or op == "/")):
        print("Dati errati")
        continue;

    # Cast
    x = int(x)
    y = int(y)

    if op == "+":
        res = x+y

    if op == "-":
        res = x-y

    if op == "*":
        res = x*y

    if op == "/":
        res =  x/y

    print("Il risultato e': ", res)       
    cont_risp = input("Vuoi continuare (y per dire sì)\n") 
    keep = cont_risp =="y"

