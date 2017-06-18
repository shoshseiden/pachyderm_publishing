window.jQuery = window.$ = require("jquery");

require("bootstrap");

require("../less/site.less");
require("../images/pachyderm_banner.jpg");

// jQuery script for cover enlargement
$(document).ready(function(){
  $('#library_content img').hover(function() {
    $(this).width("150px").height("200px");
    $(this).css("border-color", "teal");
    $(this).css("border-style", "solid");
    $(this).css("border-width", "5px");
  },
  function(){
    $(this).width("100px").height("150px");
    $(this).css("border-color", "black");
    $(this).css("border-style", "solid");
    $(this).css("border-width", "2px");
  });
});

// jQuery script for book cover photo border
$(document).ready(function(){
  $('#book_content img').css("border-style", "solid");
  $('#book_content img').css("border-color", "black");
  $('#book_content img').css("border-width", "5px");
});
