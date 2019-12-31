const item_head = document.getElementById("item-head");
const crops = document.getElementById('crops');
const livestock = document.getElementById('livestock');
const vet = document.getElementById('vet');
const forest = document.getElementById('forestry');

// side-nav
side_nav = document.getElementById('side-nav');
ham = document.getElementById('ham-nav');
close = document.getElementById('close-side');

ham.addEventListener('click',()=>
    side_nav.style.width = '50%'
);

close.addEventListener('click',()=>
    side_nav.style.width = '0%'
);

crops.addEventListener('click', ()=>
item_head.innerHTML = crops.innerText,
item_head.classList.add('nav-active')
);

livestock.addEventListener('click', ()=>
item_head.innerHTML = livestock.innerText,
item_head.classList.add('nav-active')
);

vet.addEventListener('click', ()=>
item_head.innerHTML = vet.innerText,
item_head.classList.add('nav-active')
);

forest.addEventListener('click', ()=>
item_head.innerHTML = forest.innerText,
item_head.classList.add('nav-active')
);

