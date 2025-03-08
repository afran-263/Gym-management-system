document.addEventListener("DOMContentLoaded", function() {
    // Access buttons by their IDs
    const profileButton = document.getElementById("profileButton");
    const paymentHistoryButton = document.getElementById("paymentHistoryButton");
    const trainerButton = document.getElementById("trainerButton");
    const workoutsButton = document.getElementById("workoutsButton");

    // Event listener for the Profile button
    profileButton.addEventListener("click", function() {
        window.location.href = "member_profile"; // Redirect to member profile page
    });

    // Event listener for the Payment History button
    paymentHistoryButton.addEventListener("click", function() {
        window.location.href = "payment_his"; // Redirect to payment history page
    });

    // Event listener for the Trainer button
    trainerButton.addEventListener("click", function() {
        window.location.href = "trainer_profile"; // Redirect to trainer profile page
    });

    // Event listener for the Workouts button
    workoutsButton.addEventListener("click", function() {
        window.location.href = "workouts"; // Redirect to workouts page

    });
    equipment.addEventListener("click", function() {
        window.location.href = "equip_dis"; // Redirect to workouts page
});
});
