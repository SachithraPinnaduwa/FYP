import re
import datetime
from dataclasses import dataclass, field
from typing import List

@dataclass
class LogEntry:
    timestamp: datetime.datetime
    level: str
    message: str
    component: str = "main"

class SimpleLogParser:
    """A realistic parser for application log files using Regex and Dataclasses."""
    
    LOG_PATTERN = re.compile(
        r"\[(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\]\s+"
        r"\[(?P<level>INFO|WARNING|ERROR|DEBUG)\]\s+"
        r"(?:\((?P<component>[A-Za-z0-9_-]+)\)\s+)?:\s*"
        r"(?P<message>.*)"
    )

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.entries: List[LogEntry] = []

    def load_and_parse(self, filter_levels: List[str] = None):
        self.entries.clear()
        try:
            with open(self.filepath, 'r') as log_file:
                for line in log_file:
                    self._process_line(line, filter_levels or [])
        except FileNotFoundError:
            raise RuntimeError(f"Log file not found at {self.filepath}")

    def _process_line(self, line: str, allowed_levels: List[str]):
        match = self.LOG_PATTERN.search(line.strip())
        if not match:
            return

        level = match.group("level")
        if allowed_levels and level not in allowed_levels:
            return

        try:
            ts = datetime.datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S")
            entry = LogEntry(
                timestamp=ts,
                level=level,
                message=match.group("message"),
                component=match.group("component") or "main"
            )
            self.entries.append(entry)
        except ValueError:
            pass # Invalid timestamp format
            
    def get_errors_by_component(self) -> dict:
        results = {}
        for entry in self.entries:
            if entry.level == "ERROR":
                results[entry.component] = results.get(entry.component, 0) + 1
        return results
