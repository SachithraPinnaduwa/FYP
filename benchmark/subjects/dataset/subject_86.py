class GeoHash:
    BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

    @classmethod
    def encode(cls, lat: float, lon: float, precision: int = 12) -> str:
        lat_interval = [-90.0, 90.0]
        lon_interval = [-180.0, 180.0]
        geohash = []
        bits = [16, 8, 4, 2, 1]
        bit = 0
        ch = 0
        even = True

        while len(geohash) < precision:
            if even:
                mid = (lon_interval[0] + lon_interval[1]) / 2
                if lon > mid:
                    ch |= bits[bit]
                    lon_interval[0] = mid
                else:
                    lon_interval[1] = mid
            else:
                mid = (lat_interval[0] + lat_interval[1]) / 2
                if lat > mid:
                    ch |= bits[bit]
                    lat_interval[0] = mid
                else:
                    lat_interval[1] = mid

            even = not even
            if bit < 4:
                bit += 1
            else:
                geohash.append(cls.BASE32[ch])
                bit = 0
                ch = 0

        return "".join(geohash)

    @classmethod
    def decode(cls, geohash: str):
        lat_interval = [-90.0, 90.0]
        lon_interval = [-180.0, 180.0]
        even = True

        for char in geohash:
            idx = cls.BASE32.index(char)
            for bit in [16, 8, 4, 2, 1]:
                if even:
                    cls._refine_interval(lon_interval, idx, bit)
                else:
                    cls._refine_interval(lat_interval, idx, bit)
                even = not even

        lat = (lat_interval[0] + lat_interval[1]) / 2
        lon = (lon_interval[0] + lon_interval[1]) / 2
        return lat, lon

    @staticmethod
    def _refine_interval(interval, idx, bit):
        if idx & bit:
            interval[0] = (interval[0] + interval[1]) / 2
        else:
            interval[1] = (interval[0] + interval[1]) / 2