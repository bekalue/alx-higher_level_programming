'use strict';
$(() => {
  const API_URL = 'https://fourtonfish.com';

  $.get(`${API_URL}/hellosalut/?lang=fr`, (data, status) => {
    $('DIV#hello').html(data.hello);
  });
});
