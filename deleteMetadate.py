import mutagen
import os
for i in os.listdir('.'):
    data = mutagen.File(i)
    data.delete()