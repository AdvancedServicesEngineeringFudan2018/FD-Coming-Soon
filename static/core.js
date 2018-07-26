"use strict";
var GuestControlCore = function (map) {
    // helper functions
    var helper = {

        sort_by_server_timestamp: function (a, b) {
            var a_time = a.stime || a.ctime || (a.x + a.y);
            var b_time = b.stime || b.ctime || (b.x + b.y);
            var ret = a_time - b_time;
            if (ret == 0) {
                a_time += a.ctime;
                b_time += b.ctime;
                ret = a_time - b_time;
            }
            return ret;
        },

        // merge sort
        // from https://github.com/millermedeiros/amd-utils/blob/master/src/array/sort.js
        mergeSort: function (arr, compareFn) {
            var defaultCompare = function (a, b) {
                return a < b ? -1 : (a > b ? 1 : 0);
            };

            var merge = function (left, right, compareFn) {
                var result = [];

                while (left.length && right.length) {
                    if (compareFn(left[0], right[0]) <= 0) {
                        // if 0 it should preserve same order (stable)
                        result.push(left.shift());
                    } else {
                        result.push(right.shift());
                    }
                }

                if (left.length) {
                    result.push.apply(result, left);
                }

                if (right.length) {
                    result.push.apply(result, right);
                }

                return result;
            };

            if (arr.length < 2) {
                return arr;
            }

            if (compareFn == null) {
                compareFn = defaultCompare;
            }

            var mid, left, right;

            mid = ~~(arr.length / 2);
            left = this.mergeSort(arr.slice(0, mid), compareFn);
            right = this.mergeSort(arr.slice(mid, arr.length), compareFn);

            return merge(left, right, compareFn);
        },

        // remove element from array
        // removeFromArray(array, element1, [element2, [element3, [...]]])
        removeFromArray: function (array) {
            var what, a = arguments,
                L = a.length,
                ax;
            while (L > 1 && arr.length) {
                what = a[--L];
                while ((ax = arr.indexOf(what)) !== -1) {
                    arr.splice(ax, 1);
                }
            }
            return arr;
        },

        // copy object properties
        objCopy: function (dest, src) {
            for (var attr in src) {
                dest[attr] = src[attr];
            }
        },
    };

    // event flow
    var events = {
        // server commited
        commited: [],
        // on commit process
        commiting: [],
        // pre-rendered but not commited
        queuing: [],
        // last unfinished event point
        lastPoint: null,
    };

    var vehicles = {

    };
    
    // background process
    var backgroundProcesses = {
        redraw: {
            enabled: true,
            interval: 50,
            func: function (p) {
                // for (var i in vehicles) {
                //     map.getSource(i).setData(vehicles[i]["geojson"]);
                // }
            },
            properties: {
                lastBackgroundFrame: null,
            },
        },
    };

    var initBackgroundProcesses = function () {
        for (var n in backgroundProcesses) {
            var p = backgroundProcesses[n];
            // create timed function for every background process
            p.timeFunc = (function (isForced) {
                if (this.func && (isForced || this.enabled)) this.func(this.properties);
                this.timer = window.setTimeout(this.timeFunc, this.interval);
            }).bind(p);
            // launch them asyncly
            p.timer = window.setTimeout(p.timeFunc, 1);
        }
    };

    var triggerBackgroundProcess = function (name) {
        window.clearTimeout(backgroundProcesses[name].timer);
        backgroundProcesses[name].timeFunc(true);
    }

    var onresize = function (e) {
        if (e) triggerEvent('redraw');
    };

    // global getter and setter
    // all objects whose attributes may be public accessable should be put in publicAccessibleObjects
    // then use publicProperties to define public name and its access route
    // use get('name') and set('name', 'newValue') outside
    var publicAccessibleObjects = {
    };

    var publicProperties = {
    };

    var get = function (property) {
        var path = publicProperties[property].split(".");
        var obj = publicAccessibleObjects;
        while (path.length) {
            obj = obj[path.shift()];
        }
        return obj;
    };

    var set = function (property, newValue) {
        var path = publicProperties[property].split(".");
        var obj = publicAccessibleObjects;
        while (path.length > 1) {
            obj = obj[path.shift()];
        }
        obj[path[0]] = newValue;
    };

    // user event processing
    var initUserEvents = function () {
        window.addEventListener('resize', function (e) {
            triggerEvent('resize', e);
        });
    };

    // event listeners
    var eventListeners = {
        resize: [onresize],
        redraw: [function () { triggerBackgroundProcess('redraw'); }],
    };

    // event listeners operation
    var addEventListener = function (e, f) {
        if (eventListeners[e]) {
            eventListeners[e].push(f);
        } else {
            eventListeners[e] = [f];
        }
        return function () {
            removeEventListener(e, f);
        };
    };

    var removeEventListener = function (e, f) {
        if (eventListeners[e]) {
            helper.removeFromArray(eventListeners[e], f);
        }
    };

    var triggerEvent = function (e) {
        var ret = true;
        if (eventListeners[e]) {
            for (var i in eventListeners[e]) {
                
                var cur_ret = eventListeners[e][i].apply(this, Array.from(arguments).slice(1));
                ret = ret && cur_ret;
            }
        }
        return ret;
    };

    // object initialize
    var init = function () {
        triggerEvent('resize');

        initBackgroundProcesses();
        initUserEvents();
    };

    return {
        init: init,
        get: get,
        set: set,
        addEventListener: addEventListener,
        removeEventListener: removeEventListener,
        triggerEvent: triggerEvent,
        updatePosition: function (event) { 
            if (!(event["name"] in vehicles)) {
                vehicles[event["name"]] = {
                    "geojson": {
                        "type": "FeatureCollection",
                        
                        "features": [{
                            "properties": {},
                            "type": "Feature",
                            "geometry": {
                                "type": "LineString",
                                "coordinates": [
                                ]
                            }
                        }]
                    },
                    "points": [],
                    "maplayer": {
                        'id': event["name"],
                        'type': 'line',
                        'source': {
                            'type': 'geojson',
                            'data': {
                                "type": "FeatureCollection",
                                "features": [{
                                    "properties": {},
                                    "type": "Feature",
                                    "geometry": {
                                        "type": "LineString",
                                        "coordinates": [
                                        ]
                                    }
                                }]
                            }
                        },
                        'layout': {
                            'line-cap': 'round',
                            'line-join': 'round'
                        },
                        'paint': {
                            'line-color': '#ed6498',
                            'line-width': 5,
                            'line-opacity': .8
                        }
                    },
                };
                
                map.addLayer(vehicles[event["name"]]["maplayer"]);
            } 
            vehicles[event["name"]]["points"].push(event);
            vehicles[event["name"]]["geojson"].features[0].geometry.coordinates.push([event.lng, event.lat]);
            map.getSource(event["name"]).setData(vehicles[event["name"]]["geojson"]);
            
            // console.log(vehicles[event["name"]]);
        },
    };
};
