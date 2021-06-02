/*$(document).on('mouseover','li[class^=col_]',function(){
    name=$(this).attr('class');
    change(name);

})*/
$(document).ready(function(){
    let name=window.location.pathname
    arr={}
    arr=name.split("/")
    if(arr[2] !="home" ){

    }
})
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

