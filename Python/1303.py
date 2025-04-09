class Time:
    def __init__(self, num, marcados, recebidos, pontuacao):
        self.num = num
        self.marcados = marcados
        self.recebidos = recebidos
        self.pontuacao = pontuacao

def media(marcados, recebidos):
    if recebidos == 0:
        return marcados
    else:
        return marcados/recebidos
    

qtdTimes = int(input())
times = []
instancia = 1
for i in range(qtdTimes):
    c = Time(i+1,0,0,0)
    times.append(c)

while input() != 0:
    for i in range(int(qtdTimes*((qtdTimes-1)/2))):
        x, y, z, w = (int(x) for x in input().split())
        times[x].marcados += y
        times[x].recebidos += w
        times[z].marcados += w
        times[z].recebidos += y
        if y > w:
            times[x].pontuacao += 2
            times[z].pontuacao += 1
        else:
            times[z].pontuacao += 2
            times[x].pontuacao += 1
resultado = sorted(times, key=lambda x: (-x.pontuacao, -media(x.marcados, x.recebidos), x.marcados, x.num ))

print(f"Instancia {instancia}\n")
instancia += 1
for i in range(qtdTimes):
    if i != qtdTimes:
        print(f"{resultado[i].num} ")
    else:
        print(f"{resultado[i]}")

