// JavaScript to navigate to member_login.html on click
document.addEventListener("DOMContentLoaded", function(){
document.getElementById('member').addEventListener('click', function() {
    window.location.href = 'member_login';
});

document.getElementById('user').addEventListener('click', function() {
    window.location.href = 'user_login';
});
});