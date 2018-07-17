# -*- coding:utf-8 -*-
import math


class Point:
    def __init__(self, lng=121.47, lat=31.23):
        """

        :param lng:
        :param lat:
        """
        self._lng = lng
        self._lat = lat

    @staticmethod
    def from_lnglat_str(coor='121.47, 31.23'):
        """

        :param coor: str: longitude, latitude
        :return:
        """
        _lng = float(coor.split(",")[0])
        _lat = float(coor.split(",")[1])
        return Point(_lng, _lat)

    def __repr__(self):
        return f"<Point({self._lng}, {self._lat})>"

    def latlng_tuple(self):
        """

        :return:
        """
        return self._lat, self._lng

    @property
    def latitude(self):
        return self._lat

    @property
    def longitude(self):
        return self._lng


class Cell:
    CELL_RADIUS = 3.0
    CENTER_TO_EDGE = math.sqrt(3)

    def __init__(self, center_point=Point(), radius=CELL_RADIUS, color="red"):
        self._center = center_point
        self._radius = radius
        self._color = color

    def __repr__(self):
        return f"<Cell({self._center}, {self._radius}, {self._color})>"

    def items(self):
        return {
            "center": {
                "latitude": self._center.latitude,
                "longitude": self._center.longitude
            },
            "color": self.color,
            "radius": self._radius
        }

    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    @property
    def color(self):
        return self._color


def frange(x, y, interval):
    while x < y:
        yield x
        x += interval
