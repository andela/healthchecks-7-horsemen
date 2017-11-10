$(function () {

    $(".member-remove").click(function () {
        var $this = $(this);

        $("#rtm-email").text($this.data("email"));
        $("#remove-team-member-email").val($this.data("email"));
        $('#remove-team-member-modal').modal("show");

        return false;
    });


    $('.radio').hide();
    
    $('input[type=checkbox]').click( function () {
        if ($('input[type=checkbox]').is(':checked')){
            $('input[type=radio]').prop('disabled', false);
            $('.radio').show();
        }
        else{
            $('input[type=radio]').prop('disabled', true);
            $('.radio').hide();
        }
    });


});
