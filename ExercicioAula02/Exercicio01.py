def exercicio1_calcular_desconto(valor):
    if valor < 0:
        return None, "Valor inválido. O valor não pode ser menor que zero."
    elif valor >= 1000:
        desconto = 0.08
    elif valor >= 500:
        desconto = 0.07
    elif valor >= 200:
        desconto = 0.06
    elif valor >= 50:
        desconto = 0.05
    else:
        desconto = 0.0

    valor_com_desconto = valor * (1 - desconto)
    return valor_com_desconto, None

def main():
    nome_produto = input("Digite o nome do produto: ")
    valor_produto = float(input("Digite o valor do produto: "))

    valor_com_desconto, erro = exercicio1_calcular_desconto(valor_produto)

    if erro:
        print(erro)
    else:
        print(f"Produto: {nome_produto}")
        print(f"Valor original: R$ {valor_produto:.2f}")
        print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")

if __name__ == "__main__":
    main()
    