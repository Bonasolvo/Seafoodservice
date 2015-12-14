var chicago = new google.maps.LatLng(41.850033, -87.6500523);
var mexico = new google.maps.LatLng(19.4270499, -99.1275711);
var london = new google.maps.LatLng(51.5001524, -0.1262362);
var johannesburg = new google.maps.LatLng(-26.201452, 28.045488);
var sydney = new google.maps.LatLng( -33.867139, 151.207114);
	
function initialize() {
  var myLatlng = new google.maps.LatLng(17.412856, 50.283015);
  var mapOptions = {
    zoom: 2,
    center: myLatlng
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  var markerChicago = new google.maps.Marker({
      position: chicago,
      map: map,
      title: 'Chicago'
  });
	markerChicago.info = new google.maps.InfoWindow({
	  content: '<p style="color: red; margin-bottom: -10px;"> Chicago </p><br>текст, текст, текст<br>текст, текст, текст '
	});

	google.maps.event.addListener(markerChicago, 'click', function() {
	  markerChicago.info.open(map, markerChicago);
	});
	
	
	var markerMexico = new google.maps.Marker({
      position: mexico,
      map: map,
      title: 'Mexico'
  });
	markerMexico.info = new google.maps.InfoWindow({
	  content: '<p style="color: red; margin-bottom: -10px;"> Mexico </p><br>текст, текст, текст<br>текст, текст, текст '
	});

	google.maps.event.addListener(markerMexico, 'click', function() {
	  markerMexico.info.open(map, markerMexico);
	});	
	
	
	var markerLondon = new google.maps.Marker({
      position: london,
      map: map,
      title: 'London'
  });
	markerLondon.info = new google.maps.InfoWindow({
	  content: '<p style="color: red; margin-bottom: -10px;"> London </p><br>текст, текст, текст<br>текст, текст, текст '
	});

	google.maps.event.addListener(markerLondon, 'click', function() {
	  markerLondon.info.open(map, markerLondon);
	});
	
	
	var markerJohannesburg = new google.maps.Marker({
      position: johannesburg,
      map: map,
      title: 'Johannesburg'
  });
	markerJohannesburg.info = new google.maps.InfoWindow({
	  content: '<p style="color: red; margin-bottom: -10px;"> Johannesburg </p><br>текст, текст, текст<br>текст, текст, текст '
	});

	google.maps.event.addListener(markerJohannesburg, 'click', function() {
	  markerJohannesburg.info.open(map, markerJohannesburg);
	});
	
	
	var markerSydney = new google.maps.Marker({
      position: sydney,
      map: map,
      title: 'Sydney'
  });
	markerSydney.info = new google.maps.InfoWindow({
	  content: '<p style="color: red; margin-bottom: -10px;"> Sidney </p><br>текст, текст, текст<br>текст, текст, текст '
	});

	google.maps.event.addListener(markerSydney, 'click', function() {
	  markerSydney.info.open(map, markerSydney);
	});
	
	
}

google.maps.event.addDomListener(window, 'load', initialize);
