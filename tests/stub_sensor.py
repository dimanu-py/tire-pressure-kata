from tire_pressure.sensor import Sensor


class StubSensor(Sensor):

    def __init__(self) -> None:
        self._pressure_values = []

    def stub_call_to_pop_next_pressure_psi_value(self, returned_pressures: list[int]) -> None:
        for pressure in returned_pressures:
            self._pressure_values.append(pressure)

    def pop_next_pressure_psi_value(self) -> float:
        return self._pressure_values.pop()
