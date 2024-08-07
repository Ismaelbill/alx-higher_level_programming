const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, (d) => {
    $('DIV#hello').text(d.hello);
  });
});
