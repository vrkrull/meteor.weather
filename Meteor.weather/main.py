import sys
from PySide6.QtWidgets import QApplication
from ui import WeatherWindow

app = QApplication(sys.argv)
app.setApplicationName("Meteor.weather")

window = WeatherWindow()
window.show()

sys.exit(app.exec())