// collapsing sidebar
const menuIcon = document.getElementById('menu-icon');
const sidebar = document.getElementById('sidebar');
const content = document.getElementById('content');

if(window.innerWidth >= 960){
    sidebar.classList.add('show-sidebar');
    content.style.marginLeft = '60px';
}

else if(window.innerWidth < 960){
    menuIcon.addEventListener('click', function(){
        sidebar.classList.add('show-sidebar');
        event.stopPropagation();
    });

    document.addEventListener('click', function(e){
        if(e.target.classList.contains('show-sidebar') === false){
            sidebar.classList.remove('show-sidebar');
        }
    });
};

window.addEventListener('resize', function(){
    if(window.innerWidth >= 960){
        sidebar.classList.add('show-sidebar');
        content.style.marginLeft = '60px';
    }
});

// edit account button
const editBtn = document.getElementById('edit-btn');
    if(editBtn){
        editBtn.addEventListener('click', function(){
            if(editBtn.innerText == 'Edit'){
                editBtn.innerText = 'Close';
            }
            else{
                editBtn.innerText = 'Edit';
            }
        })
    }
    
// maintenance request detail toggle switch

const toggleSwitch = document.getElementById('request-toggle-switch');
const detailTab = document.getElementById('detail-tab');
const messagesTab = document.getElementById('messages-tab');
const toggleSelect = document.getElementsByClassName('request-toggle-item');

const messageView = document.getElementById('message-view');
const detailView = document.getElementById('detail-view');


for (let i = 0; i < toggleSelect.length; i++){
        toggleSelect[i].addEventListener('click', function(event){
            
            if(event.target.id == 'messages-tab'){
                toggleSwitch.classList.add('toggle-switch'); // moves toggle swith to message tab
                messageView.style.display = 'block'; // displays maintenance request message view
                detailView.style.display = 'none'; // hides maintenance request detail view
            }
            else if(event.target.id == 'detail-tab'){
                toggleSwitch.classList.remove('toggle-switch') // reverses toggle and displayed view
                messageView.style.display = 'none';
                detailView.style.display = 'block ';
            }
    })
}






