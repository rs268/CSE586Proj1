var map;
function initMap() {
    map = new google.maps.Map($("#map")[0], {
      center: {lat: 42.880230, lng: -78.878738},
      zoom: 8
    });
}

function requestDirections() {
    fromAddress = $("#fromAddress").val();
    toAddress = $("#toAddress").val();

    var csrftoken = Cookies.get("csrftoken");

    $.ajaxSetup({
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })

    $.ajax({
        type: "POST",
        url: "",
        data: {
            "from_address": fromAddress,
            "to_address": toAddress
        },
        success: function(result) {
            alert("SUCCESS");
        }
    });
}