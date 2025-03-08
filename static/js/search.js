document.getElementById('search_button').addEventListener('click', function () {
    const memberId = document.getElementById('member_id').value;

    if (memberId) {
        fetchMemberProfile(memberId);
    } else {
        alert('Please enter a valid Member ID.');
    }
});

function fetchMemberProfile(memberId) {
    const profileDetailsDiv = document.getElementById('profile-details');
    profileDetailsDiv.innerHTML = ''; // Clear any previous data
    profileDetailsDiv.style.display = 'none'; // Hide details initially

    fetch(`/api/member/${memberId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Display member details
                const member = data.member;
                profileDetailsDiv.innerHTML = `
                    <h2>Member Profile</h2>
                    <p><strong>Name:</strong> ${member.name}</p>
                    <p><strong>Age:</strong> ${member.age}</p>
                    <p><strong>DOB:</strong> ${member.dob}</p>
                    <p><strong>Gender:</strong> ${member.gender}</p>
                    <p><strong>Blood Group:</strong> ${member.blood_group}</p>
                    <p><strong>Email:</strong> ${member.email}</p>
                    <p><strong>Phone:</strong> ${member.contact}</p>
                    <p><strong>Address:</strong> ${member.address}</p>
                    <p><strong>Package:</strong> ${member.package}</p>
                    <p><strong>Instructor Id:</strong> ${member.instructor_id}</p>
                    <p><strong>Joined:</strong> ${new Date(member.joining_date).toLocaleDateString()}</p>
                    <p><strong>Ending:</strong> ${new Date(member.ending_date).toLocaleDateString()}</p>
                `;
                profileDetailsDiv.style.display = 'block';
            } else {
                // Handle member not found
                profileDetailsDiv.innerHTML = `<p class="error">${data.message}</p>`;
                profileDetailsDiv.style.display = 'block';
            }
        })
        .catch(error => {
            profileDetailsDiv.innerHTML = `<p class="error">An error occurred while fetching the profile. Please try again later.</p>`;
            profileDetailsDiv.style.display = 'block';
        });
}
