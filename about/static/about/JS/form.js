 $(document).ready( function() {
    var maxLen = 100;

    $('#subject').keypress(function(event){
        var Length = $("#subject").val().length;
        var AmountLeft = maxLen - Length;
        $('#txt-length-left').html(AmountLeft);
        if(Length >= maxLen){
            if (event.which != 8) {
                    $('#errMsg').text('Maximum 100 characters allowed!');
                return false;
            }
        }
    });

 });
