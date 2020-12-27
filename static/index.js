$("#searchbutton").click(function() {
    console.log("bruh");
    $.ajax({
        type: "POST",
        url: "/swipe",
        data: {"test":"hello world"},
        success: function(){},
        dataType: "json",
        contentType: "application/json"
    });
});