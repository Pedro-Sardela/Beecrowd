def critoflinston(frase):
    frase = [ord(x) for x in frase]
    for i in range(len(frase)):
        if chr(frase[i]).isalpha():
            frase[i] += 3
    frase.reverse()
    meio = len(frase) // 2
    for i in range(meio, len(frase)):
        frase[i] -= 1
    frase = [chr(x) for x in frase]
    return frase

linhas = int(input())
for i in range(linhas):
    frase = list(input())
    resultado = critoflinston(frase)
    print("".join(str(t) for t in resultado))
