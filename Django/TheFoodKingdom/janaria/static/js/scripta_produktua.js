$(document).ready(function () {
  $("#guzt").val(
    parseFloat($("#prezioa").val()) * parseInt($("#kopurua").val())
  );

  $("#kendu").click(function () {
    // Kopurua
    kopt = parseInt($("#kopurua").val());
    if (kopt != 1) {
      //Prezio totala
      prezi = parseFloat($("#guzt").val());

      kopl = kopt - 1;
      $("#kopurua").val(kopl);
      kalkulo = (prezi - prezi / kopt).toFixed(2);
      $("#guzt").val(kalkulo);
    }
  });

  $("#gehitu").click(function () {
    //Kopurua
    kopz = parseInt($("#kopurua").val());

    //Prezio totala
    prezio = parseFloat($("#guzt").val());

    kopb = kopz + 1;
    $("#kopurua").val(kopb);
    kalkul = (prezio / kopz + prezio).toFixed(2);
    $("#guzt").val(kalkul);
  });
});
