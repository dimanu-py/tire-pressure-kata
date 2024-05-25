from tests.stub_sensor import StubSensor
from tire_pressure.alarm import Alarm


class TestAlarm:

    def test_alarm_is_off_by_default(self):
        stub_sensor = StubSensor()
        alarm = Alarm(sensor=stub_sensor)

        assert not alarm.is_alarm_on


    def test_alarm_is_on_when_pressure_is_too_low(self):
        stub_sensor = StubSensor()
        stub_sensor.stub_call_to_pop_next_pressure_psi_value([16])
        alarm = Alarm(sensor=stub_sensor)

        alarm.check_pressure()

        assert alarm.is_alarm_on

    def test_alarm_is_on_when_pressure_is_too_high(self):
        stub_sensor = StubSensor()
        stub_sensor.stub_call_to_pop_next_pressure_psi_value([22])
        alarm = Alarm(sensor=stub_sensor)

        alarm.check_pressure()

        assert alarm.is_alarm_on

    def test_alarm_is_off_when_pressure_is_normal(self):
        stub_sensor = StubSensor()
        stub_sensor.stub_call_to_pop_next_pressure_psi_value([18])
        alarm = Alarm(sensor=stub_sensor)

        alarm.check_pressure()

        assert not alarm.is_alarm_on
