import pytest

from tire_pressure.alarm import Alarm


@pytest.fixture
def alarm_fixture() -> Alarm:
    return Alarm()
