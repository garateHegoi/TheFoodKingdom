/*Karrikas-ek itzulia (karrikas@karrikas.com) */
( function( factory ) {
	"use strict";

	if ( typeof define === "function" && define.amd ) {

		// AMD. Register as an anonymous module.
		define( [" ..widgetsdatepicker "], factory );
	} else {

		// Browser globals
		factory( jQuery.datepicker );
	}
} )( function( datepicker ) {
"use strict";

datepicker.regional.eu = {
	closeText: "Egina",
	prevText: "Aur",
	nextText: "Hur",
	currentText: "Gaur",
	monthNames: [ "01", "02", "03", "04", "05", "06",
		"07", "08", "09", "10", "11", "12" ],
	monthNamesShort: [ "urt.", "ots.", "mar.", "api.", "mai.", "eka.",
		"uzt.", "abu.", "ira.", "urr.", "aza.", "abe." ],
	weekHeader: "As",
	isRTL: false,
	showMonthAfterYear: false,
	yearSuffix:""  };
datepicker.setDefaults( datepicker.regional.eu );

return datepicker.regional.eu;

} );