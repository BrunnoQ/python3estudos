#import modulo01
import sys as sistema
from moduloz.modulo01 import *
from datetime import datetime

print(sistema.argv)
date = datetime.now()
print(date.strftime("%H:%I:%S"))

for i in sistema.argv[1:]:
	if i not in "%O%m%H":
		print("Paramtro nao reconhecido")
		exit()