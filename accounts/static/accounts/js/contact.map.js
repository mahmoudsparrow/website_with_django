      function initMap() {
        var MDS = {lat: 30.0393831, lng: 31.2089514};
        var Metro = {lat: 30.0390069, lng: 31.2139081};  
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 17,
          center: Metro
        });
        var marker = new google.maps.Marker({
          position: MDS,
          map: map
        });
      }
    