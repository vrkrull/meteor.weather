from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QFrame
)

from providers import PROVIDERS
from worker import WeatherQueue
from geocode import geocode_city


def decode_weather(code):
    map_ = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        61: "Rain",
        71: "Snow",
        80: "Showers",
        95: "Thunderstorm"
    }
    return map_.get(code, "Unknown")


class WeatherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meteor.weather")
        self.setMinimumSize(520, 820)

        self.providers = PROVIDERS
        self.provider = self.providers[0]
        self.units = "metric"

        self.queue = WeatherQueue()

        self.build_ui()
        self.refresh()

    # ---------------- UI ----------------

    def build_ui(self):
        root = QVBoxLayout(self)

        # ---------- TOP BAR ----------
        top = QHBoxLayout()

        self.city = QLineEdit()
        self.city.setPlaceholderText("Search city")

        self.provider_box = QComboBox()
        self.provider_box.addItems([p.name for p in self.providers])
        self.provider_box.currentIndexChanged.connect(self.switch_provider)

        self.unit_btn = QPushButton("°C / °F")
        self.unit_btn.clicked.connect(self.toggle_units)

        search = QPushButton("Search")
        search.clicked.connect(self.refresh)

        top.addWidget(self.city)
        top.addWidget(self.provider_box)
        top.addWidget(self.unit_btn)
        top.addWidget(search)

        root.addLayout(top)

        # ---------- HERO ----------
        self.temp = QLabel("—")
        self.desc = QLabel("")
        self.meta = QLabel("")

        self.temp.setStyleSheet("font-size: 80px; font-weight: 200;")
        self.desc.setStyleSheet("font-size: 20px; opacity: 0.85;")
        self.meta.setStyleSheet("font-size: 13px; opacity: 0.6;")

        root.addWidget(self.temp)
        root.addWidget(self.desc)
        root.addWidget(self.meta)

        # ---------- DETAILS GRID ----------
        self.grid = QGridLayout()

        self.feels = QLabel()
        self.wind = QLabel()
        self.humidity = QLabel()
        self.pressure = QLabel()
        self.visibility = QLabel()

        self.grid.addWidget(self.card("Feels Like", self.feels), 0, 0)
        self.grid.addWidget(self.card("Wind", self.wind), 0, 1)
        self.grid.addWidget(self.card("Humidity", self.humidity), 1, 0)
        self.grid.addWidget(self.card("Pressure", self.pressure), 1, 1)
        self.grid.addWidget(self.card("Visibility", self.visibility), 2, 0, 1, 2)

        root.addLayout(self.grid)

        # ---------- STYLE ----------
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #0b1220,
                    stop:1 #05070d
                );
                color: white;
                font-family: Segoe UI;
            }

            QLineEdit, QComboBox {
                padding: 10px;
                border-radius: 12px;
                background: rgba(255,255,255,0.08);
                border: none;
            }

            QPushButton {
                padding: 10px;
                border-radius: 12px;
                background: #3b82f6;
                font-weight: 600;
            }

            QFrame {
                background: rgba(255,255,255,0.06);
                border-radius: 14px;
                padding: 10px;
            }
        """)

    def card(self, title, label):
        box = QFrame()
        layout = QVBoxLayout(box)

        t = QLabel(title)
        t.setStyleSheet("opacity:0.6; font-size:12px;")

        label.setStyleSheet("font-size:16px; font-weight:500;")

        layout.addWidget(t)
        layout.addWidget(label)

        return box

    # ---------------- LOGIC ----------------

    def switch_provider(self, i):
        self.provider = self.providers[i]
        self.refresh()

    def toggle_units(self):
        self.units = "imperial" if self.units == "metric" else "metric"
        self.refresh()

    def refresh(self):
        lat, lon = geocode_city(self.city.text())

        self.queue.fetch(
            self.provider,
            lat,
            lon,
            self.units,
            self.update_ui
        )

    # ---------------- UPDATE ----------------

    def update_ui(self, data):
        if "error" in data:
            self.temp.setText("Error")
            self.desc.setText(data["error"])
            return

        c = data.get("current", {})

        self.temp.setText(f"{c.get('temp', '—')}°")
        self.desc.setText(decode_weather(c.get("code", 0)) if "code" in c else c.get("desc", ""))

        self.feels.setText(str(c.get("feels_like", "—")))
        self.wind.setText(str(c.get("wind", "—")))
        self.humidity.setText(str(c.get("humidity", "—")))
        self.pressure.setText(str(c.get("pressure", "—")))
        self.visibility.setText(str(c.get("visibility", "—")))