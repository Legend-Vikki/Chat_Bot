function askQuestion() {
    const query = document.getElementById('user-query').value;
    if (!query) {
        alert("Please enter a query!");
        return;
    }

    // Send the query to the Flask backend
    fetch(`/ask?query=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            const responseBox = document.getElementById('response-box');
            responseBox.innerHTML = data.response;
        })
        .catch(error => {
            console.error("Error:", error);
        });
}


// Function to copy text to clipboard when the user clicks the copy icon
function copyToClipboard(event) {
    // Get the text content of the list item that was clicked
    const questionText = event.target.closest('li').innerText.trim();

    // Create a temporary text area element to copy the text
    const textArea = document.createElement('textarea');
    textArea.value = questionText;
    document.body.appendChild(textArea);
    
    // Select and copy the text inside the text area
    textArea.select();
    document.execCommand('copy');
    
    // Remove the temporary text area
    document.body.removeChild(textArea);
}
