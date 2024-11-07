"""
    Desafio 1!
    Sistema de Previsão Metereológica Avançado
    Crie um programa que simule um sistema de previsão do tempo.
    O usuário deverá inserir dados sobre a temperatura, umidade, velocidade do tempo e condições atmosféricas (ensolarado, nublado, chuvoso, etc..). O programa deve utilizar estruturas condicionais aninhadas para deteminar a previsão detalhada, levando em consideração múltiplos fatores. Por exemplo:
    * Se a temperatura for MENOR QUE 0C e 30C e o tempo estiver ensolarado, prever "Clima agradável".
    *Inclua pelo menos 10 combinações possíveis de condições.
    Desafio Extra: Adicione uma análise para prever condições adversas, como "Tempestade severa" ou "Onda de calor", utilizando condições múltiplas.
    
    Ler sckit-learn
    keras
    *pandas
"""


def metereologicalStation(temp, humidity, airSpeed, cond):

   results = {
       "Clima agradável": temp >= 20 and temp <= 30,
       "Nevasca": temp < 0 and humidity > 80,
       "Neblina densa": temp in range(5,15) and humidity in range(90,100) and airSpeed in range(0,5),
       "Ensolarado e seco": temp in range(25,35) and humidity in range(20,40) and airSpeed in range(10,15),
       "Quente e úmido": temp >= 30 and temp <= 40 and humidity in range(60,90) and airSpeed in range(5,10),
       "Granizo e frio": temp in range(-2, 8) and humidity in range(60,80) and airSpeed(20,30) and cond== "Frio",
       "Nublado e ameno": temp in range(15, 25) and humidity in range(50, 70) and airSpeed(10,20),
       "Neve com vento": temp in range(-10, 0) and humidity(50, 80) and airSpeed(20,40) or cond=="Neve",
       "Tempestade severa": temp in range(15, 25) and humidity in range(80,100) and airSpeed(80,120) and cond =="Ventos fortes" or "Granizo e frio" or "Chuvas"
    }
   
   for key, value in results.items():
       if value :
        print(key)
    

temp = float(input("Insira a temperatura atual: "))
humidity = int(input("Insira a umidade: "))
airSpeed = int(input("Insira a velocidade do ar: "))
cond = input("Insira uma condição atmosférica: ")


metereologicalStation(temp, humidity, airSpeed, cond)