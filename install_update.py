import shutil
import os

def install_update():
    update_dir = "update"
    
    if os.path.exists(update_dir):
        for item in os.listdir(update_dir):
            s = os.path.join(update_dir, item)
            d = os.path.join(os.getcwd(), item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        
        shutil.rmtree(update_dir)
        print("Update installed successfully.")
    else:
        print("No update found.")