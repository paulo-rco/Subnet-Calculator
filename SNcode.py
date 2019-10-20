ip = input("Entre com o endereco IPv4 \n")
snm = input("Entre com o CIDR \n")
snm = int(snm)
s1 = ip.split(".")
s2 = int(s1[0]) 
if snm >= 8:
    cidrp = 8
if snm >= 16:
    cidrp = 16
if snm >= 24:
    cidrp = 24

r1 = 2**(32-snm)-2

r2 = 2**(snm-cidrp)

opcao = input(
    "Se desejar numero de hosts validos digite 1 \n Se desejas numero de sub-redes digite 2 \n")
opcao = int (opcao)

if opcao == 1:
    print ("O numero de hosts e \n" + str(r1))
if opcao == 2:
    print ("O numero de sub-redes e \n" + str(r2))












