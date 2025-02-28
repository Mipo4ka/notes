import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

category={
            "images":[".png",".jpeg",".gif",".jpg",".raw"],
            "documents/text documents":[".txt"],
            "documents/word documents": [".docx", ".doc"],
            
        }
def soft_files(path):
    try:
        for filename in os.listdir(path):
            full_path=os.path.join(path, filename)
            if os.path.isfile(full_path):
                ext = os.path.splitext(filename)[1].lower()
                moved=False
                for cat, extention in category.items():
                    if ext in extention:
                        dest_dir = os.path.join(path, cat)
                         
                
            
    except Exception as e:
        logging.error(f"Ошибкав сортировке ФАЙЛОВ {e}")
        
soft_files(r"/home/student/Рабочий стол/Zlobinoi/data")
