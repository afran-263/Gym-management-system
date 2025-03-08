// payment.js

document.addEventListener('DOMContentLoaded', function () {
    const paymentForm = document.getElementById('paymentForm');
    const errorMessage = document.getElementById('error-message');

    paymentForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form from submitting normally
        
        const formData = new FormData(paymentForm);
        
        // Make an AJAX request to submit the form data to the server
        fetch('/payment', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())  // Assuming the server sends JSON response
        .then(data => {
            if (data.success) {
                // Redirect to payment success page
                window.location.href = '/payment_success';
            } else {
                // Display error message
                errorMessage.textContent = data.message || 'An error occurred. Please try again.';
            }
        })
        .catch(error => {
            console.error('Error during payment submission:', error);
            errorMessage.textContent = 'There was an error processing your payment.';
        });
    });
});
