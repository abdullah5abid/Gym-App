function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Use csrf token while doing post request, this will prevent 500 Server Error
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
}); 

//All sessions API
$.ajax({
    url : "http://localhost:8000/api/sessions/",
    dataType: "json",
    success : function (response) {
        let trHTML = '';
        $.each(response, function (i, session) {
           trHTML += "<tr><th>" + session.name + "</th><td>" + session.duration + "</td><td>" + session.exercise1 + "</td><td>" + session.exercise2 + "</td><td>" + session.exercise3 + "</td><td> <button class='btn btn-success update btn-sm' id ="+ session.id +" data-toggle='modal' data-target='#editSession'>Update</button> <button class='btn btn-danger btn-sm delete' id ="+ session.id +" data-toggle='modal' data-target='#deleteSession'>Delete</button>"
           "</td></tr>";
        });
        $('#session-Records').append(trHTML);
    }
});

$('#create').click(function(){ 
    $("#add-session").trigger('reset');
});

//Save New session Button
$(function() { 
        $('#addSession').on('submit', function(e) { 
            e.preventDefault();  

            let myurl = "http://localhost:8000/api/sessions/add/";

        $.ajax({
            type : 'POST',
            url : myurl,
            data : $("#addSession :input").serializeArray(),
            dataType: "json",
            success: function(data){
                alert("Session Added!");
                location.reload();
            },
            error:function(data){
                alert("Session Not Added!");
                location.reload();
            }
        });
    });
});

//Edit sessions API
$('#session-Records').on('click', '.update', function(e){
    e.preventDefault();
    
    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);

    let myurl = "http://localhost:8000/api/sessions/"+id+"/";

    $( "#p-name" ).change(function() {
        $('input[name=name]').val($(this).val());
    });
    $( "#p-duration" ).change(function() {
        $('select[name=duration]').val($(this).val());
    });
    $( "#p-exercise1" ).change(function() {
        $('input[name=exercise1]').val($(this).val());
    });
    $( "#p-exercise2" ).change(function() {
        $('input[name=exercise2]').val($(this).val());
    });
    $( "#p-exercise3" ).change(function() {
        $('input[name=exercise3]').val($(this).val());
    });

    $.ajax({
        async: true,
        url:myurl,
        method:'GET',
        success: function(result){
            $('input[name="name"]').val(result.name);
            $('select[name="duration"]').val(result.duration);
            $('input[name="exercise1"]').val(result.exercise1);
            $('input[name="exercise2"]').val(result.exercise2);
            $('input[name="exercise3"]').val(result.exercise3);
        }
    });

});

//Save Edited session Button
$(function() { 
        $('#editSession').on('submit', function(e) { 
            e.preventDefault();  

            let id = $("#Myid").attr("value");
            console.log(id);

            let myurl = "http://localhost:8000/api/sessions/edit/"+id+"/";

        $.ajax({
            type : 'PUT',
            url : myurl,
            data : $("#editSession :input").serializeArray(),
            dataType: "json",
            success: function(data){
                alert("Session Updated!");
                location.reload();
            },
            error:function(data){
                alert("Session Not Updated!");
                location.reload();
            }
        });
    });
});

//Delete sessions API
$('#session-Records').on('click', ".delete", function(e){
    e.preventDefault();
    
    let id = $(this).attr('id');
    $('input[id=Myid]').val(id);
    console.log(id)

    let myurl = "http://localhost:8000/api/sessions/"+id+"/";

    $.ajax({
        async: true,
        url:myurl,
        method:'GET',
        success: function(result){
            $('input[name="id"]').val(result.id);
        }
    });

});

//Save Delete sessions Button
$(function() { 
        $('#deleteSession').on('submit', function(e) { 
            e.preventDefault(); 

            let id = $("#Myid").attr("value");
            console.log(id);

        let myurl = "http://localhost:8000/api/sessions/delete/"+id+"/";

        $.ajax({
            async: true,
            url:myurl,
            method:'DELETE',
            success: function(result){
                location.reload();
            },
            error:function(result){
                alert("session Not Deleted!");
                location.reload();
            }
        });

    });
});   