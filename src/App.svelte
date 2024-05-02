<script>
    let currentDisease = '';
    let currentMedication = '';
    let previousSurgeries = '';
    let miscInfo = '';
    let responseMessage = '';

    async function getResults() {
        let response = await fetch('http://localhost:5174/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                disease: currentDisease,
                medication: currentMedication,
                surgery: previousSurgeries,
                misc: miscInfo
            })
        });
        let data = await response.json();
        responseMessage = data.response;
    }
</script>

<main>
    <!-- Input fields for user input -->
    <!-- Bind each input field to respective variables -->
    <input type="text" bind:value={currentDisease} placeholder="Enter Current Disease(s)">
    <input type="text" bind:value={currentMedication} placeholder="Enter Current Medication(s)">
    <input type="text" bind:value={previousSurgeries} placeholder="Enter Previous Surgeries (if any)">
    <input type="text" bind:value={miscInfo} placeholder="Anything else important you wish to share?">
    
    <!-- Button to trigger content generation -->
    <button on:click={getResults}>Get Results</button>
    
    <!-- Display generated content -->
    <p>Program Result: {responseMessage}</p>
</main>
