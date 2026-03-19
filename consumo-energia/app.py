print(" Calculadora de Consumo Elétrico ⚡  ")

aparelho = input("Digite o nome do aparelho elétrico: ")
potencia = float(input("Digite a potência do aparelho em (W): "))
horas_dia = float(input("Digite o tempo médio de uso por dia (horas): "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

valor_kwh = 0.75
custo = consumo_mensal * valor_kwh

print("\n Resultado 📊")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}")
