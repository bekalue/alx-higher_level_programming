'use strict';
$(() => {
  const translateHello = () => {
    const API_URL = 'https://fourtonfish.com';
    const code = $('INPUT#language_code').val();

    // For language codes
    // see https://www.loc.gov/standards/iso639-2/php/code_list.php
    $.get(`${API_URL}/hellosalut/?lang=${code}`, (data, status) => {
      $('DIV#hello').html(data.hello);
    });
  };

  $('INPUT#btn_translate').click(translateHello);
  $('INPUT#language_code').keydown((ev) => {
    if (ev.key === 'Enter') translateHello();
  });
});
