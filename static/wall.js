$("#username2").keyup(function(){
    let data = {username2: $(this)[0].value}
    $.ajax({
        url: "/usersearch",
        method: "POST",
        data: data
    })
    .done(function(response){
        $("#friendsmsg").html(response);
    })
})

$("#username").keyup(function(){
    let data = {username: $(this)[0].value}
    $.ajax({
        url: "/username",
        method: "POST",
        data: data
    })
    .done(function(response){
        $("#usernamemsg").html(response);
    })
})