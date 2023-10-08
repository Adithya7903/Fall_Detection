from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile
from PyQt5.uic import loadUi

# Load the UI file
ui_file = QFile("app.ui")
ui_file.open(QFile.ReadOnly)
ui = loadUi(ui_file)
ui_file.close()

# Write the Python code to a file
with open("app_ui.py", "w") as py_file:
    ui.save(py_file)

print("Conversion completed.")
