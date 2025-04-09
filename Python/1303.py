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
instancia = 1

while qtdTimes != 0:
    times = []
    for i in range(0, qtdTimes):
        c = Time(i+1,0,0,0)
        times.append(c)

    for i in range(int(qtdTimes * ((qtdTimes - 1) / 2))):
        x, y, z, w = [int(x) for x in input().split()]
        times[x-1].marcados += y
        times[x-1].recebidos += w
        times[z-1].marcados += w
        times[z-1].recebidos += y
        if y > w:
            times[x-1].pontuacao += 2
            times[z-1].pontuacao += 1
        else:
            times[z-1].pontuacao += 2
            times[x-1].pontuacao += 1
    resultado = sorted(times, key=lambda x: (-x.pontuacao, -media(x.marcados, x.recebidos), x.marcados, x.num ))

    print(f"Instancia {instancia}")
    print(" ".join(str(t.num) for t in resultado))
    instancia += 1

    qtdPreview = int(input())
    if qtdPreview != 0:
        print()
    qtdTimes = qtdPreview
