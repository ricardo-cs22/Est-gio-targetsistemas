import json

def calcular_faturamento(faturamento_diario):

    dias_validos = [entrada['valor'] for entrada in faturamento_diario if entrada['valor'] > 0]
    
   
    menor_faturamento = min(dias_validos) if dias_validos else 0
    maior_faturamento = max(dias_validos) if dias_validos else 0
    

    media_mensal = sum(dias_validos) / len(dias_validos) if dias_validos else 0
    
 
    dias_acima_media = sum(1 for valor in dias_validos if valor > media_mensal)
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }


def carregar_dados(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

# Exemplo de uso
faturamento_diario = carregar_dados('dados.json')
resultado = calcular_faturamento(faturamento_diario)

print("Menor faturamento:", resultado["menor_faturamento"])
print("Maior faturamento:", resultado["maior_faturamento"])
print("Dias acima da média mensal:", resultado["dias_acima_media"])
