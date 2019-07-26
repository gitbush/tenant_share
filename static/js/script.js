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

//========== chat message functionality

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
// author left hand side item
let authorListItem = '<li class="row">' +
                    '<div class="col-11 col-sm-10">' +
                        '<div class="row author-bg">' +
                            '<div class="col-3 col-sm-2 p-0 text-center">' +
                                '<img src="{ image_url }" alt="Prof"class="profile-icon rounded-circle img-fluid">' +
                                '<p class="sm-text m-1 bold"><i>"You"</i></p>' +
                            '</div>' +
                            '<div class="col-7 p-0 position-relative">' +
                                '<div class="col-12">' +
                                    '<p id="message-chat" class="md-text mb-2 mt-2">{ message }</p>' +
                                    '<p class="msg-id" hidden>{ id }</p>'+
                                '</div>'+
                                '<div class="col-12 date-posted">'+
                                    '<hr class="m-1">' +
                                    '<p id="message-date" class="sm-text mb-1 mt-1">{ date_posted }</p>' +
                                '</div>'+
                            '</div>'+
                        '</div>' +
                    '</div>' +
                '</li>';

// reciever right hand side item
let recieverListItem = '<li class="row justify-content-end">'+
                            '<div class="offset-1 col-11 col-sm-10">'+
                                '<div class="row receivers-bg justify-content-end">'+
                                    '<div class="col-7 p-0 text-right position-relative">'+
                                        '<div class="col-12">'+
                                            '<p id="message-chat" class="md-text mt-2 mb-2">{ message }</p>'+ 
                                            '<p class="msg-id" hidden>{ id }</p>'+
                                        '</div>'+
                                        '<div class="col-12 text-right date-posted">'+
                                            '<hr class="m-1">'+
                                            '<p id="message-date" class="sm-text mb-1">{ date_posted }</p>'+
                                        '</div>'+
                                    '</div>'+
                                    '<div class="col-3 col-sm-2 p-0 text-center">'+
                                        '<img src="{ image_url }" alt="Prof" class="profile-icon rounded-circle img-fluid">'+
                                        '<p class="sm-text m-1 bold"><i>"{ author }"</i></p>'+                           
                                    '</div>'+
                                '</div'+
                            '</div>'+
                        '</li>'

// global chat variables 
const msgForm = $('#chat-msg-form');
const maintId = $('#maint-title').text();
const msgView = $('#message-view');
const msgList = $('#message-list');
let msgInput = $('#id_message');


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
        url: '/api/chat/chat-message/',
        data: {"maint_request": maintId,
                "message": msg,
                "date_posted": ''},
        success: function(data){
            msgInput.val('');
            let date = new Date(data['date_posted']);
            let datePosted = date.toLocaleString('en-GB', { timeZone: 'UTC', hour12: true });

            let msgItem = authorListItem.replace('{ message }', data['message']);
            msgItem = msgItem.replace('{ date_posted }', datePosted);
            msgItem = msgItem.replace('{ image_url }', data.author.profile['profile_image']);
            msgItem = msgItem.replace('{ id }', data['id']);
            msgList.append(msgItem);
        },
        error: function(error){
            console.log(error);
        }
    });
});

// get all chat messages is current page is maint detail every 2 seconds
if(maintId){
    
    setInterval(

        function getMessages(){
        
            const maintId = $('#maint-title').text();
            let lastMsgId = $('.msg-id').last().text();
    
            $.get('/api/chat/chat-message/?q='+maintId+'&id='+lastMsgId+'', function(data){
    
                    if (data.length !== 0)
                        {
                            for(let i=0;i<data.length;i++) {
                                console.log(lastMsgId);
                                let msgItem = recieverListItem.replace('{ message }', data[i].message);
                                msgItem = msgItem.replace('{ date_posted }', data[i].date_posted);
                                msgItem = msgItem.replace('{ author }', data[i].author['first_name']);
                                msgItem = msgItem.replace('{ image_url }', data[i].author.profile['profile_image']);
                                msgItem = msgItem.replace('{ id }', data[i].id);
                                msgList.append(msgItem);
                            };
                        };
                }
            )
            
        }, 2000
    )
};




