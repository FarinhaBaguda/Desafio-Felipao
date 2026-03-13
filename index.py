nomedoheroi = input("Digite o nome do seu herói: ")
xpdoheroi = int(input("Digite a quantidade de XP do seu herói: "))

rank = [
    "Ferro",
    "Bronze",
    "Prata",
    "Ouro",
    "Platina",
    "Ascendente",
    "Imortal",
    "Radiante"
]

if xpdoheroi <= 1000:
    indicedorank = 0
elif xpdoheroi <= 2000:
    indicedorank = 1
elif xpdoheroi <= 3000:
    indicedorank = 2
elif xpdoheroi <= 4000:
    indicedorank = 3
elif xpdoheroi <= 5000:
    indicedorank = 4
elif xpdoheroi <= 6000:
    indicedorank = 5
elif xpdoheroi <= 7000:
    indicedorank = 6
else:
    indicedorank = 7

print("O Herói de nome", nomedoheroi, "está no nível", rank[indicedorank])
