
(function ($) {
    "use strict";
    var mainApp = {
     main_fun: function () {     
		//scrollReveal scripts
            window.scrollReveal = new scrollReveal();  
        },

    }
    // Initializing ///

    $(document).ready(function () {
        mainApp.main_fun();
    });

}(jQuery));
