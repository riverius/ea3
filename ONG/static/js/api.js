
$.ajax({
  type: "GET",
  url: "https://timezone.abstractapi.com/v1/current_time/?api_key=43af46b8c76d48d6b849a68cce71d91f&location=Santiago, Chile",
  dataType: "json",
  success: function (response) {
      $('#horario').append(response.requested_location," <br> Fecha : "+response.datetime);
    //console.log(response)
  
  }
});