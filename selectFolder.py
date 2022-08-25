from easygui import diropenbox
from os import listdir

folderPath = ''
listFiles = []

def selectFolder():
    #listar os arquivo de extensão excel da pasta selecionada
    folderPath = diropenbox(title="Selecione a pasta", default="../..")
    FolderFiles = listdir(folderPath)
    for file in FolderFiles:
        if file.endswith(('.xlsm','xlsx')): 
            listFiles.append(file)