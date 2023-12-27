const likeItems = document.getElementsByClassName('like-container');

for (let item in likeItems){
button.addEventListener('click', function() {
     console.log("HELLLLLO")
     [button, count] =item.children;
     count.innerHTML = Number(count.innerHTML)+1;
});
}