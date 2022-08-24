from functools import total_ordering
import time
import os
import shutil
import sys
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/User/Downloads"
to_dir = "C:/Users/User/OneDrive/Documentos/Projetos/tarefa103/Arquivos_excluidos"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in from_dir.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Excluído ", file_name)
                path1 = from_dir + "/" + file_name
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + file_name
                if os.path.exists(path2):
                    print("Diretório já existe ")
                    print("Excluindo o arquivo ", name)
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    print("Criando diretório ")
                    os.mkdir(path2)
                    print("Excluindo o arquivo ", name)
                    shutil.move(path1, path3)
                    time.sleep(1)
            

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Executando... ")
except KeyboardInterrupt:
    print("Interrompido! ")
    observer.stop()