from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass



class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        print(f"\n[WeatherStation] Temperature updated to {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

class PhoneDisplay(Observer):
    def update(self, temperature: float):
        print(f"[PhoneDisplay] New temperature: {temperature}°C")


class LEDDisplay(Observer):
    def update(self, temperature: float):
        print(f"[LEDDisplay] Display updated with temperature: {temperature}°C")


class AlarmSystem(Observer):
    def update(self, temperature: float):
        if temperature > 30:
            print(f"[AlarmSystem] WARNING: High temperature alert! {temperature}°C")
        else:
            print(f"[AlarmSystem] Temperature is normal: {temperature}°C")

from abc import ABC, abstractmethod


# --- Observer Base Class ---
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass


# --- Subject Base Class ---
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# --- Concrete Subject: WeatherStation ---
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        print(f"\n[WeatherStation] Temperature updated to {temperature}°C")
        self._temperature = temperature
        self.notify_observers()


# --- Concrete Observers ---
class PhoneDisplay(Observer):
    def update(self, temperature: float):
        print(f"[PhoneDisplay] New temperature: {temperature}°C")


class LEDDisplay(Observer):
    def update(self, temperature: float):
        print(f"[LEDDisplay] Display updated with temperature: {temperature}°C")


class AlarmSystem(Observer):
    def update(self, temperature: float):
        if temperature > 30:
            print(f"[AlarmSystem] WARNING: High temperature alert! {temperature}°C")
        else:
            print(f"[AlarmSystem] Temperature is normal: {temperature}°C")


# --- Application Logic ---
if __name__ == "__main__":
    # Create the weather station (subject)
    station = WeatherStation()

    # Create observers (devices)
    phone = PhoneDisplay()
    led = LEDDisplay()
    alarm = AlarmSystem()

    # Register observers
    station.register_observer(phone)
    station.register_observer(led)
    station.register_observer(alarm)

    # Simulate temperature updates
    station.set_temperature(22.5)
    station.set_temperature(31.0)
    station.set_temperature(18.3)







