from classPilaEncadenada import Pila

def conversion(pila):
    num = int(input("Ingrese un número decimal: "))
    while num != 0:
        resto = num % 2
        if num > 0:
            num = num // 2
        else:
            num = -(num // 2)
        pila.insertar(int(resto))

    print("\nEL RESULTADO EN BINARIO ES: ")
    while not pila.vacia():
        print(pila.suprimir(), end="")
    print() 

if __name__ == "__main__":
    pila = Pila()
    ans = ""
    while ans != "no":
        conversion(pila)
        ans = ""
        while ans != "si" and ans != "no":
            ans = input("\nQuiere realizar otra conversion? SI - NO: ").lower()
        if ans == "si":
            while not pila.vacia():
                pila.suprimir()
        

