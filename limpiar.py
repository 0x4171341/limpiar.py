#Creador :https://www.facebook.com/bruja121
#Mejorado https://github.com/cyberthrone
import os
import sys
import shutil
import time
os.system('clear')
time.sleep(1)
if 'creador' in sys.argv:
   print ("creador :team centinelas")
   exit(0)
elif 'introducion' in sys.argv:
   print("""
1-Cuando escribimos cosas en la terminal,eso deja ovbiamente huellas,y es un dato importante
en la informatica forense,sin olvidar que forma parte del mantenimiento
2-la cache tambien puede aplicarse en la informatica forense,ovbiamente no hay que
limpiarla todos los dias,pero si al menos una vez ha la semana que tambien forma
parte del mantenimiento.
3-cuando instalamos por ejemplo filezilla desde ubuntu-center el centro de
software de ubuntu,este no borra el archivo deb que descargo,con lo cual
despues de muchas instalacion esta ocupando un espacio inecesario y eso afecta mucho""")
   exit(1)
print ("""Modo de uso:
python3 limpiar.py
1-Limpiar logs Terminal
2-Vaciar la cache
3-clean
4-vaciar_tmp
5-Vaciar la papelera de reciclaje
creador:python3 limpiar.py creador
introducion python3 limpiar.py introduccion
si no tienes py3 instalado:sudo apt-get install python3""")
def limpiar_terminal():
   try:
      nombre = input("Escribe tu nombre de usuario:")
      os.chdir("/home/"+nombre+"/")  #os.environ['HOME']
      file = open(".bash_history",'w')
      file.write('')
      file.close()
   except:
      os.chdir('/root/')
      file = open(".bash_history",'w')
      file.write('')
      file.close()
      print ("Se ha vaciado con exito los logs de la terminal")
def vaciar_cache():
   try:
      tu_nombre = input("Escribe tu nombre de usuario:")
      os.chdir("/home/"+tu_nombre+"/")
      shutil.rmtree('.cache')
      os.mkdir('.cache')
      os.chmod('.cache', 0o777)
      print ("Se ha vaciado con exito la cache del sistema")
   except:
      os.chdir("/root/")
      shutil.rmtree('.cache')
      os.mkdir('.cache')
      os.chmod('.cache', 0o777)
      print ("Se ha vaciado con exito la cache del sistema")
def clean():
   os.chdir('/var/cache/apt/')
   shutil.rmtree('archives')
   os.mkdir('archives')
   os.chmod('archives', 0o777)
   print("Se ha vaciado correctamente")
def vaciar_tmp():
   os.chdir('tmp')
   shutil.rmtree('tmp')
   os.mkdir('tmp')
   os.chmod('tmp', 0o777)
def vaciar_papelera():
   try:
      indica = input("Indica tu nombre de usuario:")
      os.chdir("/home/"+indica+"/.local/share/")
      shutil.rmtree('Trash')
      os.mkdir('Trash')
      os.chmod('Trash', 0o777)
      print ("Se ha vaciado la papelera correctamente")
   except:
      os.chdir("/root/.local/share/")
      shutil.rmtree('Trash')
      os.mkdir('Trash')
      os.chmod('Trash', 0o777)
      print ("Se ha vaciado la papelera correctamente")    
opcion = input("Elige la opcion deseada:")
if opcion == "1":
   limpiar_terminal()
elif opcion == "2":
   vaciar_cache()
elif opcion == "3":
   clean()
elif opcion == "4":
   vaciar_tmp()
elif opcion == "5":
   vaciar_papelera()
else:
   print ("Opcion equivocada")
