import requests
import zipfile
import os

def check_for_updates(current_version="1.0.0"):
    url = "https://raw.githubusercontent.com/ваш-пользователь/ваш-репозиторий/main/version.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        latest_version = data["version"]
        update_url = data["url"]
        
        if latest_version != current_version:
            print("New version available!")
            return latest_version, update_url
        else:
            print("You are using the latest version.")
            return None, None
    except requests.RequestException as e:
        print(f"Error checking for updates: {e}")
        return None, None

def download_update(url):
    local_filename = "update.zip"
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall("update")
    
    os.remove(local_filename)
    print("Update downloaded and extracted successfully.")