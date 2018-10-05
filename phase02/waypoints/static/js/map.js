/*
JavaScript for rendering data on map and making AJAX requests.
*/

var map;
var markers = [];
var renderers = [];

function initMap() {
    // This function initializes the map

    map = new google.maps.Map($("#map")[0], {
      center: {lat: 42.880230, lng: -78.878738},
      zoom: 8
    });
}

function requestDirections() {
    // This function sends an AJAX request to the web server
    // to get the directions json

    origin = $("#origin").val();
    destination = $("#destination").val();

    var csrftoken = Cookies.get("csrftoken");

    $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    $.ajax({
        type: "GET",
        url: "",
        data: {
            "origin": origin,
            "destination": destination
        },
        success: function(result) {
            renderDirections(result);
        }
    });
}

function convertRoutes(result) {
    // This function converts the json data for use by the DirectionsRenderer object
    
    result.forEach(function(route) {
        route.bounds = asBounds(route.bounds);

        route.overview_path = asPath(route.overview_polyline);

        route.legs.forEach(function(leg) {
            leg.start_location = asLatLng(leg.start_location);
            leg.end_location = asLatLng(leg.end_location);

            leg.steps.forEach(function(step) {
                step.start_location = asLatLng(leg.start_location);
                step.end_location = asLatLng(leg.end_location);
                step.path = asPath(step.polyline);
            });
        });
    });

    return result;
}

function asBounds(boundsObject) {
    // This function converts the json data for use by the DirectionsRenderer object

    return new google.maps.LatLngBounds(asLatLng(boundsObject.southwest),
                                        asLatLng(boundsObject.northeast));
}

function asLatLng(latlngObject) {
    // This function converts the json data for use by the DirectionsRenderer object

    return new google.maps.LatLng(latlngObject.lat, latlngObject.lng);
}

function asPath(encodedPolyObject) {
    // This function converts the json data for use by the DirectionsRenderer object

    return google.maps.geometry.encoding.decodePath(encodedPolyObject.points);
}

function getRequest() {
    // This function converts the json data for use by the DirectionsRenderer object

    return {origin: $("#origin").val(), 
            destination: $("#destination").val(), 
            travelMode: "DRIVING"};
}

function renderDirections(result) {
    // This function renders the directions data on the map

    markers.forEach(function(marker) {
        marker.setMap(null);
    });

    renderers.forEach(function(renderer) {
        renderer.setMap(null);
    });

    var directionsDisplay = new google.maps.DirectionsRenderer();

    var convertedRoutes = convertRoutes(result);

    directionsDisplay.setOptions({
        directions: {
            routes: convertedRoutes,
            request: getRequest()
        },

        draggable: true,
        map: map
    });

    renderers.push(directionsDisplay);

    addMarkers(convertedRoutes[0].overview_path);
}

function addMarkers(overview_path) {
    // This function adds 12 evenly spaced markers to the map

    var mod = Math.floor(overview_path.length / 12);

    var index = 2 * mod;

    var window = new google.maps.InfoWindow;

    for(; index < (overview_path.length - mod); index += mod) {
        var marker = new google.maps.Marker({
            position: {'lat': overview_path[index].lat(), 'lng': overview_path[index].lng()},
            map: map
        });

        marker.addListener('click', function(markerData) {
            var lat = markerData.latLng.lat();
            var lng = markerData.latLng.lng();
            window.close();
            setWeatherContent(lat, lng, window);
            window.setPosition({'lat': lat, 'lng': lng});
            window.open(map);
        });

        markers.push(marker);
    }
}

function setWeatherContent(lat, lng, window) {
    // This method sends an AJAX request for the weather data when a marker is clicked

    $.ajax({
        type: "GET",
        url: "",
        data: {
            "lat": lat,
            "lng": lng
        }, 
        success: function(result) {

            var content = "<p>General: " + result.weather[0].description + "</p>";
            content += "<p>Wind: " + result.wind.speed.toString() + " m/s</p>";
            content += "<p>Temperature: " + (result.main.temp - 273.15).toFixed(2) + " C</p>";
            content += "<p>High Temp: " + (result.main.temp_max - 273.15).toFixed(2) + " C</p>";
            content += "<p>Low Temp: " + (result.main.temp_min - 273.15).toFixed(2) + " C</p>";
            content += "<p>Pressure: " + result.main.pressure.toString() + " hpa</p>";

            window.setContent(content);
        }
    });
}