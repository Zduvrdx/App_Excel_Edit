from easygui import diropenbox
from os import listdir

folderPath = ''
listFiles = ''

def selectFolder():
    folderPath = diropenbox(msg="Selecione a pasta")
    listFiles = listdir(folderPath)
    justExcelFiles(listFiles)


def justExcelFiles(listFiles):
    for file in range(0, len(listFiles)-1):
        if ".xls" not in listFiles[file]:
            listFiles.remove(file)

