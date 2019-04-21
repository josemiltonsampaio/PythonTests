import os
from pathlib import Path
import sys

path = Path(sys.argv[1])

if not path.exists():
    print("Caminho não encontrado:", sys.argv[1])
    sys.exit()


dirs = [d[0] for d in os.walk(path)]
for dir in dirs:
    path = Path(dir)
    files = [f for f in path.glob("*.mp4")]
    for file in files:
        os.popen("ffmpeg -i " + '"' + str(file) + '" "' +
                 str(file).replace("mp4", "mp3") + '"')

print("Finalizado")
