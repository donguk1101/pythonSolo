$(function(){
    $('.side_menu > li').hover(function(){
        $('.side_detail_menu').hide()
        $(this).children('.side_detail_menu').show()
    })
})