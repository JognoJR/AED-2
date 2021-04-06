#contar os aspectos e lista-los em um arquivo
# betha pode ser executado em alpha!

aspectos = open('aspectos.think','r')
quantidades = open('quantidades.think','w')
print('Arquivo aberto;\n:)')
c = {}
qdt_aspec = qdt_elementos = 0

for e in aspectos:
    qdt_elementos += 1
    e = e.strip().lower()
    if c.get(e) is not None:
        c[e] += 1
    else:
        c.__setitem__(e,1)
        qdt_aspec += 1

print('Escrevendo no arquivo;\n:)')

quantidades.write(str(c))

aspectos.close()
quantidades.close()


print(str(qdt_elementos)+' elementos')
print(str(qdt_aspec)+' aspectos diferentes')
print('Feito\n:)')
