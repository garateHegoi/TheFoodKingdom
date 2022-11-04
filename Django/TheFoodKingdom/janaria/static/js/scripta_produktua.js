$(document).ready(function(){
    $("#kendu").click(function(){
      // Kopurua 
      kopt = parseInt($("#kopurua").val())
      if (kopt != 1) {
        //Prezio totala 
        prezi = parseFloat($("#prez").val())
  
        kopl = kopt - 1
        $("#kopurua").val(kopl);
        kalkulo = (prezi - (prezi/kopt)).toFixed(2);
        $("#prez").val(kalkulo);
      }
    })
  
    $("#gehitu").click(function(){
       //Kopurua 
       kopz = parseInt($("#kopurua").val())
  
      //Prezio totala 
      prezio = parseFloat($("#prez").val())
  
      kopb = kopz + 1;
      $("#kopurua").val(kopb);
      kalkul = ((prezio/kopz) + prezio).toFixed(2)
      $("#prez").val(kalkul);
        })
    });