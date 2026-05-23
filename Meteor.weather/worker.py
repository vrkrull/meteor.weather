from PySide6.QtCore import QThread, Signal, QObject


class WeatherWorker(QThread):
    done = Signal(dict)

    def __init__(self, provider, lat, lon, units):
        super().__init__()
        self.provider = provider
        self.lat = lat
        self.lon = lon
        self.units = units
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def run(self):
        if self._cancel:
            return

        try:
            data = self.provider.get_weather(self.lat, self.lon, self.units)
        except Exception as e:
            data = {"error": str(e)}

        if not self._cancel:
            self.done.emit(data)


class WeatherQueue(QObject):
    def __init__(self):
        super().__init__()
        self.worker = None

    def fetch(self, provider, lat, lon, units, callback):
        if self.worker:
            self.worker.cancel()
            self.worker = None

        self.worker = WeatherWorker(provider, lat, lon, units)
        self.worker.done.connect(callback)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.start()