# open ("caminho", "r")

# Mode
# r - leitura do arquivo
# a - Append / incremente
# w - Escrita
# x - Criar arquivo
# R+ - Leitura + Escrita

arquivo = open("test.txt","a")

#print(arquivo.readable())
#print(arquivo.read())
#print(arquivo.readline())
#lista = arquivo.readlines()
#print(lista[3])


arquivo.write("SQL\n")
arquivo.write("Angular\n")
arquivo.close()# sempre que tiver que abrir um arquivo tem que feichar no final, sempre usar close.

