#!/usr/bin/python3
"""Initialize models directory"""
from models.engine.file_storage import FileStorage

#create an instance of FileStorage
storage = FileStorage()

#Reload data from storage
storage.reload()
