import os
import requests
from xml.etree import ElementTree as ET
from tqdm import tqdm
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

# Basis-URL
base_url = "https://archive.org/download/wiieuroperedump/"

# Pfad zur XML-Datei als URL
xml_url = "https://ia804707.us.archive.org/2/items/wiieuroperedump/wiieuroperedump_files.xml"  # Setze den tatsächlichen URL-Pfad deiner XML-Datei ein

def download_file(file_name, file_url):
    response = requests.get(file_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name)

    with open(file_name, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

def download_wrapper(file_info):
    file_name = file_info['name']
    file_url = base_url + file_name.replace(" ", "%20")
    
    print(f"Downloade {file_name}...")

    # Überprüfe, ob die Datei bereits existiert, bevor sie erneut heruntergeladen wird
    if not os.path.exists(file_name):
        download_file(file_name, file_url)
        print(f"{file_name} erfolgreich heruntergeladen.")
    else:
        print(f"{file_name} existiert bereits. Überspringe den Download.")

def main():
    # Lese die XML-Datei von der URL ein
    response = requests.get(xml_url)
    tree = ET.fromstring(response.content)

    # Extrahiere Informationen über Dateien
    files_info = [{'name': file_elem.attrib['name']} for file_elem in tree.findall('.//file')]

    # Starte bis zu 3 Downloads gleichzeitig
    with ThreadPoolExecutor(max_workers=60) as executor:
        executor.map(download_wrapper, files_info)

if __name__ == "__main__":
    main()

