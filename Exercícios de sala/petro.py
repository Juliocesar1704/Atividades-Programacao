import matplotlib.pyplot as plt
import json

petrobras = [
  {
    "DATA": "31/01/2025",
    "ABERTURA": "37,39",
    "FECHAMENTO": "37,69",
    "VARIAÇÃO": "0,80",
    "MÍNIMO": "37,66",
    "MÁXIMO": "37,78",
    "VOLUME": "2,46B"
  },
  {
    "DATA": "30/01/2025",
    "ABERTURA": "37,20",
    "FECHAMENTO": "37,39",
    "VARIAÇÃO": "1,33",
    "MÍNIMO": "36,80",
    "MÁXIMO": "37,51",
    "VOLUME": "1,74B"
  },
  {
    "DATA": "29/01/2025",
    "ABERTURA": "37,40",
    "FECHAMENTO": "36,90",
    "VARIAÇÃO": "-0,62",
    "MÍNIMO": "36,76",
    "MÁXIMO": "37,33",
    "VOLUME": "1,61B"
  },
  {
    "DATA": "28/01/2025",
    "ABERTURA": "36,57",
    "FECHAMENTO": "37,13",
    "VARIAÇÃO": "-0,13",
    "MÍNIMO": "36,88",
    "MÁXIMO": "37,49",
    "VOLUME": "2,07B"
  },
  {
    "DATA": "27/01/2025",
    "ABERTURA": "36,57",
    "FECHAMENTO": "37,18",
    "VARIAÇÃO": "1,47",
    "MÍNIMO": "36,47",
    "MÁXIMO": "37,30",
    "VOLUME": "995,73M"
  },
  {
    "DATA": "24/01/2025",
    "ABERTURA": "37,12",
    "FECHAMENTO": "36,64",
    "VARIAÇÃO": "-0,52",
    "MÍNIMO": "36,40",
    "MÁXIMO": "36,90",
    "VOLUME": "1,50B"
  },
  {
    "DATA": "23/01/2025",
    "ABERTURA": "37,36",
    "FECHAMENTO": "36,83",
    "VARIAÇÃO": "-0,70",
    "MÍNIMO": "36,70",
    "MÁXIMO": "37,41",
    "VOLUME": "1,68B"
  },
  {
    "DATA": "22/01/2025",
    "ABERTURA": "37,10",
    "FECHAMENTO": "37,09",
    "VARIAÇÃO": "-0,56",
    "MÍNIMO": "37,03",
    "MÁXIMO": "37,63",
    "VOLUME": "1,58B"
  },
  {
    "DATA": "21/01/2025",
    "ABERTURA": "37,22",
    "FECHAMENTO": "37,30",
    "VARIAÇÃO": "0,03",
    "MÍNIMO": "36,72",
    "MÁXIMO": "37,35",
    "VOLUME": "1,32B"
  },
  {
    "DATA": "20/01/2025",
    "ABERTURA": "37,22",
    "FECHAMENTO": "37,29",
    "VARIAÇÃO": "0,24",
    "MÍNIMO": "37,11",
    "MÁXIMO": "37,43",
    "VOLUME": "467,58M"
  },
  {
    "DATA": "17/01/2025",
    "ABERTURA": "37,21",
    "FECHAMENTO": "37,20",
    "VARIAÇÃO": "0,54",
    "MÍNIMO": "36,85",
    "MÁXIMO": "37,40",
    "VOLUME": "1,88B"
  },
  {
    "DATA": "16/01/2025",
    "ABERTURA": "36,93",
    "FECHAMENTO": "37,00",
    "VARIAÇÃO": "-0,78",
    "MÍNIMO": "36,77",
    "MÁXIMO": "37,24",
    "VOLUME": "2,07B"
  },
  {
    "DATA": "15/01/2025",
    "ABERTURA": "36,93",
    "FECHAMENTO": "37,29",
    "VARIAÇÃO": "1,28",
    "MÍNIMO": "36,80",
    "MÁXIMO": "37,32",
    "VOLUME": "2,15B"
  },
  {
    "DATA": "14/01/2025",
    "ABERTURA": "37,11",
    "FECHAMENTO": "36,82",
    "VARIAÇÃO": "-0,67",
    "MÍNIMO": "36,58",
    "MÁXIMO": "37,13",
    "VOLUME": "1,76B"
  },
  {
    "DATA": "13/01/2025",
    "ABERTURA": "37,30",
    "FECHAMENTO": "37,07",
    "VARIAÇÃO": "0,35",
    "MÍNIMO": "36,97",
    "MÁXIMO": "37,53",
    "VOLUME": "756,85M"
  },
  {
    "DATA": "10/01/2025",
    "ABERTURA": "36,70",
    "FECHAMENTO": "36,94",
    "VARIAÇÃO": "0,27",
    "MÍNIMO": "36,90",
    "MÁXIMO": "37,52",
    "VOLUME": "1,82B"
  },
  {
    "DATA": "09/01/2025",
    "ABERTURA": "36,99",
    "FECHAMENTO": "36,84",
    "VARIAÇÃO": "0,44",
    "MÍNIMO": "36,70",
    "MÁXIMO": "36,97",
    "VOLUME": "1,27B"
  },
  {
    "DATA": "08/01/2025",
    "ABERTURA": "36,55",
    "FECHAMENTO": "36,68",
    "VARIAÇÃO": "-0,81",
    "MÍNIMO": "36,43",
    "MÁXIMO": "37,12",
    "VOLUME": "2,18B"
  },
  {
    "DATA": "07/01/2025",
    "ABERTURA": "36,55",
    "FECHAMENTO": "36,98",
    "VARIAÇÃO": "2,13",
    "MÍNIMO": "36,30",
    "MÁXIMO": "37,18",
    "VOLUME": "2,13B"
  },
  {
    "DATA": "06/01/2025",
    "ABERTURA": "36,60",
    "FECHAMENTO": "36,21",
    "VARIAÇÃO": "-0,47",
    "MÍNIMO": "36,06",
    "MÁXIMO": "36,28",
    "VOLUME": "837,87M"
  },
  {
    "DATA": "03/01/2025",
    "ABERTURA": "36,42",
    "FECHAMENTO": "36,38",
    "VARIAÇÃO": "-1,06",
    "MÍNIMO": "36,33",
    "MÁXIMO": "37,04",
    "VOLUME": "1,81B"
  },
  {
    "DATA": "02/01/2025",
    "ABERTURA": "35,78",
    "FECHAMENTO": "36,77",
    "VARIAÇÃO": "1,60",
    "MÍNIMO": "36,19",
    "MÁXIMO": "37,09",
    "VOLUME": "1,78B"
  },
  {
    "DATA": "30/12/2024",
    "ABERTURA": "35,78",
    "FECHAMENTO": "36,19",
    "VARIAÇÃO": "1,49",
    "MÍNIMO": "35,77",
    "MÁXIMO": "36,37",
    "VOLUME": "703,99M"
  },
  {
    "DATA": "27/12/2024",
    "ABERTURA": "35,63",
    "FECHAMENTO": "35,66",
    "VARIAÇÃO": "-0,31",
    "MÍNIMO": "35,61",
    "MÁXIMO": "36,00",
    "VOLUME": "1,59B"
  },
  {
    "DATA": "26/12/2024",
    "ABERTURA": "n/d",
    "FECHAMENTO": "35,77",
    "VARIAÇÃO": "0,39",
    "MÍNIMO": "35,60",
    "MÁXIMO": "36,00",
    "VOLUME": "700,93M"
  },
  {
    "DATA": "23/12/2024",
    "ABERTURA": "n/d",
    "FECHAMENTO": "35,63",
    "VARIAÇÃO": "0,03",
    "MÍNIMO": "35,49",
    "MÁXIMO": "35,81",
    "VOLUME": "1,22B"
  },
  {
    "DATA": "20/12/2024",
    "ABERTURA": "36,40",
    "FECHAMENTO": "35,62",
    "VARIAÇÃO": "-0,83",
    "MÍNIMO": "35,49",
    "MÁXIMO": "36,10",
    "VOLUME": "2,66B"
  },
  {
    "DATA": "19/12/2024",
    "ABERTURA": "37,00",
    "FECHAMENTO": "35,92",
    "VARIAÇÃO": "-0,75",
    "MÍNIMO": "35,75",
    "MÁXIMO": "36,66",
    "VOLUME": "3,55B"
  },
  {
    "DATA": "18/12/2024",
    "ABERTURA": "36,67",
    "FECHAMENTO": "36,19",
    "VARIAÇÃO": "-2,25",
    "MÍNIMO": "36,10",
    "MÁXIMO": "37,12",
    "VOLUME": "3,18B"
  },
  {
    "DATA": "17/12/2024",
    "ABERTURA": "36,92",
    "FECHAMENTO": "37,02",
    "VARIAÇÃO": "0,95",
    "MÍNIMO": "36,57",
    "MÁXIMO": "37,21",
    "VOLUME": "2,07B"
  },
  {
    "DATA": "16/12/2024",
    "ABERTURA": "36,92",
    "FECHAMENTO": "36,67",
    "VARIAÇÃO": "-0,42",
    "MÍNIMO": "36,57",
    "MÁXIMO": "36,98",
    "VOLUME": "641,77M"
  },
  {
    "DATA": "13/12/2024",
    "ABERTURA": "37,31",
    "FECHAMENTO": "36,83",
    "VARIAÇÃO": "-0,63",
    "MÍNIMO": "36,74",
    "MÁXIMO": "36,83",
    "VOLUME": "2,19B"
  },
  {
    "DATA": "12/12/2024",
    "ABERTURA": "37,43",
    "FECHAMENTO": "37,06",
    "VARIAÇÃO": "-1,79",
    "MÍNIMO": "36,86",
    "MÁXIMO": "37,16",
    "VOLUME": "1,30B"
  },
  {
    "DATA": "11/12/2024",
    "ABERTURA": "37,51",
    "FECHAMENTO": "37,74",
    "VARIAÇÃO": "1,00",
    "MÍNIMO": "37,14",
    "MÁXIMO": "37,90",
    "VOLUME": "1,76B"
  },
  {
    "DATA": "10/12/2024",
    "ABERTURA": "36,61",
    "FECHAMENTO": "37,37",
    "VARIAÇÃO": "0,37",
    "MÍNIMO": "37,29",
    "MÁXIMO": "37,59",
    "VOLUME": "1,70B"
  },
  {
    "DATA": "09/12/2024",
    "ABERTURA": "36,61",
    "FECHAMENTO": "37,23",
    "VARIAÇÃO": "2,59",
    "MÍNIMO": "36,60",
    "MÁXIMO": "37,35",
    "VOLUME": "927,99M"
  },
  {
    "DATA": "06/12/2024",
    "ABERTURA": "36,62",
    "FECHAMENTO": "36,29",
    "VARIAÇÃO": "-1,54",
    "MÍNIMO": "36,22",
    "MÁXIMO": "36,91",
    "VOLUME": "1,97B"
  },
  {
    "DATA": "05/12/2024",
    "ABERTURA": "36,72",
    "FECHAMENTO": "36,85",
    "VARIAÇÃO": "0,99",
    "MÍNIMO": "36,45",
    "MÁXIMO": "37,01",
    "VOLUME": "2,01B"
  },
  {
    "DATA": "04/12/2024",
    "ABERTURA": "36,63",
    "FECHAMENTO": "36,49",
    "VARIAÇÃO": "-0,63",
    "MÍNIMO": "36,25",
    "MÁXIMO": "37,06",
    "VOLUME": "1,87B"
  },
  {
    "DATA": "03/12/2024",
    "ABERTURA": "36,17",
    "FECHAMENTO": "36,72",
    "VARIAÇÃO": "0,89",
    "MÍNIMO": "36,33",
    "MÁXIMO": "36,72",
    "VOLUME": "1,83B"
  },
  {
    "DATA": "02/12/2024",
    "ABERTURA": "36,17",
    "FECHAMENTO": "36,40",
    "VARIAÇÃO": "0,64",
    "MÍNIMO": "36,05",
    "MÁXIMO": "36,63",
    "VOLUME": "1,07B"
  },
  {
    "DATA": "29/11/2024",
    "ABERTURA": "35,79",
    "FECHAMENTO": "36,17",
    "VARIAÇÃO": "0,80",
    "MÍNIMO": "36,00",
    "MÁXIMO": "36,46",
    "VOLUME": "2,58B"
  },
  {
    "DATA": "28/11/2024",
    "ABERTURA": "36,08",
    "FECHAMENTO": "35,88",
    "VARIAÇÃO": "-1,03",
    "MÍNIMO": "35,68",
    "MÁXIMO": "36,53",
    "VOLUME": "2,15B"
  },
  {
    "DATA": "27/11/2024",
    "ABERTURA": "36,45",
    "FECHAMENTO": "36,25",
    "VARIAÇÃO": "-0,36",
    "MÍNIMO": "36,10",
    "MÁXIMO": "36,59",
    "VOLUME": "2,31B"
  },
  {
    "DATA": "26/11/2024",
    "ABERTURA": "36,61",
    "FECHAMENTO": "36,38",
    "VARIAÇÃO": "-0,13",
    "MÍNIMO": "36,31",
    "MÁXIMO": "36,73",
    "VOLUME": "2,70B"
  },
  {
    "DATA": "25/11/2024",
    "ABERTURA": "n/d",
    "FECHAMENTO": "36,43",
    "VARIAÇÃO": "-0,61",
    "MÍNIMO": "36,40",
    "MÁXIMO": "37,06",
    "VOLUME": "1,34B"
  },
  {
    "DATA": "22/11/2024",
    "ABERTURA": "35,30",
    "FECHAMENTO": "36,65",
    "VARIAÇÃO": "3,98",
    "MÍNIMO": "35,77",
    "MÁXIMO": "37,03",
    "VOLUME": "4,27B"
  },
  {
    "DATA": "21/11/2024",
    "ABERTURA": "35,42",
    "FECHAMENTO": "35,25",
    "VARIAÇÃO": "0,29",
    "MÍNIMO": "34,91",
    "MÁXIMO": "35,45",
    "VOLUME": "2,11B"
  },
  {
    "DATA": "19/11/2024",
    "ABERTURA": "34,59",
    "FECHAMENTO": "35,14",
    "VARIAÇÃO": "-1,05",
    "MÍNIMO": "35,00",
    "MÁXIMO": "35,61",
    "VOLUME": "2,21B"
  },
  {
    "DATA": "18/11/2024",
    "ABERTURA": "34,59",
    "FECHAMENTO": "35,52",
    "VARIAÇÃO": "2,50",
    "MÍNIMO": "34,59",
    "MÁXIMO": "35,61",
    "VOLUME": "1,28B"
  }
]

