def exercicio2_calcular_resistencias(resistencias):
    resistencia_equivalente = sum(resistencias)
    maior_resistencia = max(resistencias)
    menor_resistencia = min(resistencias)
    return resistencia_equivalente, maior_resistencia, menor_resistencia

def main():
    resistencias = []
    for i in range(4):
        resistencia = float(input(f"Digite o valor da resistência {i+1}: "))
        resistencias.append(resistencia)

    resistencia_equivalente, maior_resistencia, menor_resistencia = exercicio2_calcular_resistencias(resistencias)

    print(f"Resistências fornecidas: {resistencias}")
    print(f"Resistência equivalente: {resistencia_equivalente} Ω")
    print(f"Maior resistência: {maior_resistencia} Ω")
    print(f"Menor resistência: {menor_resistencia} Ω")

if __name__ == "__main__":
    main()
    
