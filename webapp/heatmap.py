# -*- coding:utf-8 -*-
import time

import numpy as np
from webapp.thrall.amap import session
from webapp.thrall.amap.consts import ExtensionFlag
from webapp.gistool import *
from webapp.map_batch_api import *


def get_city_polylines(keywords: str):
    """

    :param keywords: the keyword of cityname in China in Chinese!!!
    :return:
    """
    result = session.district(keywords, sub_district=0, extensions=ExtensionFlag(1))
    raw_polylines = result.data[0].polyline.split("|") if result.data else []

    return [
        Point.from_lnglat_str(polyline)
        for raw_polyline in raw_polylines
        for polyline in raw_polyline.split(";")
    ]


def get_city_cells(_polylines: [Point]):
    """

    :param _polylines:
    :return:
    """
    sorted_polylines_by_longitude = sorted(_polylines, key=lambda kv: kv.longitude)
    left = sorted_polylines_by_longitude[0]
    right = sorted_polylines_by_longitude[-1]

    sorted_polylines_by_latitude = sorted(_polylines, key=lambda kv: kv.latitude)
    bottom = sorted_polylines_by_latitude[0]
    top = sorted_polylines_by_latitude[-1]
    # print(sorted_polylines_by_longitude)
    # print(sorted_polylines_by_latitude)
    # print(left, right, top, bottom)
    # print(calculate_distance_km_between_two_point(left, right))

    longitude_precision = convert_distance_to_lnglat(distance=Cell.CELL_RADIUS * math.sqrt(3), angle=0).longitude
    latitude_precision = convert_distance_to_lnglat(distance=Cell.CELL_RADIUS * 3, angle=90).latitude
    offset = convert_distance_to_lnglat(distance=Cell.CELL_RADIUS * math.sqrt(3), angle=60)
    # print(left.longitude, right.longitude + longitude_precision, longitude_precision)
    # print(bottom.latitude, top.latitude + latitude_precision, latitude_precision)
    # print(offset)

    return [
               Cell(Point(i, j))
               for i in np.arange(left.longitude + longitude_precision,
                                  right.longitude,
                                  longitude_precision)
               for j in np.arange(bottom.latitude + latitude_precision,
                                  top.latitude + latitude_precision,
                                  latitude_precision)
           ] + \
           [
               Cell(Point(i, j))
               for i in np.arange(left.longitude + offset.longitude,
                                  right.longitude + offset.longitude,
                                  longitude_precision)
               for j in np.arange(bottom.latitude + offset.latitude,
                                  top.latitude + offset.latitude,
                                  latitude_precision)
           ]


def get_time_to_reach_in_batch(start_point: Point, _cells: [Cell], cityname="021"):
    _map = MapBatchAPI()
    results = []
    query_list = []
    for cell in _cells:
        query_list.append({
            "origin": start_point.url_str(),
            "destination": cell.center.url_str(),
            "city": cityname,
            "nightflag": "1",
            "output": "json"
        })
        if len(query_list) == 20:
            results += _map.get_transit_data(query_list)
            query_list = []
            time.sleep(0.5)
    results += _map.get_transit_data(query_list)

    return results


def filter_cells(cells, cityname):
    # TODO
    pass


def filter_results(results):
    return [
        result
        for result in results
        if isinstance(result, dict) and
           isinstance(result.get('body'), dict) and
           result.get('body').get('status') != '0'
    ]


if __name__ == "__main__":
    city_name = "上海"  # it has to be chinese keyword

    polylines = get_city_polylines(city_name)
    # print(*polylines, sep="\n")

    cells = get_city_cells(polylines)[:40]
    # print(*cells, sep="\n")

    results = get_time_to_reach_in_batch(Point('121.47, 31.23'), cells)
    # results = filter_results(results)
    # print(*results, sep="\n")
