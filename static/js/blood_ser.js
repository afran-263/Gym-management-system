document.getElementById('search_button').addEventListener('click', function () {
    const bloodGroup = document.getElementById('blood_group').value.trim();

    if (bloodGroup) {
        fetchMembersByBloodGroup(bloodGroup);
    } else {
        alert('Please enter a valid blood group.');
    }
});

function fetchMembersByBloodGroup(bloodGroup) {
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = ''; // Clear previous results

    fetch(`/api/members?blood_group=${bloodGroup}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                displayMembersRowByRow(data.members);
            } else {
                resultsContainer.innerHTML = `<div class="error-message">${data.message}</div>`;
            }
        })
        .catch(error => {
            resultsContainer.innerHTML = `<div class="error-message">An error occurred. Please try again later.</div>`;
        });
}

function displayMembersRowByRow(members) {
    const resultsContainer = document.getElementById('results-container');
    
    // Create a header row for column names
    const headerDiv = document.createElement('div');
    headerDiv.classList.add('member-row', 'header-row');
    
    headerDiv.innerHTML = `
        <div><strong>Member ID</strong></div>
        <div><strong>Name</strong></div>
        <div><strong>Blood Group</strong></div>
        <div><strong>Email</strong></div>
        <div><strong>Phone</strong></div>
        <div><strong>Address</strong></div>
    `;
    
    resultsContainer.appendChild(headerDiv); // Append the header to the container
    
    // Create rows for each member
    members.forEach(member => {
        const rowDiv = document.createElement('div');
        rowDiv.classList.add('member-row');
        
        rowDiv.innerHTML = `
            <div>${member.member_id}</div>
            <div>${member.name}</div>
            <div>${member.blood_group}</div>
            <div>${member.email}</div>
            <div>${member.contact}</div>
            <div>${member.address}</div>
        `;
        
        resultsContainer.appendChild(rowDiv);
    });
}
