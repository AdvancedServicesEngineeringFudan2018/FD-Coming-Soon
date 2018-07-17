# -*- coding:utf-8 -*-
import log
import consts


class Point:
    def __init__(self, coor='120.0, 30.0'):
        self._lat = float(coor.split(",")[0])
        self._lng = float(coor.split(",")[1])


class Cell:
    def __init__(self, center_point=Point(), size=consts.CELL_RADIUS):
        self._center = center_point
        self._size = size
