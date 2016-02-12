/**
 * GUI enhancements in preview view
 */
var preview = (function(){
    $('body').on('click', '#track_btn', function(e){
        e.preventDefault();
        var el = $(this);
        var url = el.attr('href');
        function successH(res){
            el.removeClass('loading');
            var icon = el.find('span');
            if(el.find('.glyphicon-eye-open').length > 0){
                icon.removeClass('glyphicon-eye-open');
                icon.addClass('glyphicon-eye-close');
            }else{
                icon.removeClass('glyphicon-eye-close');
                icon.addClass('glyphicon-eye-open');
            }
        };
        function errorH(err){
            alert('An error occurred');
            console.log(err);
        };

        el.addClass('loading');
        $.ajax(
            url,
            {
                success: successH,
                fail: errorH,
            }
        );
    });
})();