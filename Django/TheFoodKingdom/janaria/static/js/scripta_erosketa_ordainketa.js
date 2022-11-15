$(document).ready(function(){
    $("#paypal").change(function(){
        window.open("https://www.paypal.com/signin")
        window.location='erosketarenLaburpena'
    })

    $(function() {
        $('.date-picker').datepicker( {
        changeMonth: true,
        changeYear: true,
        showButtonPanel: true,
        dateFormat: 'MM/yy',
        yearRange: '2022:2042',
        minDate: 'dateToday',
        onClose: function(dateText, inst) {
            $(this).datepicker('setDate', new Date(inst.selectedYear, inst.selectedMonth, 1));
        }
        });
    });
});