# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a função saudade:")
saudacao("Alice")
saudacao("Bob")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da função quadrado: ",resultado_quadrado)

# Função com multiplos parametros
def soma(numero1,numero2):
    resultado = numero1 + numero2
    return resultado

print("\n Chamando a função soma:")
numero1 = 25
numero2 = 30
resultado_soma = soma(numero1,numero2)
print("A soma do número %s e número %s é %s" % (numero1,numero2,resultado_soma))