#!/usr/bin/python3

from .engine.file_storage import FileStorage

""" creates a unique FileStorage instance for the application"""

storage = FileStorage()
storage.reload()
