mapeamento = {
  '6': 'F',
  '5': 'E',
  '50': 'L',
  '1': 'I',
  '26': 'Z',
  'MM': '2000',
  'R': '18'
}

codificado = "6550126 MMR"
decodificado = ""
i = 0
n = len(codificado)

while i < n:
  if i < n - 1:
      j = codificado[i:i+2]
      if j in mapeamento:
          decodificado += mapeamento[j]
          i += 2
          continue

  if codificado[i] in mapeamento:
      decodificado += mapeamento[codificado[i]]
  elif codificado[i] == ' ':
      decodificado += ' '
  i += 1

partes = decodificado.split()
texto = partes[0]
num = partes[1]

ano = str(int(num[:4]) + int(num[4:]))
fim = f"{texto} {ano}!"

print(f"Mensagem codificada: {codificado}")
print(f"Mensagem decodificada: {fim}")