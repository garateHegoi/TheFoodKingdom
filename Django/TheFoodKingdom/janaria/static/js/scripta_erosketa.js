$(document).ready(function(){
    $(".needs-validation").addClass("was-validated");
    
    $(".needs-validation").on("submit", function (e) {
        e.preventDefault();
        if (!this.checkValidity()) {
        e.stopPropagation();
        } 
        else {
            window.location='gehitu_bezero_datuak'
        }
    });
});
