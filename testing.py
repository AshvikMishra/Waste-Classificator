import classify
import base64

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps

file_path = filedialog.askopenfilename()

imagePath = "test-images/testing.jpg"
result = classify.analyse(file_path)

print(result)
