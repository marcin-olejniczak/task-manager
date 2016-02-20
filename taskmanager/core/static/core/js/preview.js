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
        var comments_list = $('#comments-list');

        form.find('textarea').wysihtml5();

        // Handle Comment Form
        form.on('click', 'input[type=submit]', function(e){
            e.preventDefault();
            e.stopPropagation();
            var el = $(this);
            var url = form.attr('action');
            var textarea = form.find('#id_text');
            function successH(res){
                //reset added errors
                form.find('fieldset.error').removeClass('error');
                form.find('fieldset .errorlist').remove();
                debugger;
                if(res.data.errors){
                    var errors = res.data.errors;
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
                            .addClass('alert-success text-center')
                            .text('Saved')
                    );
                    form.find('textarea').data('wysihtml5').editor.clear();
                }
            };

            $.ajax(
                url,
                {
                    method: 'POST',
                    data: {
                        text: textarea.val(),
                    }
                }
            ).done(successH).fail(ajaxErrorH);
        });

        // Display comments
        function displayComments(res){
            var comments = res.data.comments
            for(var i in comments){
                var comment_obj = comments[i];
                var avatar = (comment_obj.avatar)? comment_obj.avatar : '/static/core/img/avatar.png';
                comments_list.append(
                    $('<li/>').addClass('media').append(
                        $('<a/>').addClass('avatar pull-left').append(
                            $('<img/>').attr('src', avatar)
                        )
                    ).append(
                        $('<div/>').addClass('media-body').append(
                            $('<div/>').addClass('well well-lg').append(
                                $('<div/>').addClass('media-heading').append(
                                    $('<h5/>').text(comment_obj.author)
                                )
                            ).append(
                                $('<span/>').addClass('media-date').text(
                                    comment_obj.created_date
                                )
                            ).append(
                                $('<p/>').addClass('media-comment').html(
                                    comment_obj.text
                                )
                            )
                        )
                    )
                );
            }
        }
        // Get tasks comments
        function get_comments(){
            var url = '/api/comments/get/' + comments_list.attr('data-task-id');
            $.get(
                url,
                displayComments,
                'json'
            ).fail(ajaxErrorH)
        }

        get_comments();

    })();
})();
