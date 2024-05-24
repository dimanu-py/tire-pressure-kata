import pytest

from tire_pressure.alarm import Alarm
from tire_pressure.sensor import Sensor


@pytest.fixture
def alarm_fixture() -> Alarm:
    sensor = Sensor()
    return Alarm(sensor=sensor)
