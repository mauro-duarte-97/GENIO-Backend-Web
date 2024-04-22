
function initMap() {
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: {lat: -34.590747, lng: -58.4174746}  // Centro inicial del mapa
    });

    // Guarda la referencia del mapa en una variable global si necesitas acceder desde otras funciones
    window.myMap = map;
}

function setLocation(latitude, longitude) {
    // Centra el mapa en las nuevas coordenadas
    window.myMap.setCenter({lat: latitude, lng: longitude});
}

// Inicializa el mapa cuando la ventana carga
window.onload = initMap;
