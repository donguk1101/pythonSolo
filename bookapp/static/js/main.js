$(function(){
    $('.side_menu > li').mouseover(function(){
        $('.side_detail_menu').hide()
        let no=$(this).attr('no');
        let top=16+1.7*(no-1);
        $(this).children('.side_detail_menu').css('top',top+'em');
        $(this).children('.side_detail_menu').show()
    })
    $('.side_menu > li').mouseout(function(){
        $('.side_detail_menu').hide()
    })
})
$(document).on('click','.side_detail_menu > ul > li',function(){
    let tb=$(this).text()
    booklist_loc(tb)
})
function booklist_loc(tb){
    location.href="../shop?tb="+tb
}