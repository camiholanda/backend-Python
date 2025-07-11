

dist = float(input("Informe a distancia percorrida (km): "))
velo_media = float(input("Informe a velocidade média: "))

hora = dist / velo_media
print("O tempo de viagem = ", int(dist/velo_media), "h", int(60 * ((dist/velo_media) - int(dist/velo_media))), "min")

             