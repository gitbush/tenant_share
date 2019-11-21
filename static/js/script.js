/*jshint esversion: 6, sub:true */
/*global $, keys  */

// collapsing sidebar
const menuIcon = document.getElementById("menu-icon");
const sidebar = document.getElementById("sidebar");
const content = document.getElementById("content");

if(window.innerWidth >= 960){
    if(sidebar){
        sidebar.classList.add("show-sidebar");
        content.style.marginLeft = "60px";
    }
}

else if(menuIcon && (window.innerWidth < 960)){
    menuIcon.addEventListener("click", function(){
        sidebar.classList.add("show-sidebar");
        event.stopPropagation();
    });
    

    document.addEventListener("click", function(e){
        if(e.target.classList.contains("show-sidebar") === false){
            sidebar.classList.remove("show-sidebar");
        }
    });
}

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
        });
    }
    
// maintenance request detail toggle switch

const toggleSwitch = document.getElementById("request-toggle-switch");
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
                toggleSwitch.classList.remove("toggle-switch"); // reverses toggle and displayed view
                messageView.style.display = "none";
                detailView.style.display = "block ";
            }
    });
}


// maintenance request priority and status colors
const priorityBadge = document.querySelectorAll(".priority-badge");

priorityBadge.forEach(function(badge){
    switch(badge.innerText) {
        case "Low":
            badge.classList.add("badge-success");
          break;
        case "Med":
            badge.classList.add("badge-amber");
          break;
        case "High":
            badge.classList.add("badge-danger");
            break;
        default:
            badge.classList.add("badge-info");
    }
});


// submit status form on change
const statusForm = document.getElementById("status-form");

if(statusForm){
    statusForm.addEventListener("change", function(){
        this.submit();
    });
}

// submit maintenance list sort form on change
const maintSearchForm = document.getElementById("maint-search-form");
const sortField = document.getElementById("id_ordering");

if(maintSearchForm){
    sortField.addEventListener("change", function(){
        maintSearchForm.submit();
    });
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
let authorListItem =    `<li class="row"> 
                            <div class="col-11 col-sm-10"> 
                                <div class="row author-bg"> 
                                    <div class="col-3 col-sm-2 p-0 text-center"> 
                                        <img src="{ image_url }" alt="Prof"class="profile-icon rounded-circle img-fluid"> 
                                        <p class="sm-text m-1 bold"><i>"You"</i></p> 
                                    </div> 
                                    <div class="col-7 p-0 position-relative"> 
                                        <div class="col-12"> 
                                            <p id="message-chat" class="md-text mb-2 mt-2">{ message }</p> 
                                            <p class="msg-id" hidden>{ id }</p>
                                        </div>
                                        <div class="col-12 date-posted">
                                            <hr class="m-1"> 
                                            <p id="message-date" class="sm-text mb-1 mt-1">{ date_posted }</p> 
                                        </div>
                                    </div>
                                </div> 
                            </div> 
                        </li>`;

// reciever right hand side item
let recieverListItem = `<li class="row justify-content-end">
                            <div class="offset-1 col-11 col-sm-10">
                                <div class="row receivers-bg justify-content-end">
                                    <div class="col-7 p-0 text-right position-relative">
                                        <div class="col-12">
                                            <p id="message-chat" class="md-text mt-2 mb-2">{ message }</p> 
                                            <p class="msg-id" hidden>{ id }</p>
                                        </div>
                                        <div class="col-12 text-right date-posted">
                                            <hr class="m-1">
                                            <p id="message-date" class="sm-text mb-1">{ date_posted }</p>
                                        </div>
                                    </div>
                                    <div class="col-3 col-sm-2 p-0 text-center">
                                        <img src="{ image_url }" alt="Prof" class="profile-icon rounded-circle img-fluid">
                                        <p class="sm-text m-1 bold"><i>"{ author }"</i></p>                           
                                    </div>
                                </div
                            </div>
                        </li>`;

// global chat variables 
const msgForm = $('#chat-msg-form');
const maintId = $('#maint-title').text();
const msgList = $('#message-list');
let msgInput = $('#id_message');


// capture message form and send post to chat api             
msgForm.on('submit', function(e){
    e.preventDefault();
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
            
            if(lastMsgId){
                $.get(`/api/chat/chat-message/?q=${maintId}&id=${lastMsgId}`, function(data){
    
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
                            }
                        }
                }
            );
            }
            
        }, 2000
    );
}

    
// add and remove tenant modals

function confirmModal(title, message, href){

    const modalTitle = document.getElementById('title');
    const modalMessage = document.getElementById('message');
    const modalConfirm = document.getElementById('delete-confirm');

    modalTitle.innerText = title;
    modalMessage.innerText = message;
    modalConfirm.setAttribute('href', href);
    
    document.getElementById('confirm-modal').style.display = 'block';

}

let modalClose = document.getElementsByClassName('modal-close');

if(modalClose.length > 0){

    for(let i=0; i < modalClose.length; i++){
        modalClose[i].addEventListener('click', function(){

        modalClose[i].closest('.modal').style.display = 'none';
    });
    }
}


window.addEventListener('click', function(e){
    if(e.target.className === 'overlay'){
        e.target.closest('.modal').style.display = 'none';
    }
});

// add tenant functionality

