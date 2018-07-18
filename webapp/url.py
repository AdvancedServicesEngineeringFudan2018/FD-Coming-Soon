# -*- coding: UTF-8 -*-
import json
from flask import request, render_template
from webapp.heatmap import get_city_polylines, get_city_cells

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/city_cells', methods=['POST'])
def city_cells():
    req = request.json if request.json else {}
    keywords = req.get('keywords', '上海')
    polylines = get_city_polylines(keywords)
    cells = [cell.items() for cell in get_city_cells(polylines)]
    return json.dumps(cells, ensure_ascii=False)
