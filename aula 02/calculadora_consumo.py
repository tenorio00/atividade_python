# Calculadora de Consumo de Combustível

distancia = 300  # km
combustivel_gasto = 25  # litros

consumo_medio = distancia / combustivel_gasto

print("\nDados da viagem:")
print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel_gasto, "litros")
print("Consumo médio: {:.2f} km/l".format(consumo_medio))