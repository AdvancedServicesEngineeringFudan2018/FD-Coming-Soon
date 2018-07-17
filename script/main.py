# -*- coding:utf-8 -*-
from thrall.amap import session
from thrall.amap.consts import ExtensionFlag
from utils import *


def get_city_polylines(keywords: str):
    """

    :param keywords: 地名关键词
    规则：只支持单个关键词语搜索关键词支持：行政区名称、citycode、adcode
    :return:
    """
    result = session.district(keywords, sub_district=0, extensions=ExtensionFlag(1))
    raw_polylines = result.data[0].polyline.split("|") if result.data else []

    return [
        Point.from_str(polyline)
        for raw_polyline in raw_polylines
        for polyline in raw_polyline.split(";")
    ]


def order_polylines_by_latitude(_polylines: [Point]):
    _sorted_polylines = sorted(_polylines, key=lambda kv: kv.latitude)
    return _sorted_polylines


def get_city_cells(sorted_polylines: [Cell]):
    pass


if __name__ == "__main__":
    polylines = get_city_polylines("上海")
    # print("上海边界: ", polylines)

    sorted_polylines = order_polylines_by_latitude(polylines)
    # for i in sorted_polylines:
    #     print(i)

    cells = get_city_cells(sorted_polylines)
