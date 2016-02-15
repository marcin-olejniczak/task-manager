/**
 * GUI enhancements in preview view
 */

var gui = (function(){
    /**
     * Handle Ajax error in most cases
     * @param err
     */
    function ajaxErrorH(err){
        alert('An error occurred');
        console.log(err);
    };
    /**
     * Preview of Task or Project
     */
    var preview = (function(){
        // Toggle tracking Task
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

            el.addClass('loading');
            $.ajax(url, {})
                .done(successH)
                .fail(ajaxErrorH);
        });
    })();
    /**
     * Comments list enhancements
     */
    var comments = (function(){
        // initialize WYSIWYG editor
        var comment_form_container = $('#add-comment');
        var form = comment_form_container.find('form');
        form.find('textarea').wysihtml5();

        // Handle Comment Form
        form.on('click', 'input[type=submit]', function(e){
            e.preventDefault();
            e.stopPropagation();
            var el = $(this);
            var url = form.attr('action');
            var comment_text = form.find('#id_text').val();
            function successH(res){
                //reset added errors
                form.find('fieldset.error').removeClass('error');
                form.find('fieldset .errorlist').remove();
                var errors = res.result.errors;
                if(errors){
                    for (var field in errors){
                        var errorlist = $('<ul/>').addClass('errorlist');
                        for (var i in errors[field]){
                            var error_text = errors[field][i];
                            var fieldset = $('#id_' + field).parents('fieldset');
                            errorlist.append(
                                $('<li/>').text(error_text)
                            );
                        }
                        fieldset.addClass('error').append(errorlist);
                    }
                }else{
                    comment_form_container.find('.panel-body').append(
                        $('<p/>')
                            .addClass('alert-success')
                            .text('Saved')
                    );
                }
            };

            $.ajax(
                url,
                {
                    method: 'POST',
                    data: {
                        text: comment_text,
                    }
                }
            ).done(successH).fail(ajaxErrorH);
        });

    })();
})();
