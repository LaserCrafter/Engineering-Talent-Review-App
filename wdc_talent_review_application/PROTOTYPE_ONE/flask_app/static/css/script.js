const container = document.getElementById('container'); //select container element
const registerBtn = document.getElementById('register'); //select register element
const loginBtn = document.getElementById('login'); //select login element

registerBtn.addEventListener('click', () => { //add functionality for sign up button when clicked
    container.classList.add("active"); //add class active to container
});

loginBtn.addEventListener('click', () => { //add functionality for login button when clicked
    container.classList.remove("active"); // remove active class from container when button is clicked.
});