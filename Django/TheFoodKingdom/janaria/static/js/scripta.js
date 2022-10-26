/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
$(document).ready(function(){
  $("#user_login").on("click", function(){
    $("#myDropdown").slideToggle();
  });

  /**$(document).on('click', function(event) {
    if (!$(event.target).closest('#myDropdown').length) {
      // Hide the menus.
      $("#myDropdown").hide();
    }
  });**/
})