petrobras = json.dumps(petrobras) # Convertendo a lista de dicionários para uma string JSON
petrobras = json.loads(petrobras) # Convertendo a string JSON de volta para uma lista de dicionários
petrobras = sorted(petrobras, key=lambda x: x["DATA"]) # Ordenando a lista de dicionários pela chave "DATA"

#print(petrobras) # Exibindo a lista de dicionários ordenada

# Criar o gráfico
plt.figure(figsize=(14, 7)) # Define o tamanho da figura
plt.plot(['DATAS'], ['ABERTURA'], label='Abertura', marker='o', linestyle='--', color='blue') 
plt.plot(['DATAS'], ['FECHAMENTO'], label='Fechamento', marker='o', linestyle='--', color='orange')
plt.plot(['DATAS'], ['VARIAÇÃO'], label='Variação', marker='o', linestyle='--', color='green')
plt.plot(['DATAS'], ['MÍNIMO'], label='Mínimo', marker='o', linestyle='--', color='red')
plt.plot(['DATAS'], ['MÁXIMO'], label='Máximo', marker='o', linestyle='--', color='purple')
plt.plot(['DATAS'], ['VOLUME'], label='Volume', marker='o', linestyle='--', color='brown')

# Configurações do eixo x
plt.xticks(rotation=90) # Rotaciona os rótulos do eixo x em 90 graus
plt.xlabel("Data") # Adiciona um rótulo ao eixo x
plt.ylabel("Preço") # Adiciona um rótulo ao eixo y
plt.legend("Ações da petrobras") # Adiciona a legenda ao gráfico
plt.title("Preços da Petrobras ao Longo do Tempo") # Adiciona um título ao gráfico

# Mostrar o gráfico
plt.tight_layout() # Ajusta o layout para evitar cortar o título
plt.show() # Exibe o gráfico
