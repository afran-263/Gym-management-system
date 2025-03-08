document.addEventListener("DOMContentLoaded", function() {
    // Access buttons by their IDs
    const payment = document.getElementById("payment");

    payment.addEventListener("click", function() {
        window.location.href = "payment"; // Redirect to workouts page
});
});
