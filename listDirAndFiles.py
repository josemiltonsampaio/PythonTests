from pathlib import Path, PureWindowsPath
import os
import glob
import sys
import codecs


def save(text, file):
    if file:
        with open(file, "a", encoding="utf-8") as fileObj:
            fileObj.write(text + "\n")

    else:
        print(text)


recursive = False
saveTo = ""


if len(sys.argv) == 1:
    path = Path()

if len(sys.argv) >= 2:
    path = Path(sys.argv[1])
    if not path.exists():
        print("Caminho não encontrado:", sys.argv[1])
        sys.exit()

    if len(sys.argv) >= 3:
        if sys.argv[2].lower() == "-r":
            recursive = True

        if len(sys.argv) >= 4:
            saveTo = sys.argv[3]


dirs = []  # type:list

if recursive:
    # os.walk result is a 3 items tuple, root, dirs, files
    # it's recursive. In this case x[0] gets only the root directory
    # of each directory (and subdirectories)
    dirs = [x[0] for x in os.walk(path)]
    print('teste:', dirs)
    for dir in dirs:
        save(str(PureWindowsPath(dir)) + "\\", saveTo)
        path = Path(dir)
        files = [f for f in path.glob("*.*")]
        for file in files:
            save(str(file), saveTo)
else:
    dirs = [d for d in path.iterdir() if d.is_dir()]
    files = [f for f in path.glob("*.*")]
    for dir in dirs:
        save(str(PureWindowsPath(dir)) + "\\", saveTo)
    for file in files:
        save(str(file), saveTo)

if saveTo:
    save("-------------------------------", saveTo)
    print("Arquivo criado")
