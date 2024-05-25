from tests.stub_sensor import StubSensor
from tire_pressure.alarm import Alarm


class TestAlarm:

    def test_alarm_is_off_by_default(self):
        stub_sensor = StubSensor()
        alarm = Alarm(sensor=stub_sensor)

        assert not alarm.is_alarm_on
