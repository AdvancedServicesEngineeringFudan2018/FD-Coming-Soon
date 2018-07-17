# -*- coding:utf-8 -*-
from thrall.amap import session
from thrall.amap.consts import ExtensionFlag
from utils import *


def get_city_polyline(keywords):
    """

    :param keywords: 地名关键词
    规则：只支持单个关键词语搜索关键词支持：行政区名称、citycode、adcode
    :return:
    """
    result = session.district(keywords, sub_district=0, extensions=ExtensionFlag(1))
    raw_polylines = result.data[0].polyline.split("|") if result.data else []

    return [
        Point(polyline)
        for raw_polyline in raw_polylines
        for polyline in raw_polyline.split(";")
    ]


if __name__ == "__main__":
    print("上海边界: ", get_city_polyline("上海"))
