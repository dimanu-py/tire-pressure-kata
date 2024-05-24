import pytest

from tire_pressure.alarm import Alarm
from tire_pressure.sensor import TireSensor


@pytest.fixture
def alarm_fixture() -> Alarm:
    sensor = TireSensor()
    return Alarm(sensor=sensor)
