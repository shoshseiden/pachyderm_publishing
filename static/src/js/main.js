window.jQuery = window.$ = require("jquery");

require("bootstrap");

require("../less/site.less");
require("../images/pachyderm_banner.jpg");

// jQuery script for cover enlargement
$(document).ready(function(){
  $('#librarycontent img').hover(function() {
    $(this).width("150px").height("200px");
    $(this).css("border-color", "teal");
    $(this).css("border-style", "solid");
    $(this).css("border-width", "5px");
  },
  function(){
    $(this).width("100px").height("150px");
    $(this).css("border-color", "none");
    $(this).css("border-style", "none");
    $(this).css("border-width", "0px");
  });
});
