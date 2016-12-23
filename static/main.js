/**
 * Created by assig on 6/14/16.
 */

$('.add_item').click(function(){
  var item_id =  $(this).data('item_id');
  cart_ajax('/cart/add_item', item_id, '', '');
});


$('.delete_item').click(function(){
  $(this).parent().parent().hide();
  var item_position = $(this).parent().parent().find('.item_position').text();
  cart_ajax('/cart/delete_item', '', item_position, '');
});

$('.set_count').click(function(){
  $(this).attr('type', 'number').parent().find('.change_item_count').css('display', 'block');
});

$('.change_item_count').click(function(){
  $(this).hide().parent().find('.set_count').attr('type', 'button');
  var item_position =  $(this).parent().parent().find('.item_position').text();
  var count =  $(this).parent().find('.set_count').val();
  console.log(count + ' -count');
  cart_ajax('/cart/change_item_count', '', item_position, count);
});
