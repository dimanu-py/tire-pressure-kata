from unittest.mock import patch

from tire_pressure.alarm import Alarm


class TestAlarm:

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on

    def test_alarm_is_on_when_pressure_is_too_low(self):
        alarm = Alarm()

        with patch("tire_pressure.sensor.Sensor.pop_next_pressure_psi_value", return_value=16):
            alarm.check_pressure()

            assert alarm.is_alarm_on
