const XLSX = require('xlsx');
const excelData = XLSX.readFile(".DataFiles_DuffieldHall_2023/DuffieldDataPivot.csv");
const keys = Object.keys(excelData.Sheets).map(name => ({
  name,
  data: XLSX.utils.sheet_to_json(
    excelData.Sheets[name]),
}));
keys.forEach(element => {
  console.log(element.data);
});

// todo: read directly from duffield hall file
// note - need to install xlsx

let duff_electricity = [942.7, 935.8, 948.8, 940.4]
let electricity_color = '#' + Math.floor(duff_electricity[0]).toString(16)

mapboxgl.accessToken = "pk.eyJ1Ijoia2V2aW54c2hhbmciLCJhIjoiY2xzb2FyeWkzMGRuZTJsbnl6enJvMzY1ZSJ9.oVhcnWifoSeqv554mrjaKg";

const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/light-v10',
  center: [-76.4735, 42.4534],
  zoom: 15
});

// Function to generate a random color
function getRandomColor() {
  let red = 0;
  let green = 0;
  let blue = 0;
  red = Math.floor(Math.random() * 256);
  green = Math.floor(Math.random() * 256);
  blue = Math.floor(Math.random() * 256);
  return [red, green, blue];
}

// Generate a random color for each level (0 to 23)
let [r1, g1, b1] = getRandomColor()
let [r2, g2, b2] = getRandomColor()
let levelColors = [[r1, g1, b1]];

for (let i = 1; i < 23; i++) {
  let progress = i / 23.0
  // linear interpolation for the colors
  let red = (1 - progress) * r1 + progress * r2
  let green = (1 - progress) * g1 + progress * g2
  let blue = (1 - progress) * b1 + progress * b2
  levelColors.push([red, green, blue])
}

levelColors.push([r2, g2, b2])
console.log(levelColors)
// convert colors to hex
let levelHexes = []
for (let i = 0; i < 24; i++) {
  rgb = levelColors[i]
  //print(rgb[0])
  console.log(rgb)
  hex = "#" + rgb[0].toString(16).substring(0, 2) + rgb[1].toString(16).substring(0, 2) + rgb[2].toString(16).substring(0, 2)
  console.log(hex)
  levelHexes.push(hex)
}

map.on('load', function () {
  map.addSource('cornellBuildings', {
    type: 'geojson',
    data: 'cugir-008163-geojson.json',
  });

  map.addLayer({
    id: 'buildings',
    type: 'fill',
    source: 'cornellBuildings',
    layout: {},
    paint: {
      'fill-color': levelHexes[0],
      'fill-opacity': 0.75,
    },
  });

  // Listen to the slider input
  document.getElementById('timeSlider').addEventListener('input', function () {
    const level = parseInt(this.value, 10);
    map.setPaintProperty('buildings', 'fill-color', levelHexes[level]);
    // map.setPaintProperty('buildings', 'fill-color', electricity_color);
  });
});