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
const detail = document.getElementById('detail');
const messages = document.getElementById('messages');
const toggleSelect = document.getElementsByClassName('request-toggle-item');



for (let i = 0; i < toggleSelect.length; i++){
        toggleSelect[i].addEventListener('click', function(event){
            
            if(event.target.id == 'messages'){
                toggleSwitch.classList.add('toggle-switch')
            }
            else if(event.target.id == 'detail'){
                toggleSwitch.classList.remove('toggle-switch')
            }
    })
}




