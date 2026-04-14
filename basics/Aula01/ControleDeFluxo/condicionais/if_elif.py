categoria = int(input("Digte a categoria do produto(1-5): "))

if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 20
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria == 5:
    preço = 31
else:
    print ("cateogira inválida, digite um valor entre 1 e 5!")
print (f"O preço do produto é: R$ {preço:6.2f}")