mapboxgl.accessToken = 'pk.eyJ1IjoicHVudGhhbmFrb3JuIiwiYSI6ImNsdTc2ZjMxMTAybmIycXFteHp0aGphZnkifQ.QLr5XN7GOEi9MONf2mygjQ';

// Initialize the map
const map = new mapboxgl.Map({
  container: 'map', // The ID of the container element
  style: 'mapbox://styles/mapbox/light-v10', // The style URL
  center: [-76.4735, 42.4534], // Starting position [lng, lat]
  zoom: 15 // Starting zoom level
});

// Assuming we have a function to convert electricity usage to a color
function usageToColor(usage) {
  // Define the range of your electricity usage here and return a color based on the usage
  // This is a simple example; you might want to use a more sophisticated scale
  if (usage < 100) return '#00ff00'; // Green for low usage
  if (usage < 200) return '#ffff00'; // Yellow for medium
  return '#ff0000'; // Red for high usage
}

map.on('load', function () {
  map.addSource('buildingData', {
    type: 'geojson',
    data: 'cugir-008163-geojson' // Make sure this path is correct
  });

  map.addLayer({
    id: 'electricity-usage',
    type: 'fill',
    source: 'buildingData',
    layout: {},
    paint: {
      // Use a data-driven style for the fill-color, based on the 'electricUsage' property
      'fill-color': ['get', 'electricUsage'], // Replace 'electricUsage' with the property from your GeoJSON
      'fill-opacity': 0.75
    }
  });
});
