# -*- coding:utf-8 -*-
import math
from geopy.distance import geodesic as distance
from utils import Point, Cell


def calculate_distance_km_between_two_point(pointx: Point, pointy: Point):
    """
    calculate great-circle distance
    :param pointx: Point latitude [-90, 90]
    :param pointy: Point longitude [-180, 180]
    :return:
    """
    return distance(pointx.tuple(), pointy.tuple()).kilometers


def convert_distance_to_lnglat(point: Point, distance=Cell.CELL_RADIUS, angle=60.0):
    """
    1° in latitude is 111 km
    1° in longitude is 111*cos(angle) km
    :param point:
    :param distance:
    :param angle:
    :return:
    """
    lat_distance = distance * (1 + math.sin(angle))
    lng_distance = math.sqrt(distance)

    delta_lng = lng_distance * math.sin(angle * math.pi / 180) / (111 * math.cos(point.latitude * math.pi / 180))
    delta_lat = lat_distance * math.cos(angle * math.pi / 180) / 111

    return Point(point.longitude + delta_lng, point.latitude + delta_lat)


def get_upper_right_cell(point: Point):
    return convert_distance_to_lnglat(point, angle=60)


def get_bottom_right_cell(point: Point):
    return convert_distance_to_lnglat(point, angle=-60)


def get_cell_above(point: Point):
    return convert_distance_to_lnglat(point, distance=Cell.CELL_RADIUS * 3, angle=90.0)


def get_cell_below(point: Point):
    return convert_distance_to_lnglat(point, distance=Cell.CELL_RADIUS * 3, angle=-90.0)


if __name__ == "__main__":
    print(calculate_distance_km_between_two_point(Point(), Point()))
    print(get_upper_right_cell(Point()))
    print(get_bottom_right_cell(Point()))
    print(get_cell_above(Point()))
    print(get_cell_below(Point()))

