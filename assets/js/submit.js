$(function() {
    // When the testform is submitted…
    $("form").submit(function(event) {
        // post the form values via AJAX…
        var address = event.target.children[0].value;
        var postdata = {address: address}

        $.post('http://gobaan.com/ava/email', postdata, function(data) {
            // and set the title with the result
           });

        $("form").html("<h2>Thanks " + address + "! I'll contact you soon!");
        return false ;
    });
});
