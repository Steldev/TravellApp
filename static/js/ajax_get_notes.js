$(document).ready(function () {
    // Посилання з id="test" буде тригером події
    $("#load_href_1").click(function () {

        var qr = $(".user-posts >:last-child .note_date").text();

        $.ajax({
            type: 'GET',
            async: true,
            url: 'load_notes/',
            data: "since=" + qr,
            success: function (data) {
                $(".user-posts").append(data['html'])
            },
            dataType: 'json',
        });

    });
});