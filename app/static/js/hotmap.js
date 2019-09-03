var Hmap = function (t, i, e) {
    this.obj = {
        map: t,
        div: i,
        points: [],
        maxValue: 100,
        hmapDataMPoints: e
    };
    this.startExtent = null;
    this.mapScale = null;
    this.countOfNoshow = 0;
    this.isMoving = false;
    this.isLoadData = false;
    this.indexOfMarker = 1;
    this.heatmapOverlay = null;
    this.init = function () {
        var t = this.obj.div.parentElement;
        this.obj.div = document.createElement("div");
        this.obj.div.style.position = "absolute";
        this.obj.div.style.left = "0px";
        this.obj.div.style.top = "0px";
        this.obj.div.style.display = "none";
        this.setSize(this.obj.map.width, this.obj.map.height);
        t.appendChild(this.obj.div);
        this.heatmapOverlay = h337.create({
            container: this.obj.div
        });
        this.imgLayer = new Careland.Layer("point", "imgLayerHmap");
        this.obj.map.addLayer(this.imgLayer);
        this.getMapState();
        this.addEventListener(this)
    };
    this.setData = function (t, i) {
        this.obj.points = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ];
        for (var e in t) {
            if (t[e].scale && t[e].scale > 1 && t[e].scale < this.obj.points.length) {
                this.obj.points[t[e].scale].push(t[e])
            } else {
                for (var a = 0; a < this.obj.points.length; a++) {
                    this.obj.points[a].push(t[e])
                }
            }
        }
        if (i > 0) {
            this.obj.maxValue = i
        }
        this.showDatas(this);
        this.isLoadData = true
    };
    this.visible = function () {
        if (this.imgLayer) {
            return this.imgLayer.getVisible()
        } else return false
    };
    this.show = function () {
        if (this.imgLayer) {
            this.imgLayer.setVisible(true)
        }
    };
    this.hide = function () {
        if (this.imgLayer) {
            this.imgLayer.setVisible(false)
        }
    };
    this.getMapState = function () {
        this.startExtent = this.getBounds();
        this.mapScale = this.obj.map.getZoom()
    };
    this.getBounds = function () {
        if (this.obj.map) {
            return this.obj.map.getBounds()
        }
    };
    this.getPixels = function () {
        this.countOfNoshow = 0;
        var t = [];
        var i;
        for (var e = 0; e < this.obj.points[this.mapScale].length; e++) {
            var a = this.obj.points[this.mapScale][e];
            if (a.point.x < this.startExtent.maxX && a.point.y < this.startExtent.maxY && a.point.x > this.startExtent.minX && a.point.y > this.startExtent.minY) {
                if (this.obj.map) {
                    i = this.obj.map.pointToPixel(a.point)
                } else {
                    i = this.obj.map.pointToPixel(a.point)
                }
                t.push({
                    x: i.x,
                    y: i.y,
                    value: a.value,
                    radius: a.radius
                })
            } else {
                this.countOfNoshow++
            }
        }
        return t
    };
    this.showDatas = function (t) {
        var i = {
            max: this.obj.maxValue,
            data: this.getPixels()
        };
        this.heatmapOverlay.setData(i);
        var e = this.imgMarker;
        this.imgPoint = this.obj.map.pixelToPoint(new Careland.Pixel(0, 0));
        this.imgMarker = new Careland.Marker("image", "imgPointHMap" + this.indexOfMarker++);
        console.log(this.imgMarker);
        this.imgPointStyle = new Careland.PointStyle({
            src: this.heatmapOverlay._renderer.canvas.toDataURL("image/png"),
            borderSize: 0,
            offsetX: 0,
            offsetY: 0
        });
        this.imgMarker.setStyle(this.imgPointStyle);
        this.imgMarker.setPoint(this.imgPoint);
        this.imgLayer.add(this.imgMarker);
        var a = 0;
        document.getElementById("Point_" + this.imgMarker.id).children[0].onload = function () {
            if (e) {
                if (a++ != 0) {
                    if (e && document.getElementById("Point_" + e.id) && document.getElementById("Point_" + e.id).children && document.getElementById("Point_" + e.id).children.length > 0) {
                        document.getElementById("Point_" + e.id).children[0].style.opacity = "0"
                    }
                    document.getElementById("Point_" + t.imgMarker.id).children[0].style.opacity = "0.7";
                    t.imgLayer.remove(e.id);
                    e = null;
                    delete e
                } else {
                    document.getElementById("Point_" + t.imgMarker.id).children[0].style.opacity = "0"
                }
            } else {
                document.getElementById("Point_" + t.imgMarker.id).children[0].style.opacity = "0.7"
            }
        }
    };
    this.setSize = function (t, i) {
        this.obj.div.style.width = t + "px";
        this.obj.div.style.height = i + "px";
        if (this.obj.heatmapOverlay) {
            this.obj.heatmapOverlay.setCanvasSize(t, i)
        }
        if (this.isLoadData && this.countOfNoshow > 0) {
            this.startExtent = this.getBounds();
            this.showDatas(this)
        }
    };
    this.addEventListener = function (t) {
        this.obj.map.addEventListener("zoomstart", function () {
            if (t.isLoadData && t.imgLayer) {
                t.imgLayer.clear();
                console.log('1');
            }
        });
        this.obj.map.addEventListener("movestart", function () {
            if (t.isLoadData) { }
        });
        this.obj.map.addEventListener("zoomend", function () {
            t.getMapState();
            if (t.isLoadData) {
                t.showDatas(t)
                console.log('2');
            }
        });
        this.obj.map.addEventListener("moveend", function () {
            if (t.isLoadData && t.countOfNoshow > 0) {
                t.startExtent = t.getBounds();
                t.showDatas(t);
                console.log('3');
            }
        })
    }
};
(function (t, i, e) {
    if (typeof module !== "undefined" && module.exports) {
        module.exports = e()
    } else if (typeof define === "function" && define.amd) {
        define(e)
    } else {
        i[t] = e()
    }
})("h337", this, function () {
    var n = {
        defaultRadius: 40,
        defaultRenderer: "canvas2d",
        defaultGradient: {
            .25: "rgb(0,0,255)",
            .55: "rgb(0,255,0)",
            .85: "yellow",
            1: "rgb(255,0,0)"
        },
        defaultMaxOpacity: 1,
        defaultMinOpacity: 0,
        defaultBlur: .85,
        defaultXField: "x",
        defaultYField: "y",
        defaultValueField: "value",
        plugins: {}
    };
    var s = function t() {
        var i = function t(i) {
            this._coordinator = {};
            this._data = [];
            this._radi = [];
            this._min = 0;
            this._max = 1;
            this._xField = i["xField"] || i.defaultXField;
            this._yField = i["yField"] || i.defaultYField;
            this._valueField = i["valueField"] || i.defaultValueField;
            if (i["radius"]) {
                this._cfgRadius = i["radius"]
            }
        };
        var l = n.defaultRadius;
        i.prototype = {
            _organiseData: function (t, i) {
                var e = t[this._xField];
                var a = t[this._yField];
                var r = this._radi;
                var n = this._data;
                var s = this._max;
                var o = this._min;
                var h = t[this._valueField] || 1;
                var d = t.radius || this._cfgRadius || l;
                if (!n[e]) {
                    n[e] = [];
                    r[e] = []
                }
                if (!n[e][a]) {
                    n[e][a] = h;
                    r[e][a] = d
                } else {
                    n[e][a] += h
                } if (n[e][a] > s) {
                    if (!i) {
                        this._max = n[e][a]
                    } else {
                        this.setDataMax(n[e][a])
                    }
                    return false
                } else {
                    return {
                        x: e,
                        y: a,
                        value: h,
                        radius: d,
                        min: o,
                        max: s
                    }
                }
            },
            _unOrganizeData: function () {
                var t = [];
                var i = this._data;
                var e = this._radi;
                for (var a in i) {
                    for (var r in i[a]) {
                        t.push({
                            x: a,
                            y: r,
                            radius: e[a][r],
                            value: i[a][r]
                        })
                    }
                }
                return {
                    min: this._min,
                    max: this._max,
                    data: t
                }
            },
            _onExtremaChange: function () {
                this._coordinator.emit("extremachange", {
                    min: this._min,
                    max: this._max
                })
            },
            addData: function () {
                if (arguments[0].length > 0) {
                    var t = arguments[0];
                    var i = t.length;
                    while (i--) {
                        this.addData.call(this, t[i])
                    }
                } else {
                    var e = this._organiseData(arguments[0], true);
                    if (e) {
                        this._coordinator.emit("renderpartial", {
                            min: this._min,
                            max: this._max,
                            data: [e]
                        })
                    }
                }
                return this
            },
            setData: function (t) {
                var i = t.data;
                var e = i.length;
                this._data = [];
                this._radi = [];
                for (var a = 0; a < e; a++) {
                    this._organiseData(i[a], false)
                }
                this._max = t.max;
                this._min = t.min || 0;
                this._onExtremaChange();
                this._coordinator.emit("renderall", this._getInternalData());
                return this
            },
            removeData: function () { },
            setDataMax: function (t) {
                this._max = t;
                this._onExtremaChange();
                this._coordinator.emit("renderall", this._getInternalData());
                return this
            },
            setDataMin: function (t) {
                this._min = t;
                this._onExtremaChange();
                this._coordinator.emit("renderall", this._getInternalData());
                return this
            },
            setCoordinator: function (t) {
                this._coordinator = t
            },
            _getInternalData: function () {
                return {
                    max: this._max,
                    min: this._min,
                    data: this._data,
                    radi: this._radi
                }
            },
            getData: function () {
                return this._unOrganizeData()
            }
        };
        return i
    }();
    var e = function t() {
        var s = function (t) {
            var i = t.gradient || t.defaultGradient;
            var e = document.createElement("canvas");
            var a = e.getContext("2d");
            e.width = 256;
            e.height = 1;
            var r = a.createLinearGradient(0, 0, 256, 1);
            for (var n in i) {
                r.addColorStop(n, i[n])
            }
            a.fillStyle = r;
            a.fillRect(0, 0, 256, 1);
            return a.getImageData(0, 0, 256, 1).data
        };
        var v = function (t, i) {
            var e = document.createElement("canvas");
            var a = e.getContext("2d");
            var r = t;
            var n = t;
            e.width = e.height = t * 2;
            if (i == 1) {
                a.beginPath();
                a.arc(r, n, t, 0, 2 * Math.PI, false);
                a.fillStyle = "rgba(0,0,0,1)";
                a.fill()
            } else {
                var s = a.createRadialGradient(r, n, t * i, r, n, t);
                s.addColorStop(0, "rgba(0,0,0,1)");
                s.addColorStop(1, "rgba(0,0,0,0)");
                a.fillStyle = s;
                a.fillRect(0, 0, 2 * t, 2 * t)
            }
            return e
        };
        var i = function (t) {
            var i = [];
            var e = t.min;
            var a = t.max;
            var r = t.radi;
            var t = t.data;
            var n = Object.keys(t);
            var s = n.length;
            while (s--) {
                var o = n[s];
                var h = Object.keys(t[o]);
                var d = h.length;
                while (d--) {
                    var l = h[d];
                    var u = t[o][l];
                    var c = r[o][l];
                    i.push({
                        x: o,
                        y: l,
                        value: u,
                        radius: c
                    })
                }
            }
            return {
                min: e,
                max: a,
                data: i
            }
        };

        function e(t) {
            var i = t.container;
            var e = this.shadowCanvas = document.createElement("canvas");
            var a = this.canvas = t.canvas || document.createElement("canvas");
            var r = this._renderBoundaries = [1e4, 1e4, 0, 0];
            var n = getComputedStyle(t.container) || {};
            a.className = "heatmap-canvas";
            this._width = a.width = e.width = +n.width.replace(/px/, "");
            this._height = a.height = e.height = +n.height.replace(/px/, "");
            this.shadowCtx = e.getContext("2d");
            this.ctx = a.getContext("2d");
            a.style.cssText = e.style.cssText = "position:absolute;left:0;top:0;";
            i.style.position = "relative";
            i.appendChild(a);
            this._palette = s(t);
            this._templates = {};
            this._setStyles(t)
        }
        e.prototype = {
            renderPartial: function (t) {
                this._drawAlpha(t);
                this._colorize()
            },
            renderAll: function (t) {
                this._clear();
                this._drawAlpha(i(t));
                this._colorize()
            },
            _updateGradient: function (t) {
                this._palette = s(t)
            },
            updateConfig: function (t) {
                if (t["gradient"]) {
                    this._updateGradient(t)
                }
                this._setStyles(t)
            },
            setDimensions: function (t, i) {
                this._width = t;
                this._height = i;
                this.canvas.width = this.shadowCanvas.width = t;
                this.canvas.height = this.shadowCanvas.height = i
            },
            _clear: function () {
                this.shadowCtx.clearRect(0, 0, this._width, this._height);
                this.ctx.clearRect(0, 0, this._width, this._height)
            },
            _setStyles: function (t) {
                this._blur = t.blur == 0 ? 0 : t.blur || t.defaultBlur;
                if (t.backgroundColor) {
                    this.canvas.style.backgroundColor = t.backgroundColor
                }
                this._opacity = (t.opacity || 0) * 255;
                this._maxOpacity = (t.maxOpacity || t.defaultMaxOpacity) * 255;
                this._minOpacity = (t.minOpacity || t.defaultMinOpacity) * 255;
                this._useGradientOpacity = !!t.useGradientOpacity
            },
            _drawAlpha: function (t) {
                var i = this._min = t.min;
                var e = this._max = t.max;
                var t = t.data || [];
                var a = t.length;
                var r = 1 - this._blur;
                while (a--) {
                    var n = t[a];
                    var s = n.x;
                    var o = n.y;
                    var h = n.radius;
                    var d = Math.min(n.value, e);
                    var l = s - h;
                    var u = o - h;
                    var c = this.shadowCtx;
                    var f;
                    if (!this._templates[h]) {
                        this._templates[h] = f = v(h, r)
                    } else {
                        f = this._templates[h]
                    }
                    c.globalAlpha = (d - i) / (e - i);
                    c.drawImage(f, l, u);
                    if (l < this._renderBoundaries[0]) {
                        this._renderBoundaries[0] = l
                    }
                    if (u < this._renderBoundaries[1]) {
                        this._renderBoundaries[1] = u
                    }
                    if (l + 2 * h > this._renderBoundaries[2]) {
                        this._renderBoundaries[2] = l + 2 * h
                    }
                    if (u + 2 * h > this._renderBoundaries[3]) {
                        this._renderBoundaries[3] = u + 2 * h
                    }
                }
            },
            _colorize: function () {
                var t = this._renderBoundaries[0];
                var i = this._renderBoundaries[1];
                var e = this._renderBoundaries[2] - t;
                var a = this._renderBoundaries[3] - i;
                var r = this._width;
                var n = this._height;
                var s = this._opacity;
                var o = this._maxOpacity;
                var h = this._minOpacity;
                var d = this._useGradientOpacity;
                if (t < 0) {
                    t = 0
                }
                if (i < 0) {
                    i = 0
                }
                if (t + e > r) {
                    e = r - t
                }
                if (i + a > n) {
                    a = n - i
                }
                var l = this.shadowCtx.getImageData(t, i, e, a);
                var u = l.data;
                var c = u.length;
                var f = this._palette;
                for (var v = 3; v < c; v += 4) {
                    var m = u[v];
                    var _ = m * 4;
                    if (!_) {
                        continue
                    }
                    var g;
                    if (s > 0) {
                        g = s
                    } else {
                        if (m < o) {
                            if (m < h) {
                                g = h
                            } else {
                                g = m
                            }
                        } else {
                            g = o
                        }
                    }
                    u[v - 3] = f[_];
                    u[v - 2] = f[_ + 1];
                    u[v - 1] = f[_ + 2];
                    u[v] = d ? f[_ + 3] : g
                }
                l.data = u;
                this.ctx.putImageData(l, t, i);
                this._renderBoundaries = [1e3, 1e3, 0, 0]
            },
            getValueAt: function (t) {
                var i;
                var e = this.shadowCtx;
                var a = e.getImageData(t.x, t.y, 1, 1);
                var r = a.data[3];
                var n = this._max;
                var s = this._min;
                i = Math.abs(n - s) * (r / 255) >> 0;
                return i
            },
            getDataURL: function () {
                return this.canvas.toDataURL()
            }
        };
        return e
    }();
    var o = function t() {
        var i = false;
        if (n["defaultRenderer"] === "canvas2d") {
            i = e
        }
        return i
    }();
    var h = {
        merge: function () {
            var t = {};
            var i = arguments.length;
            for (var e = 0; e < i; e++) {
                var a = arguments[e];
                for (var r in a) {
                    t[r] = a[r]
                }
            }
            return t
        }
    };
    var i = function t() {
        var a = function t() {
            function i() {
                this.cStore = {}
            }
            i.prototype = {
                on: function (t, i, e) {
                    var a = this.cStore;
                    if (!a[t]) {
                        a[t] = []
                    }
                    a[t].push(function (t) {
                        return i.call(e, t)
                    })
                },
                emit: function (t, i) {
                    var e = this.cStore;
                    if (e[t]) {
                        var a = e[t].length;
                        for (var r = 0; r < a; r++) {
                            var n = e[t][r];
                            n(i)
                        }
                    }
                }
            };
            return i
        }();
        var r = function (i) {
            var t = i._renderer;
            var e = i._coordinator;
            var a = i._store;
            e.on("renderpartial", t.renderPartial, t);
            e.on("renderall", t.renderAll, t);
            e.on("extremachange", function (t) {
                i._config.onExtremaChange && i._config.onExtremaChange({
                    min: t.min,
                    max: t.max,
                    gradient: i._config["gradient"] || i._config["defaultGradient"]
                })
            });
            a.setCoordinator(e)
        };

        function i() {
            var t = this._config = h.merge(n, arguments[0] || {});
            this._coordinator = new a;
            if (t["plugin"]) {
                var i = t["plugin"];
                if (!n.plugins[i]) {
                    throw new Error("Plugin '" + i + "' not found. Maybe it was not registered.")
                } else {
                    var e = n.plugins[i];
                    this._renderer = new e.renderer(t);
                    this._store = new e.store(t)
                }
            } else {
                this._renderer = new o(t);
                this._store = new s(t)
            }
            r(this)
        }
        i.prototype = {
            addData: function () {
                this._store.addData.apply(this._store, arguments);
                return this
            },
            removeData: function () {
                this._store.removeData && this._store.removeData.apply(this._store, arguments);
                return this
            },
            setData: function () {
                this._store.setData.apply(this._store, arguments);
                return this
            },
            setDataMax: function () {
                this._store.setDataMax.apply(this._store, arguments);
                return this
            },
            setDataMin: function () {
                this._store.setDataMin.apply(this._store, arguments);
                return this
            },
            configure: function (t) {
                this._config = h.merge(this._config, t);
                this._renderer.updateConfig(this._config);
                this._store._cfgRadius = this._config["radius"];
                this._coordinator.emit("renderall", this._store._getInternalData());
                return this
            },
            repaint: function () {
                this._coordinator.emit("renderall", this._store._getInternalData());
                return this
            },
            getData: function () {
                return this._store.getData()
            },
            getDataURL: function () {
                return this._renderer.getDataURL()
            },
            getValueAt: function (t) {
                if (this._store.getValueAt) {
                    return this._store.getValueAt(t)
                } else if (this._renderer.getValueAt) {
                    return this._renderer.getValueAt(t)
                } else {
                    return null
                }
            },
            setCanvasSize: function (t, i) {
                this._renderer.setDimensions(t, i)
            },
            setCanvasDisplay: function (t) {
                this._renderer.canvas.style.display = t
            },
            setCanvasOpacity: function (t) {
                this._renderer.canvas.style.opacity = t
            }
        };
        return i
    }();
    var t = {
        create: function (t) {
            return new i(t)
        },
        register: function (t, i) {
            n.plugins[t] = i
        }
    };
    return t
});