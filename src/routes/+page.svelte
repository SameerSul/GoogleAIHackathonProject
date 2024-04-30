<script>
    import logo from '$lib/images/LogoAI.png';
</script>

<section>
    <h1 class="larger-text">RejuvAI - Your Personal AI Healthcare Overseer</h1>
    <h2 class="large-text">Interested in trying it out? Use the boxes below to better inform us on how we can help you</h2>

    <div class="container">
        <div class = "input-container">
            <h2 class="large-text">Current Disease(s)</h2>
            <input class = "textbox" type="Disease" placeholder="Enter Disease">
        </div>
        <div class = "input-container">
            <h2 class="large-text">Current Prescribed Medication(s)</h2>
            <input class = "textbox" type="Medication" placeholder="Enter Current Medication">
        </div>
        <div class = "input-container">
            <h2 class="large-text">Previous Surgeries (if any)</h2>
            <input class = "textbox" type="Surgery" placeholder="Enter Recent Surgeries (if any)">
        </div>
        <div class = "input-container">
            <h2 class="large-text">Anything else important you wish to share?</h2>
            <input class = "textbox" type="Misc" placeholder="i.e Mental or Other Underlying Conditions">
        </div>
                <div class="button-container"><input class="button" type="button" value="Get Results"> </div>
        <p></p>
        <div class = "large-input-container">
            <h2 class="large-text">Program Result</h2>
            <input class = "large-textbox" type="Disease" placeholder="Output">
        </div>
       
    </div>
</section>

<style>
    section {
        display: flex;
        flex-direction: column;
        align-items: center;
        flex: 1;
        padding-top: 20px;
    }

    .container {
        padding: 20px;
        display: grid;
        grid-template-columns: repeat(2, 1fr); /* Two columns */
        gap: 40px; /* Adjust the gap between items */
    }

    .input-container {
        background: linear-gradient(to right, #0F79EE, #000000);
        background-clip: text;
        color: transparent;
    }
    
    .large-input-container {
        display:block;
        background: linear-gradient(to right, #0F79EE, #000000);
        background-clip: text;
        color: transparent;
    }

    .button-container {
        display:block;
        background: linear-gradient(to right, #0F79EE, #000000);
        background-clip: text;
        color: transparent;
    }



    .textbox {
        width: 300px;
        height: 50px;
        font-weight:bold;
        background-color: #A4F7C5; /* Fill color */
        border-radius: 10px;
    }

    .large-textbox {
        width: 500px;
        height: 200px;
        font-weight:bold;
        background-color: #A4F7C5; /* Fill color */
        border-radius: 10px;
    }
    .button {
        border: none;
        font-weight:bolder;
        display:flex;
        border-radius: 5px; /* Adjust the radius as needed */
        padding: 10px 20px; /* Adjust padding as needed */
        background-color: #d6d4ff; /* Change background color if desired */
        color: #000000; /* Change text color if desired */
        cursor: pointer;
    }


    .large-text {
        font-weight: bold;
        font-size: 1.5em;
        background: linear-gradient(to right, #0F79EE, #000000);
        background-clip: text;
        color: transparent;
    }



.larger-text {
    font-weight:bold;
    font-size:2em;
    background: linear-gradient(to right, #0F79EE, #000000);
    background-clip: text;
    color: transparent;																			
}


</style>
