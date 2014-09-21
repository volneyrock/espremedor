import os.path
import zipfile

class Compactador:
    def compactar(self, arquivos):
        arq_zip = zipfile.ZipFile("aquivo.zip","w")
        for arquivo in arquivos:
            if(os.path.isfile(arquivo) and os.path.exists(arquivo)):
                base = os.path.basename(arquivo)
                arq_zip.write(arquivo,base)
        arq_zip.close()

    def descompactar(self,arquivo_zip):
        arquivo = zipfile.ZipFile.extractall(arquivo_zip)
        
         
        
    
