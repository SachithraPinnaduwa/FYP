import json
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional

class WeatherAPIClient:
    """A realistic weather API client with caching, error handling, and data parsing."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.openweathermap.org/data/2.5"):
        self.api_key = api_key
        self.base_url = base_url
        self.cache: Dict[str, Dict[str, Any]] = {}

    def fetch_weather(self, city: str, temp_unit: str = "metric") -> Optional[Dict[str, Any]]:
        cache_key = f"{city}_{temp_unit}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        params = urllib.parse.urlencode({
            "q": city,
            "appid": self.api_key,
            "units": temp_unit
        })
        url = f"{self.base_url}/weather?{params}"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    parsed = self._parse_weather_data(data)
                    self.cache[cache_key] = parsed
                    return parsed
        except urllib.error.URLError as e:
            print(f"Network error: {e}")
        except json.JSONDecodeError:
            print("Failed to decode JSON response")
            
        return None

    def _parse_weather_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "city": data.get("name", "Unknown"),
            "temperature": data.get("main", {}).get("temp"),
            "humidity": data.get("main", {}).get("humidity"),
            "conditions": [w.get("description") for w in data.get("weather", [])]
        }
