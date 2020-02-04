/*jshint esversion: 6, sub:true */
/*global $, keys  */

/**
 * Collapsable sidebar
 */
console.log('ehjj')
var menuIcon = document.getElementById("menu-icon");
var sidebar = document.getElementById("sidebar");
var content = document.getElementById("content");

/**
 * show sidebar when screen is above 960px
 */
if(window.innerWidth >= 960){
    if(sidebar){
        pushContentSidebar();   
    }
}

/**
 * show sidebar when screen is resized above 960px
 */
window.addEventListener("resize", function(){
    if(window.innerWidth >= 960){
        pushContentSidebar();
    }
});

/**
 * show sidebar
 */
function pushContentSidebar(){
    sidebar.classList.add("show-sidebar");
    content.style.marginLeft = "60px";
}


/**
 * show/hide sidebar with hamburger menu
 */
if(menuIcon && (window.innerWidth < 960)){
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




/**
 * Account edit button 
 * Change inner text when clicked
 */
let editBtn = document.querySelectorAll(".account-edit-btn");
if(editBtn){

    editBtn.forEach(function(btn){
        btn.addEventListener("click", function(){
            
            if(btn.innerText == "Edit"){
                btn.innerText = "Close";                
            }
            else{
                btn.innerText = "Edit";
            }

        });
    });
}
    
/**
 * Maintenance request detail messages/detail tab
 * Slide to either messages or detail view when clicked
 */

const toggleSwitch = document.getElementById("request-toggle-switch");
const toggleSelect = document.getElementsByClassName("request-toggle-item");

const messageView = document.getElementById("message-view");
const detailView = document.getElementById("detail-view");

/**
 * Event listener on both messages and detail tabs
 */
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


/**
 * Set colour of priority badges relevant to text
 */
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


/**
 * Submit maintenance request 'Status' form on change 
 */
const statusForm = document.getElementById("status-form");

if(statusForm){
    statusForm.addEventListener("change", function(){
        this.submit();
    });
}

/**
 * Submit maintenance request list sort form on change
 */
const maintSearchForm = document.getElementById("maint-search-form");
const sortField = document.getElementById("id_ordering");

if(maintSearchForm){
    sortField.addEventListener("change", function(){
        maintSearchForm.submit();
    });
}


/**
 * csrf protection for maintenance request messages call to API. 
 * Copied from django documentation
 */
var csrftoken = getCookie('csrftoken');

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/**
 * Maintenance request messages functionality
 */

// author left hand side message template
let authorListItem =    `<li class="row"> 
                            <div class="col-11 col-sm-10"> 
                                <div class="row author-bg"> 
                                    <div class="col-3 col-sm-2 p-0 text-center"> 
                                        <img src="{ image_url }" alt="Prof"class="profile-icon rounded-circle img-fluid"> 
                                        <p class="sm-text m-1 bold"><i>"You"</i></p> 
                                    </div> 
                                    <div class="col-7 p-0 position-relative"> 
                                        <div class="col-12"> 
                                            <p class="md-text mb-2 mt-2">{ message }</p> 
                                            <p class="msg-id" hidden>{ id }</p>
                                        </div>
                                        <div class="col-12 date-posted">
                                            <hr class="m-1"> 
                                            <p class="sm-text mb-1 mt-1">{ date_posted }</p> 
                                        </div>
                                    </div>
                                </div> 
                            </div> 
                        </li>`;

// reciever right hand message template
let recieverListItem = `<li class="row justify-content-end">
                            <div class="offset-1 col-11 col-sm-10">
                                <div class="row receivers-bg justify-content-end">
                                    <div class="col-7 p-0 text-right position-relative">
                                        <div class="col-12">
                                            <p class="md-text mt-2 mb-2">{ message }</p> 
                                            <p class="msg-id" hidden>{ id }</p>
                                        </div>
                                        <div class="col-12 text-right date-posted">
                                            <hr class="m-1">
                                            <p class="sm-text mb-1">{ date_posted }</p>
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
            // clear message text box
            msgInput.val(''); 

            // convert date-time to local format
            let date = new Date(data['date_posted']);
            let datePosted = date.toLocaleString('en-GB', { timeZone: 'UTC', hour12: true });

            // replace variables in message template with input data. Append to container
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

// get all chat messages on current page is maint detail every 2 seconds
if(maintId){
    
    setInterval(

        // Get all new messages from API that are not currently in the DOM
        function getMessages(){
        
            const maintId = $('#maint-title').text();
            let lastMsgId = $('.msg-id').last().text();
            
            if(lastMsgId){
                $.get(`/api/chat/chat-message/?q=${maintId}&id=${lastMsgId}`, function(data){
    
                    if (data.length !== 0)
                        {
                            for(let i=0;i<data.length;i++) {
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

    
/**
 * Confirm modal
 * Replace modal variables with relevant data
 * Close modal with click of window
 */
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

/**
 * Add tenant functionality
 * Show add tenant search modal on click of button
 */
const addTenantBtn = document.getElementById('add-tenant-btn');

if(addTenantBtn){
    addTenantBtn.addEventListener('click', function(){
        addTenantModal();
    });
}

function addTenantModal(){
    document.getElementById('add-tenant-modal').style.display = 'block';
}

/**
 * Add tenant search form
 */
const searchTenForm = $('#txt-search');
const addTenForm = $('#add-tenant-form'); 
const addTenantList = $('#add-user-list');

/**
 * Check if suggestion list is empty and display message
 */
function emptyUserList(list, e, form){
    if(list.is(':empty')){
        list.append('<p class="md-text text-left m-2">No results found</p>');
    } 
    else if((e.keyCode == 8 && !form)){
        list.empty();
        list.append('<p class="md-text text-left m-2">No results found</p>');
    }
}

/**
 * Template for add tenant suggestion 
 */
let tenantSuggestion =  `<li class="row m-1 tenant-suggestion">
                            <div class="col-3 col-sm-4 col-md-3">
                                <img src="{ img_url }" alt="" class="add-tenant-icon rounded-circle">
                            </div>
                            <div class="col-7 text-left pl-1">
                                <p id="ten-name" class="md-text m-1">{ name }</p>
                            </div>
                        </li>`;

/**
 * Query user API on keyup
 */
searchTenForm.on('keyup', function(e){

    // get input data
    let formVal = searchTenForm.val();

    // clear tenant suggestions 
    addTenantList.empty();

    // disabled keys for add tenant search form
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
                    
                    // display text based on results
                    emptyUserList(addTenantList, e, formVal);
    
                });

                emptyUserList(addTenantList, e, formVal);
    
                // Submit add tenant form on click of user
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

/**
 * Dropdown modal for django messages
 * Show dropdown after redirect
 */
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

/**
 * Set text/colour of django error message 
 */
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

/**
 * Delete payment from payments list
 */
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

/**
 * Delete maintenance request modal
 * Dynamically set href of clicked maintenance request
 */
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

/**
 * Remove tenant modal when 'X' is clicked above tenant
 */
const deleteTenantBtn = document.querySelectorAll('#delete-tenant-btn');

if(deleteTenantBtn){
    deleteTenantBtn.forEach(function(btn){
        btn.addEventListener('click', function(e){

            // Display tenant name in confirm modal
            const firstName = this.parentNode.parentNode.querySelector('#ten-first').innerText;
            const lastName = this.parentNode.parentNode.querySelector('#ten-last').innerText;

            // Get tenant ID and rental ID from DOM
            const tenId = this.getAttribute('data-ten-Id');
            const rentId = this.getAttribute('data-rent-Id');

            // Set href using relevant values
            const href = `/tenant/remove/${rentId}/${tenId}`;
            const message = `Are you sure you want to remove ${firstName} ${lastName} from this property?`;
            const title = 'Remove tenant';

            confirmModal(title, message, href);
        
        });
    });
}

/**
 * Show/hide loading spinner
 */
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

