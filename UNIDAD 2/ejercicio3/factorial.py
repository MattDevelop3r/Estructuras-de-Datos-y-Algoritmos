from classPilaEncadenada import Pila

def factorial():
    num = int(input("Ingrese un número decimal: "))
    res = 1
    aux = num
    pila = Pila()
    while aux != 0:
        pila.insertar(aux)
        aux -= 1 
    while not pila.vacia():
        res *= pila.suprimir()

    print(f"El factorial de {num} es {res}")
    
if __name__ == "__main__":
    ans = ""
    while ans != "no":
        factorial()
        ans = ""
        while ans != "si" and ans != "no":
            ans = input("\nQuiere realizar otro factorial? SI - NO: ").lower() 