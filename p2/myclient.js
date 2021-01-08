window.onload = function () {
    var url,
      i,
      ports = [28, 29];  // the GPIO ports we will read
  
    for (i in ports) {
      $('#input_' + ports[i]).html('loading GPIO ' + ports[i] + ' value...');
    }
  
    setInterval( function () {
      for (i in ports) {
        url = document.URL + 'inputs/' + ports[i];
        console.log('making API call ' + url);
  
        $.getJSON(url, function (data) {
          console.log('API response received. port ' + data.gpio + ' value = ' + data.value);
          $('#input_' + data.gpio).html('GPIO input port ' + data.gpio + ' value is ' + data.value);
        });
      } // for 
    }, 3000); // setInterval
    
  }; //onload
  
  