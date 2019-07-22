// collapsing sidebar
const menuIcon = document.getElementById("menu-icon");
const sidebar = document.getElementById("sidebar");
const content = document.getElementById("content");

if(window.innerWidth >= 960){
    sidebar.classList.add("show-sidebar");
    content.style.marginLeft = "60px";
}

else if(window.innerWidth < 960){
    menuIcon.addEventListener("click", function(){
        sidebar.classList.add("show-sidebar");
        event.stopPropagation();
    });

    document.addEventListener("click", function(e){
        if(e.target.classList.contains("show-sidebar") === false){
            sidebar.classList.remove("show-sidebar");
        }
    });
};

window.addEventListener("resize", function(){
    if(window.innerWidth >= 960){
        sidebar.classList.add("show-sidebar");
        content.style.marginLeft = "60px";
    }
});

// edit account button
const editBtn = document.getElementById("edit-btn");
    if(editBtn){
        editBtn.addEventListener("click", function(){
            if(editBtn.innerText == "Edit"){
                editBtn.innerText = "Close";
            }
            else{
                editBtn.innerText = "Edit";
            }
        })
    }
    
// maintenance request detail toggle switch

const toggleSwitch = document.getElementById("request-toggle-switch");
const detailTab = document.getElementById("detail-tab");
const messagesTab = document.getElementById("messages-tab");
const toggleSelect = document.getElementsByClassName("request-toggle-item");

const messageView = document.getElementById("message-view");
const detailView = document.getElementById("detail-view");


for (let i = 0; i < toggleSelect.length; i++){
        toggleSelect[i].addEventListener("click", function(event){
            
            if(event.target.id == "messages-tab"){
                toggleSwitch.classList.add("toggle-switch"); // moves toggle swith to message tab
                messageView.style.display = "block"; // displays maintenance request message view
                detailView.style.display = "none"; // hides maintenance request detail view
            }
            else if(event.target.id == "detail-tab"){
                toggleSwitch.classList.remove("toggle-switch") // reverses toggle and displayed view
                messageView.style.display = "none";
                detailView.style.display = "block ";
            }
    })
}


// maintenance request priority and status colors

const priorityBadge = document.getElementById("priority-badge");
const statusBadge = document.getElementById("status-badge");

if(priorityBadge && statusBadge){
    if(priorityBadge.innerText == "low"){
        priorityBadge.classList.add("badge-success");
    }
    else if(priorityBadge.innerText == "med"){
        priorityBadge.classList.add("badge-amber");
    }
    else if(priorityBadge.innerText == "high"){
        priorityBadge.classList.add("badge-danger");
    }

    if(statusBadge.innerText == "new"){
        statusBadge.classList.add("badge-info");
    }
    else if(statusBadge.innerText == "In Progress"){
        statusBadge.classList.add("badge-info");
    }
    else if(statusBadge.innerText == "Awaiting Payment"){
        statusBadge.classList.add("badge-amber");
    }
    else if(statusBadge.innerText == "Resolved"){
        statusBadge.classList.add("badge-success");
    }

}


// submit status form on change
const statusForm = document.getElementById("status-form")

if(statusForm){
    statusForm.addEventListener("change", function(){
        this.submit()
    })
}

// submit maintenance list sort form on change
const maintSearchForm = document.getElementById("maint-search-form");
const sortField = document.getElementById("id_ordering");


if(maintSearchForm){
    sortField.addEventListener("change", function(){
        maintSearchForm.submit()
    })
}

// chat message functionality
const msgForm = $('#chat-msg-form');
const maintId = $('#maint-title').text();
const msgView = $('#message-view');
const msgList = $('#message-list');
let msgInput = $('#id_message');

// csrf protection. Copied from django documentation
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// create message list item template
let listItem = '<li class="row">' +
                    '<div class="col-3 col-sm-2 p-0 text-center">' +
                        '<img src="{ image_url }" alt="Prof"class="profile-icon rounded-circle img-fluid">' +
                    '</div>' +
                    '<div class="col-7 p-0">' +
                        '<div class="col-12">' +
                            '<p id="message-chat" class="md-text">{ message }</p>' +
                        '</div>'
                        '<div class="col-12">'
                            '<p id="message-date" class="md-text">{ message.date_posted }</p>' +
                        '</div>'+
                    '</div>'+
                '</li>';

// capture message form and send post to chat api             
msgForm.on('submit', function(e){
    e.preventDefault()
    let msg = msgInput.val();
    // insert csrf token before sending request
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.ajax({
        type: 'POST',
        url: '/chat/api/chat-message/',
        data: {"maint_request": maintId,
                "author": 8,
                "message": msg,
                "date_posted": ''},
        success: function(data){
            msgInput.val('');
            var msgItem = listItem.replace('{ message }', data['message'])
            msgList.append(msgItem)
        }
    })
})



