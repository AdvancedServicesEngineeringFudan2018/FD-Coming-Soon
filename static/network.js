var GuestControlCoreNetworking = function (core, ws_location, params) {
    var cseq = 0;
    // dict to URL params
    // https://stackoverflow.com/questions/7045065/how-do-i-turn-a-javascript-dictionary-into-an-encoded-url-string
    var param_serialize = function (obj) {
        var str = [];
        for(var p in obj)
             str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        return str.join("&");
    }

    var deferHelper = function () {
        var deferredFunctions = [],
            addTask = function (f) { deferredFunctions.push(f); },
            runTasks = function () {
                for (var i = deferredFunctions.length; i > 0; --i) {
                    try {
                        deferredFunctions[i]();
                    }
                    catch (err) {
                        console.log("Unable to execute deferred function ", deferredFunctions[i], err.message);
                    }
                }
                deferredFunctions.length = 0;
            };
        return {
            addTask: addTask,
            runTasks: runTasks,
        };
    }

    // set up websocket
    var ws = {
        status: "disconnected",
        is_first_connect: true,
        connected: false,
        reconnect_interval: 0,
        timer: null,
        ping: {
            interval: 3000,
            timer: null,
            lastPingTimeStamp: 0,
            lastPongTimeStamp: 0,
            lastUpload: 0,
            lastDownload: 0,
            lastRTT: 0,
        },
        socket: null,
        waiting_list: [],
        paint_event_defer: null,
        debug_msg: "",
        online_number: 0,
    };

    var send = function (msg) {
        console.log("Sending: ", msg);
        if (ws.connected) {
            ws.socket.send(msg);
        }
        if (!ws.connected) {
            ws.waiting_list.push(msg);
        }
    };

    var sendControlMsg = function (msg, args) {
        // var t = msg + " " + Date.now();
        // if (args) t = t + " " + args;
        // send(t);
    };

    var setRole = function (role) {
        send(JSON.stringify({'role' : role, 'name' : params.id}));
    }

    var updatePosition = function(lat, lon) {
        ws.send({'role' : 'push', 'lat': lat, 'lng' : lon, 'speed' : 10, 'name' : params.id})
    }

    var wsSetup = function () {
        if (ws.paint_event_defer) ws.paint_event_defer.runTasks();
        ws.paint_event_defer = deferHelper();
        ws.connected = false;
        ws.status = "initializating...";
        // if WebSocket is still active, close it.
        if (ws.socket) {
            ws.socket.close();
        }
        ws.socket = new WebSocket(ws_location + "?" + param_serialize(params));

        var wsPing = function () {
            if (ws.connected) {
                ws.ping.lastPingTimeStamp = Date.now();
                sendControlMsg("PING");
            }
        }

        // connected
        ws.socket.addEventListener('open', function (event) {
            ws.connected = true;
            ws.reconnect_interval = 0;
            if (ws.is_first_connect) {
                sendControlMsg("INIT");
                ws.status = "pulling log...";
                sendControlMsg("PULL");
            } else {
                sendControlMsg("RECONNECT");
            }
            ws.status = "sending log...";
            console.log("WebSocket connected: ", event);
            while (ws.connected && ws.waiting_list.length > 0) {
                send(ws.waiting_list.shift());
            }
            ws.status = "connected";
            sendControlMsg("HELLO");
            ws.is_first_connect = false;
            ws.ping.timer = setTimeout(wsPing, ws.ping.interval);
        });

        // server disconnect
        ws.socket.addEventListener('close', function (event) {
            ws.is_connected = false;
            ws.status = "disconnected";
            ws.timer = setTimeout(wsSetup, ws.reconnect_interval);
        });

        // connection failure
        ws.socket.addEventListener('error', function (event) {
            ws.is_connected = false;
            ws.status = "error";
            // console.log("WebSocket error: ", event);
            if (ws.reconnect_interval <= 32000) {
                ws.reconnect_interval = ws.reconnect_interval + 500;
            }
        });

        // set up draw event listener
        p.addEventListener('updatePosition', function (e, f) {
            e.cseq = ++cseq;
            e.ctime = Date.now();
            var msg = JSON.stringify(e);
            setTimeout(send.bind(this, msg), 0);
            return true;
        });

        var serverMsgHandlers = {
            "track": function (msg) { 
                core.updatePosition(msg);
            },
        };

        ws.socket.addEventListener('message', function (event) {
            console.log("Got data: ", event.data);
            var msg = JSON.parse(event.data);
            for (var key in serverMsgHandlers) {
                if (msg["type"] == key) {
                    serverMsgHandlers[key](msg);
                }
            }
        });

        return ws;
    };

    return {
        init: wsSetup,
        setRole: setRole,
        updatePosition: updatePosition,
    }
}
