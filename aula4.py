'''fila = []
fila.append("Júlia")
fila.append("Sofia")
fila.append("Masanori")
print(fila)
fila.pop()
print(fila)
fila.pop()
print(fila)'''
A = [[0, 1, 0, 0, 0, 0], 
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 1, 0],
     [1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0]]

def Distancias(n, origem):
  d = [-1] * n
  d[origem] = 0
  f = []
  f.append(origem)
  while len(f) > 0:     #fila não vazia = possibilidades
    x = f.pop(0)        #retiro o primeiro da fila
    for y in range(n):      #percorre cidades
      if A[x][y] == 1 and d[y] == -1:
        #chego lá e nunca visitei mais (-1)
        d[y] = d[x] + 1
        f.append(y)     #enfileiro onde cheguei
                        #para ir mais para frente
  return d

print (Distancias(len(A), 5))
