var gui = (function(){
    window.onhashchange = function(){
        $(".nav-sidebar li").removeClass('active');
        var hash = window.location.hash;
        hash = ( hash == "")? '#' : hash;
        var active = ".nav-sidebar li a[href='"+ hash +"']";
        $(active).parents('li').addClass('active')
    };

    $('.dateinput input').datepicker({
        'format':'yyyy-mm-dd'
    });

})();