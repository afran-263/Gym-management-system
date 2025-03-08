document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/user_login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ username, password })
        });

        const data = await response.json();

        if (response.status === 200) {
            alert(data.message);  // Show success message or redirect
        } else {
            document.getElementById('error-message').textContent = data.message;
        }
    } catch (error) {
        document.getElementById('error-message').textContent = "An error occurred. Please try again.";
    }
});