const addTenantBtn = document.getElementById('add-tenant-btn');

function addTenantModal(){
    document.getElementById('add-tenant-modal').style.display = 'block';

}

if(addTenantBtn){
    addTenantBtn.addEventListener('click', function(){
        addTenantModal();
    });
}


// add tenant form


const searchTenForm = $('#txt-search');
const addTenForm = $('#add-tenant-form'); 
const addTenantList = $('#add-user-list');

// check if suggestion list is empty and display message
function emptyUserList(list, e, form){
    if(list.is(':empty')){
        list.append('<p class="md-text text-left m-2">No results found</p>');
    } 
    else if((e.keyCode == 8 && !form)){
        list.empty();
        list.append('<p class="md-text text-left m-2">No results found</p>');
    }
}

// template for add tenant suggestion 
let tenantSuggestion =  `<li class="row m-1 tenant-suggestion">
                            <div class="col-3 col-sm-4 col-md-3">
                                <img src="{ img_url }" alt="" class="add-tenant-icon rounded-circle">
                            </div>
                            <div class="col-7 text-left pl-1">
                                <p id="ten-name" class="md-text m-1">{ name }</p>
                            </div>
                        </li>`;

// emptyUserList(addTenantList);

// handling of add tenant form suggestions
searchTenForm.on('keyup', function(e){

    let formVal = searchTenForm.val();

    addTenantList.empty();

    keys = [32, 37, 38, 39, 40];
    if(keys.includes(e.keyCode) == false){
        $.ajax({
            type:'GET',
            url: `/api/users/user-list/?q=${formVal}`,
            success: function(data){
                data.forEach(function(d){
    
                    // replace relevant placeholders with incoming values
                    let suggestion = tenantSuggestion.replace('{ img_url }', d.profile['profile_image']);
                    suggestion = suggestion.replace('{ name }', d.username);
                    addTenantList.append(suggestion);
    
                    emptyUserList(addTenantList, e, formVal);
    
                });
                emptyUserList(addTenantList, e, formVal);
    
                // add tenant form processing 
                let suggestionEl = $('.tenant-suggestion');
    
                suggestionEl.on('click', function(e){
                    let clickUsername = $(this).find('#ten-name').text();
                    searchTenForm.val(clickUsername);
                    addTenForm.submit();
                });
            }
        });
    } else {
        e.preventDefault();
    }
});    

// alert modal for user messages
const alertDiv = document.getElementById('edit-profile-alert');

if(alertDiv){
    document.addEventListener('DOMContentLoaded', function(e){
        setTimeout(function(){
            if(alertDiv.innerText != false){
                alertDiv.classList.toggle('show-alert');
                setTimeout(function(){
                    alertDiv.classList.toggle('show-alert');
                }, 5000);
            } 
        }, 1000);
    });
}

// handle message tags error/success
let msgTag = document.getElementById('msg-tag');
const msgHeading = document.getElementsByClassName('alert-header')[0];

if(msgTag){
    msgType();
}

function msgType(){
    if(msgTag.classList.contains('error')){
        msgHeading.innerText = 'WOOPS!';
        msgHeading.style.color = 'red';
    }
}

// delete payment from list
const deletePaymentBtn= document.getElementById('delete-payment-btn');

if(deletePaymentBtn){
    deletePaymentBtn.addEventListener('click', function(e){

        const payId = this.getAttribute('data-payId');
        const href = `/payments/delete/${payId}`;
        const message = 'Are you sure you want to delete this payment?';
        const title = 'Delete payment';

        confirmModal(title, message, href);
    
    });
}

// delete maintenance request
const deleteRequestBtn= document.querySelectorAll('#delete-request-btn');

if(deleteRequestBtn){
    deleteRequestBtn.forEach(function(btn){
        btn.addEventListener('click', function(e){
            const maintId = this.getAttribute('data-maint-id');
            const href = `/maintenance/delete/${maintId}`;
            const message = 'Are you sure you want to delete this maintenance request?';
            const title = 'Delete maintenance request';
    
            confirmModal(title, message, href);
        
        });
    });
}

// remove tenant from rental property
const deleteTenantBtn = document.querySelectorAll('#delete-tenant-btn');

if(deleteTenantBtn){
    deleteTenantBtn.forEach(function(btn){
        btn.addEventListener('click', function(e){

            const firstName = this.parentNode.parentNode.querySelector('#ten-first').innerText;
            const lastName = this.parentNode.parentNode.querySelector('#ten-last').innerText;

            const tenId = this.getAttribute('data-ten-Id');
            const rentId = this.getAttribute('data-rent-Id');

            const href = `/tenant/remove/${rentId}/${tenId}`;
            const message = `Are you sure you want to remove ${firstName} ${lastName} from this property?`;
            const title = 'Remove tenant';

            confirmModal(title, message, href);
        
        });
    });
}

// loading spinner
function showLoader(){
    const spinner = document.querySelector('.spinner');
    spinner.style.visibility = 'visible';
}

function hideLoader(){
    const spinner = document.querySelector('.spinner');
    spinner.style.visibility = 'hidden';
}

window.addEventListener('DOMContentLoaded', function(){
    showLoader();
});

window.addEventListener('load', function(){
    setTimeout(hideLoader, 500);
});

