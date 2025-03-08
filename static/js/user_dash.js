document.addEventListener("DOMContentLoaded", function() {
    // Access buttons by their IDs
    const registerButton = document.getElementById("registerButton");
    const paymentButton = document.getElementById("paymentButton");
    const searchButton = document.getElementById("searchButton");
    const bloodGroupButton = document.getElementById("bloodGroupButton");
    const paymentHistoryButton = document.getElementById("paymentHistoryButton");

    // Event listener for the Register button
    registerButton.addEventListener("click", function() {
        window.location.href = "register"; // Redirect to the registration page
    });

    // Event listener for the Payment button
    paymentButton.addEventListener("click", function() {
        window.location.href = "payment"; // Redirect to the payment page
    });

    // Event listener for the Search button
    searchButton.addEventListener("click", function() {
        window.location.href = "search"; // Redirect to the search page
    });

    // Event listener for the Blood Group button
    bloodGroupButton.addEventListener("click", function() {
        window.location.href = "blood_ser"; // Redirect to the blood group page
    });

    // Event listener for the Payment History button
    paymentHistoryButton.addEventListener("click", function() {
        window.location.href = "user_payhis"; // Redirect to the payment history page
    });

    equipment.addEventListener("click", function() {
        window.location.href = "equip"; // Redirect to the payment history page
    });
});
