import math

class GeoDistance:
    EARTH_RADIUS_KM = 6371.0

    @classmethod
    def haversine(cls, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return cls.EARTH_RADIUS_KM * c

    @classmethod
    def bounding_box(cls, lat: float, lon: float, distance_km: float):
        lat_delta = math.degrees(distance_km / cls.EARTH_RADIUS_KM)
        lon_delta = math.degrees(distance_km / (cls.EARTH_RADIUS_KM * math.cos(math.radians(lat))))
        return {
            "min_lat": lat - lat_delta,
            "max_lat": lat + lat_delta,
            "min_lon": lon - lon_delta,
            "max_lon": lon + lon_delta
        }