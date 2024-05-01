<script>
  let currentDisease = '';
  let currentMedication = '';
  let previousSurgeries = '';
  let miscInfo = '';
  let responseMessage = '';

  // Function to call the API
  function getResults() {
    fetch('http://localhost:5174/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json'
      },
      body: JSON.stringify({
        disease: currentDisease,
        medication: currentMedication,
        surgery: previousSurgeries,
        misc: miscInfo
      })
    })
    .then(response => response.json())
    .then(data => {
      responseMessage = data.response;
    })
    .catch(error => {
      console.error('Error:', error);
      responseMessage = 'Error: ' + error.message;
    });
  }
</script>

<main>
  <h1>RejuvAI - Your Personal AI Healthcare Overseer</h1>
  <h2>Interested in trying it out? Use the boxes below to better inform us on how we can help you</h2>

  <input type="text" bind:value={currentDisease} placeholder="Enter Current Disease(s)">
  <input type="text" bind:value={currentMedication} placeholder="Enter Current Medication(s)">
  <input type="text" bind:value={previousSurgeries} placeholder="Enter Previous Surgeries (if any)">
  <input type="text" bind:value={miscInfo} placeholder="Anything else important you wish to share?">
  
  <button on:click={getResults}>Get Results</button>
  
  <p>Program Result: {responseMessage}</p>

  <!-- Dynamically display current data -->
  <div class="current-data">
    <p>Current Disease(s): {currentDisease}</p>
    <p>Current Medication(s): {currentMedication}</p>
    <p>Previous Surgeries: {previousSurgeries}</p>
    <p>Miscellaneous Info: {miscInfo}</p>
  </div>
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
  }
  input, button {
    margin-top: 10px;
  }
</style>
