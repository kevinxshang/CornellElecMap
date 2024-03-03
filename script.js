mapboxgl.accessToken = "pk.eyJ1Ijoia2V2aW54c2hhbmciLCJhIjoiY2xzb2FyeWkzMGRuZTJsbnl6enJvMzY1ZSJ9.oVhcnWifoSeqv554mrjaKg";

const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/light-v10',
  center: [-76.4735, 42.4534],
  zoom: 15
});

// Function to generate a random color
function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

// Generate a random color for each level (0 to 23)
const levelColors = Array.from({ length: 24 }, () => getRandomColor());

map.on('load', function () {
  map.addSource('cornellBuildings', {
    type: 'geojson',
    data: 'cugir-008163-geojson.json',
  });

  map.addLayer({
    id: 'buildings',

map.on('load', function () {
  map.addSource('cornellBuildings', {
    type: 'geojson',
    data: 'cugir-008163-geojson.geojson' // Adjust this path to your GeoJSON file
  });

  // Add a layer to visualize the building outlines
  map.addLayer({
    id: 'building-outlines',
    type: 'fill',
    source: 'cornellBuildings',
    layout: {},
    paint: {
      'fill-color': levelColors[0],
      'fill-opacity': 0.75,
    },
  });

  // Listen to the slider input
  document.getElementById('timeSlider').addEventListener('input', function () {
    const level = parseInt(this.value, 10);
    map.setPaintProperty('buildings', 'fill-color', levelColors[level]);
  });
});
