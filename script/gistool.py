# -*- coding:utf-8 -*-
import math
from geopy.distance import geodesic as calculate
from utils import Point, Cell


def calculate_distance_km_between_two_point(pointx: Point, pointy: Point):
    """
    calculate distance in km
    :param pointx: Point
    :param pointy: Point
    :return:
    """
    return calculate(pointx.latlng_tuple(), pointy.latlng_tuple()).kilometers


def convert_distance_to_lnglat(point=Point(0, 0), distance=Cell.CELL_RADIUS, angle=60.0):
    """
    Latitude: 1 deg = 110.574 km
    Longitude: 1 deg = 111.320*cos(latitude) km
    :param point:
    :param distance:
    :param angle:
    :return:
    """
    lng_distance = distance * math.cos(angle * math.pi / 180)
    lat_distance = distance * math.sin(angle * math.pi / 180)
    # print(lng_distance, lat_distance)

    delta_lng = lng_distance / (111 * math.cos(point.latitude * math.pi / 180))
    delta_lat = lat_distance / 111
    # print(delta_lng, delta_lat)

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
    res = calculate_distance_km_between_two_point(Point(121, 31), Point(120, 30))
    print(res)
    print(convert_distance_to_lnglat(Point(120, 30), distance=res, angle=45))
    print(get_upper_right_cell(Point()))
    print(get_bottom_right_cell(Point()))
    print(get_cell_above(Point()))
    print(get_cell_below(Point()))
