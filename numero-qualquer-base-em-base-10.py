c = int(input("Quantas casas tem seu número : "))
base = int(input("Qual a base do número: "))
final = 0
i = 1
while c > 0:
    final += (int(input(f"Digite seu {i}º número: "))) * (base ** (c-1))
    c += -1
    i += 1
print(final)

