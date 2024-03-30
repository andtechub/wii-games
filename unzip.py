import zipfile
import os
import shutil

def entpacke_zip(zip_dateipfad, entpackungsziel):
    with zipfile.ZipFile(zip_dateipfad, 'r') as zip_ref:
        zip_ref.extractall(entpackungsziel)

def kopiere_wbfs(quellordner, zielordner):
    for ordnername, _, dateien in os.walk(quellordner):
        for datei in dateien:
            if datei.lower().endswith('.wbfs'):
                wbfs_dateipfad = os.path.join(ordnername, datei)
                ziel_dateipfad = os.path.join(zielordner, datei)
                if not os.path.exists(ziel_dateipfad):
                    shutil.move(wbfs_dateipfad, zielordner)
                    print(f"Verschiebe {datei} nach {zielordner}")
                else:
                    print(f"Datei {datei} existiert bereits im Zielordner") # File Exists

def loesche_entpackte_datei(entpackte_dateipfad):
    shutil.rmtree(entpackte_dateipfad)
    print(f"Entpackter Ordner gelöscht: {entpackte_dateipfad}")

if __name__ == "__main__":
    ordner_pfad = "path/to/zip/folder"
    entpackungsziel = "path/to/temp/folder" # Create an temp folder
    zielordner = "/path/to/target/folder" 

    for zip_datei in os.listdir(ordner_pfad):
        if zip_datei.lower().endswith('.zip'):
            zip_dateipfad = os.path.join(ordner_pfad, zip_datei)
            entpacke_zip(zip_dateipfad, entpackungsziel)
            kopiere_wbfs(entpackungsziel, zielordner)
            loesche_entpackte_datei(entpackungsziel)