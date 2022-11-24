import random 

min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'

qnt = input('Digite qual tamanho da senha: ')
qntInt = int(qnt)
length = qntInt

#Criando senhas
all = min + max + num + sybs
passwordAll = "".join(random.sample(all,length))

#Maiúsculas e números
MAXnum = max + num
passwordMAXnum = "".join(random.sample(MAXnum,length))

#Minusculas e Maiúsculas
MAXmin = max + min
passwordMAXmin = "".join(random.sample(MAXmin,length))

print ('passwordAll = ' + passwordAll) 
print ('passwordMAXnum = ' + passwordMAXnum) 
print ('passwordMAXmin = ' + passwordMAXmin)