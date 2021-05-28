/*$(document).on('mouseover','li[class^=col_]',function(){
    name=$(this).attr('class');
    change(name);

})*/
$(function(){
    $('li[class^=col_]').hover(function(){
        name=$(this).attr('class');
        change(name);
    })
})
function change(name){
    img=[
        "/img/new_book.png","/img/weekly_book.png",
        "/img/yes_cup.jpg","/img/wel_food.jpg"
    ]
    img_name=img[name[name.length-1]-1];
   $('.main_img').attr('src','/static'+img_name);
}
