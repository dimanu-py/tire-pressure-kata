from unittest.mock import patch

from tire_pressure.alarm import Alarm


class TestAlarm:

    def test_alarm_is_off_by_default(self, alarm_fixture: Alarm):
        assert not alarm_fixture.is_alarm_on

    def test_alarm_is_on_when_pressure_is_too_low(self, alarm_fixture: Alarm):
        with patch("tire_pressure.sensor.TireSensor.pop_next_pressure_psi_value", return_value=16):
            alarm_fixture.check_pressure()

            assert alarm_fixture.is_alarm_on

    def test_alarm_is_on_when_pressure_it_to_high(self, alarm_fixture: Alarm):
        with patch("tire_pressure.sensor.TireSensor.pop_next_pressure_psi_value", return_value=22):
            alarm_fixture.check_pressure()

            assert alarm_fixture.is_alarm_on

    def test_alarm_is_off_when_pressure_is_between_thresholds(self, alarm_fixture: Alarm):
        with patch("tire_pressure.sensor.TireSensor.pop_next_pressure_psi_value", return_value=18):
            alarm_fixture.check_pressure()

            assert not alarm_fixture.is_alarm_on
