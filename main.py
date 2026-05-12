def main():
    print("Hello from demp!")


if __name__ == "__main__":
    main()


num1 = float(input("Qual seu numero preferido? "))
num2 = float(input("Digite um numero aleatorio: "))

print(f"Seu numero preferido é {num1} e seu numero aletario é {num2}")

print(f"Agora escolha uma função para fazer um cálculo dos seus número: ")


def soma( a: float, b:  float) -> float:

   return a + b

def subtracacao( a: float, b: float) -> float:

    return a - b 

def multiplicacao( a: float, b: float) -> float:

    return a * b

def divisao( a: float, b: float) -> float:
    
    return a / b


def menu() -> none:

    print(" ----MENU---- ")
    print("(1) SOMA")
    print("(2) SUBTRAÇÃO")
    print("(3) MULTIPLICAÇÃO")
    print("(4) DIVISÃO")


while True:



option = input("Informe uma opção: ")

if option == "1"

a = float(input("Informe o valor de (a):"))
b = float(input("Informe um valor de (b):"))

       print("Saída de soma:", soma(a, b))
