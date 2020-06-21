setInterval(function () {
    $('head title', window.parent.document).text("csTimer - Professional Rubik's Cube Speedsolving/Training Timer " +
        $("#scrambleDiv > div.title > nobr:nth-child(1) > select:nth-child(2) > option:selected").text() + " " +
        $("[data=cs]").text() + " " +
        $("[data=cm0]").text() + " " +
        $("[data=ca1]").text() + " " +
        $("[data=ca2]").text() + " " +
        $("[data=ca3]").text()
    );
}, 5000);