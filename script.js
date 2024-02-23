mapboxgl.accessToken = "pk.eyJ1Ijoia2V2aW54c2hhbmciLCJhIjoiY2xzb2FyeWkzMGRuZTJsbnl6enJvMzY1ZSJ9.oVhcnWifoSeqv554mrjaKg";

const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/light-v10',
  center: [-76.4735, 42.4534],
  zoom: 15
});

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
      // Initially set a default color; will be updated by the slider
      'fill-color': '#0000FF', // Dark blue
      'fill-opacity': 0.75
    }
  });

  // Update building color based on the slider
  document.getElementById('timeSlider').addEventListener('input', function () {
    const hour = parseInt(this.value, 10);
    const colorScale = d3.scaleLinear()
      .domain([0, 23]) // Assuming 0 to 23 hours for simplicity
      .range(['#0000FF', '#FFFF00']); // Dark blue to bright yellow

    const newColor = colorScale(hour);

    map.setPaintProperty('building-outlines', 'fill-color', newColor);
  });
});


