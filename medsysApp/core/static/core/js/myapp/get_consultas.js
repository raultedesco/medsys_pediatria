$(document).ready(function get_consultas() {

    $.ajax({
        type: "GET",
        url: "/pacientes/get_consultas/2/",
        dataType: "json",
        success: function (json) {
            var consult = json.consults;
            console.log(consult);
            // $("#"+dni).append(count_text);

        }

    });

});