function custom_style_summernote()
{

		//STYLE SUMMERNOTE: Static files from summernote plugin are not loading properly (bug from summernote)

		//Summernote Widget
        $('.note-editable').css('background','rgba(0,0,0,0.3)');

        $('.dropdown-item p').addClass('summernote-style-text');
        $('.dropdown-item h3').addClass('summernote-style-text');
        $('.dropdown-item h2').addClass('summernote-style-text');
        $('.dropdown-item h1').addClass('summernote-style-text');
        $('.dropdown-item h4').addClass('summernote-style-text');
        $('.dropdown-item h5').addClass('summernote-style-text');
        $('.dropdown-item h6').addClass('summernote-style-text');
        $('.dropdown-item pre').addClass('summernote-style-text');
        //## Summernote Widget

        //Modals
        $('.note-image-input .form-control-file .note-form-control .note-input').addClass('summernote-style-text');
        $('.note-form-label').css('color','#fff');

        $('.note-form-label small').css('color','#fff');

        $('.modal-header').css('background','#3a3a3a');
        $('.modal-header button').css('color','#fff');
        $('.modal-title').css('padding','5px');
        $('.modal-title').css('color','#fff');

        $('.modal-body').css('background','#626263');
        $('.modal-footer').css('background','#626263');
        $('.modal-footer input').css('background','#1b1b47');
        $('.modal-footer input').css('color','#fff');

        $('.text-muted').css('color','#fff');
        //## Modals

        //Style button
        $('.dropdown-menu').css('background','#eee');

}