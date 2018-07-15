# -*- coding: utf-8 -*-
import requests
import bs4
import urllib.parse
import hashlib
from secret import *

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
        'Chrome/56.0.2924.87 Safari/537.36'
}
city = 'shanghai'
city_CN = "上海"


def get_lines_stations():
    url = f'http://{city}.8684.cn'
    html = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(html.text, 'lxml')
    links_number = soup.find('div', class_='bus_kt_r1').find_all('a')
    links_letter = soup.find('div', class_='bus_kt_r2').find_all('a')
    links = links_letter + links_number
    lines_stations = {}
    for link in links:
        link_href = link['href']
        link_html = requests.get(url + link_href, headers=headers)
        link_soup = bs4.BeautifulSoup(link_html.text, 'lxml')
        lines = link_soup.find('div', class_='stie_list').find_all('a')
        for line in lines:
            line_href = line['href']
            line_name = line.get_text()
            try:
                line_html = requests.get(url + line_href, headers=headers)
                line_info = {}
                line_soup = bs4.BeautifulSoup(line_html.text, 'lxml')
                bus_lines = line_soup.find_all('div', class_='bus_line_site')
                for bus_line in bus_lines:
                    stations = []
                    bus_stations = bus_line.find_all('a')
                    for bus_station in bus_stations:
                        stations.append(bus_station.get_text())
                    # 来回两条路
                    if bus_lines.index(bus_line) == 0:
                        line_info[line_name] = stations
                lines_stations.update(line_info)
            except Exception:
                print(f"[info] some error occur during get the info of line {line_name}")
                continue
            print(f"[info] get the info of line {line_name}, total: {len(lines_stations)}")
        with open(f"data/lines_stations_{city}.json", "w", encoding='utf-8') as f:
            f.write(str(lines_stations))


def get_poi_position(address):
    # api documentation
    # http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
    query_str = f'/place/v2/search?query={address}&tag=公交车站&city_limit=true&region={city_CN}&output=json&ak={ak}'
    encoded_str = urllib.parse.quote(query_str, safe="/:=&?#+!$,;'@()*[]")
    raw_str = encoded_str + sk
    sn = hashlib.md5(urllib.parse.quote_plus(raw_str).encode("utf-8")).hexdigest()
    url = urllib.parse.quote("http://api.map.baidu.com" + query_str + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
    try:
        response = requests.get(url)
        content = eval(response.content)
        lng = content['results'][0]['location']['lng']
        lat = content['results'][0]['location']['lat']
        return lng, lat
    except Exception:
        return None, None


def get_lines_stations_geometry():
    lines_geometry = []

    with open(f'data/lines_stations_{city}.json', "r", encoding='utf-8') as f:
        lines = dict(eval(f.read()))
        for name, stations in lines.items():
            line = []
            lng_1, lat_1 = get_poi_position(stations[0])
            lng_2, lat_2 = get_poi_position(stations[-1])
            if lng_1 and lng_2:
                line.append(lng_1)
                line.append(lat_1)
                line.append(lng_2)
                line.append(lat_2)
            if len(line):
                lines_geometry.append(line)
                print(f"[info] process line {name}, total: {len(lines_geometry)}")

    with open(f'data/lines_geometry_{city}.json', 'w', encoding='utf-8') as f:
        f.write(str(lines_geometry))


def get_bus_info_baidu(start_lng, start_lat, end_lng, end_lat):
    # api documentation
    # http://lbsyun.baidu.com/index.php?title=webapi/direction-api-v2
    query_str = f'/direction/v2/transit?origin={start_lat},{start_lng}&destination={end_lat},{end_lng}&ak={ak}'
    encoded_str = urllib.parse.quote(query_str, safe="/:=&?#+!$,;'@()*[]")
    raw_str = encoded_str + sk
    sn = hashlib.md5(urllib.parse.quote_plus(raw_str).encode("utf-8")).hexdigest()
    url = urllib.parse.quote("http://api.map.baidu.com" + query_str + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
    try:
        response = requests.get(url)
        content = response.content
        content = dict(eval(content))
        steps = content['result']['routes'][0]['steps']
        route = []
        for step in steps:
            path = step[0]['path']
            polylines = path.split(';')
            for polyline in polylines:
                lng = float(polyline.split(',')[0])
                lat = float(polyline.split(',')[1])
                route.append(lng)
                route.append(lat)
        for i in range(-2, -len(route), -2):
            route[i] = int(1e4 * (route[i] - route[i - 2]))
            route[i + 1] = int(1e4 * (route[i + 1] - route[i - 1]))
        route[0] = int(1e4 * route[0])
        route[1] = int(1e4 * route[1])
        filter_route = []
        for i in range(0, len(route), 2):
            if route[i] != 0 or route[i + 1] != 0:
                filter_route.append(route[i])
                filter_route.append(route[i + 1])
        return filter_route
    except Exception as e:
        return None


def process_data():
    with open(f'data/lines_geometry_{city}.json') as f:
        lines = list(eval(f.read()))
    lines_data = []
    for line in lines:
        start_lng, start_lat = line[0], line[1]
        end_lng, end_lat = line[2], line[3]
        route = get_bus_info_baidu(start_lng, start_lat, end_lng, end_lat)
        print(f"[info] process data [{start_lng}, {start_lat}]-[{end_lng}, {end_lat}], total: {len(lines_data))}")
        if route and len(route) > 2:
            lines_data.append(route)

    with open(f'data/lines_data_{city}.json', 'w') as f:
        f.write(str(lines_data))
    return len(lines_data)


if __name__ == '__main__':
    print('start...')
    get_lines_stations()
    get_lines_stations_geometry()
    result_length = process_data()
    print(f'done... result_length={result_length}')
