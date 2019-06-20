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

    editBtn.addEventListener('click', function(){
        if(editBtn.innerText == 'Edit'){
            editBtn.innerText = 'Close';
        }
        else{
            editBtn.innerText = 'Edit';
        }
    })


