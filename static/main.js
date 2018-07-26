"use strict";

var hasClass = function (el, className) {
    if (el) {
        if (el.classList)
            return el.classList.contains(className);
        else
            return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
    } else return false;
};

var addClass = function (el, className) {
    if (el.classList)
        el.classList.add(className);
    else if (!hasClass(el, className)) el.className += " " + className;
};

var removeClass = function (el, className) {
    if (el.classList)
        el.classList.remove(className);
    else if (hasClass(el, className)) {
        var reg = new RegExp('(\\s|^)' + className + '(\\s|$)');
        el.className = el.className.replace(reg, ' ');
    }
};

var resetEnabledButton = function () {
    var elems = document.getElementsByClassName('round-button');
    for (var i in elems) {
        if (elems.hasOwnProperty(i)) {
            removeClass(elems[i], 'round-button-selected');
        }
    }
};

var p;
var onReady = function () {

    // check URL params
    var getURLParameter = function (name) {
        return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
    }

    
    

    // disable context menu
    window.addEventListener('contextmenu', function (e) {
        e.preventDefault();
        e.stopPropagation();
        return false;
    });

    // init map
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v9',
        center: [121.59, 31.178],
        zoom: 14
    });

    map.on('load', function () {
        $.getJSON("../geo/shanghaitech.geojson", null, function(gdata) {
            map.addLayer({
                'id': 'maine',
                'type': 'fill',
                'source': {
                    'type': 'geojson',
                    'data': gdata,
                },
                'layout': {},
                'paint': {
                    'fill-color': '#088',
                    'fill-opacity': 0.8
                }
            });
        })

        s.setRole("pull");
    });

    // set up paint canvas
    p = GuestControlCore(map);
    p.init();

    // generate UUID for this client
    var uuid = localStorage.getItem('uuid');
    if (!uuid) {
        uuid = UUID.generate().toString();
        localStorage.setItem('uuid', uuid);
    }

    // WebSocket URL
    var ws_location = (basesURIProtocol.toLowerCase().startsWith("https") ? "wss://" : "ws://") + baseURI + "/status";
    console.log(ws_location);

    var s = GuestControlCoreNetworking(p, ws_location, {
        id: uuid,
    });

    s.init();

    
};

(function ready(fn) {
    if (document.readyState != 'loading'){
        fn();
    } else if (document.addEventListener) {
        document.addEventListener('DOMContentLoaded', fn);
    } else {
        document.attachEvent('onreadystatechange', function() {
          if (document.readyState != 'loading')
              fn();
        });
    }
})(onReady);
