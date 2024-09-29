document.getElementById('jobDescriptionForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // Prevent default form submission

    const jobDescription = document.getElementById('jobDescription').value;

    // Send the job description to the backend API
    const response = await fetch('/generate-resume', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ jobDescription }),
    });

    // Get the response data (generated resume)
    const result = await response.json();
    
    // Display the generated resume on the page
    document.getElementById('resumeOutput').innerHTML = `
        <h2>Generated Resume</h2>
        <pre>${result.resumeContent}</pre>
    `;
});
