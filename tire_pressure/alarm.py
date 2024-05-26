from tire_pressure.sensor import TireSensor


class Alarm:

    def __init__(self, sensor: TireSensor) -> None:
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21
        self._sensor = sensor
        self._is_alarm_on = False

    def check_pressure(self) -> None:
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()
        if psi_pressure_value < self._low_pressure_threshold or self._high_pressure_threshold < psi_pressure_value:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self) -> bool:
        return self._is_alarm_on
