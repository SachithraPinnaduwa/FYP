class SimpleCronParser:
    def __init__(self, cron_string: str):
        parts = cron_string.split()
        if len(parts) != 5:
            raise ValueError("Invalid cron format, expected 5 parts")
        self.minute, self.hour, self.day_of_month, self.month, self.day_of_week = parts

    def _match_part(self, value: int, cron_part: str) -> bool:
        if cron_part == '*':
            return True
        if '/' in cron_part:
            base, step = cron_part.split('/')
            return value % int(step) == 0
        if '-' in cron_part:
            start, end = map(int, cron_part.split('-'))
            return start <= value <= end
        if ',' in cron_part:
            values = map(int, cron_part.split(','))
            return value in values
        return value == int(cron_part)

    def is_time_match(self, minute: int, hour: int, day: int, month: int, weekday: int) -> bool:
        return (self._match_part(minute, self.minute) and
                self._match_part(hour, self.hour) and
                self._match_part(day, self.day_of_month) and
                self._match_part(month, self.month) and
                self._match_part(weekday, self.day_of_week))