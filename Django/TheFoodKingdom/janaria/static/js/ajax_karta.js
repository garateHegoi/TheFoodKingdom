$(document).ready(function () {
  $("a#sailkatu").on("click", function () {
    let submota =this.value;
    $(
      $.ajax({
        type: 'GET',
        url: "{% url 'karta_sailkatua' submota='submota' %}",
        success: function (response) {
            for(let i=0; i<response.length;i++){
                $('#janariak').append($('<div id="janaria" class="text-center">'));
                janari_id=response[i].id;
                $('#janaria').append($(`<a id="link" href="{% url 'produktua' id=janari_id %}">`));
                $('#link').append($(`<img src="{% static 'img/enchilada.jpg'%}">`));
                $('#link').append($(`<p id="janari_izena">`).html(response[i].izena));
            }
        },
        error: function (response) {
            alert("Errore bat egon da kargatzerakoan")
        },
      })
    );
  });
});
