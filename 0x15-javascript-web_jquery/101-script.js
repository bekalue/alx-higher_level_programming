'use strict';
$(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    const last = $('UL.my_list').children().last();
    if (last) {
      last.remove();
    }
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
