$(function () {

    $(".member-remove").click(function () {
        var $this = $(this);

        $("#rtm-email").text($this.data("email"));
        $("#remove-team-member-email").val($this.data("email"));
        $('#remove-team-member-modal').modal("show");

        return false;
    });


    $('input[type=radio]').prop('disabled', 'disabled');

    $('input[type=checkbox]').change( function () {
        if ($(this).is(':checked')){
            $('input[type=radio]').prop('disabled', false);
        }
        else{
            $('input[type=radio]').prop('disabled', 'disabled');
        }
    });


});
