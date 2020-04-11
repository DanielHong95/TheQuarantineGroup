// d3 map
map = {
    const context = DOM.context2d(width, height);
    const path = d3.geoPath(projection, context);
    context.save();
    context.beginPath(), path(outline), context.clip(), context.fillStyle = "#fff", context.fillRect(0, 0, width, height);
    context.beginPath(), path(graticule), context.strokeStyle = "#ccc", context.stroke();
    context.beginPath(), path(land), context.fillStyle = "#000", context.fill();
    context.restore();
    context.beginPath(), path(outline), context.strokeStyle = "#000", context.stroke();
    return context.canvas;
  }
  height = {
    const [[x0, y0], [x1, y1]] = d3.geoPath(projection.fitWidth(width, outline)).bounds(outline);
    const dy = Math.ceil(y1 - y0), l = Math.min(Math.ceil(x1 - x0), dy);
    projection.scale(projection.scale() * (l - 1) / l).precision(0.2);
    return dy;
  }
  outline = ({type: "Sphere"})
  graticule = Object {
    type: "MultiLineString"
    coordinates: Array(53) [Array(3), Array(3), Array(3), Array(3), Array(145), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), Array(3), …]
  }
  land = topojson.feature(world, world.objects.land)
  world = FileAttachment("land-50m.json").json()
  topojson = require("topojson-client@3")
  d3 = require("d3-geo@1", "d3-geo-projection@2")
  import {projectionInput} from "@d3/projection-comparison"
