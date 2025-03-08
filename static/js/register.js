document.addEventListener("DOMContentLoaded", function() {
    // Get references to the buttons
    const submitButton = document.getElementById("submitButton");

    // Event listener for the Member button
    profileButton.addEventListener("click", function() {
        window.location.href = "member_reg"; // Redirect to Member registration page
    });

    // Event listener for the Trainer button
    trainerButton.addEventListener("click", function() {
        window.location.href = "trainer_reg"; // Redirect to Trainer registration page
    });

    // Event listener for the User button
    workoutsButton.addEventListener("click", function() {
        window.location.href = "user_reg"; // Redirect to User registration page
    });
});
