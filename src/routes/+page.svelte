<script>
	import logo from '$lib/images/LogoAI.png';
	document.addEventListener('DOMContentLoaded', function () {
		const diseaseInput = document.getElementById('diseaseInput');
		const medicationInput = document.getElementById('medicationInput');
		const surgeryInput = document.getElementById('surgeryInput');
		const miscInput = document.getElementById('miscInput');
		const getResultsButton = document.getElementById('getResultsButton');
		const outputResult = document.getElementById('outputResult');

		// Event listener for Get Results button
		getResultsButton.addEventListener('click', function () {
			// Example: Concatenate input values and display in outputResult
			const result = `Disease: ${diseaseInput.value}\nMedication: ${medicationInput.value}\nSurgery: ${surgeryInput.value}\nMisc: ${miscInput.value}`;
			outputResult.value = result;
		});
	});
</script>

<section>
	<h1 class="larger-text">RejuvAI - Your Personal AI Healthcare Overseer</h1>
	<h2 class="large-text">
		Interested in trying it out? Use the boxes below to better inform us on how we can help you
	</h2>

	<div class="container">
		<div class="input-container">
			<h2 class="large-text">Current Disease(s)</h2>
			<input id="diseaseInput" class="textbox" type="text" placeholder="Enter Disease" />
		</div>
		<div class="input-container">
			<h2 class="large-text">Current Prescribed Medication(s)</h2>
			<input
				id="medicationInput"
				class="textbox"
				type="text"
				placeholder="Enter Current Medication"
			/>
		</div>
		<div class="input-container">
			<h2 class="large-text">Previous Surgeries (if any)</h2>
			<input
				id="surgeryInput"
				class="textbox"
				type="text"
				placeholder="Enter Recent Surgeries (if any)"
			/>
		</div>
		<div class="input-container">
			<h2 class="large-text">Anything else important you wish to share?</h2>
			<input
				id="miscInput"
				class="textbox"
				type="text"
				placeholder="i.e Mental or Other Underlying Conditions"
			/>
		</div>
		<div class="button-container">
			<input id="getResultsButton" class="button" type="button" value="Get Results" />
		</div>
		<p />
		<div class="large-input-container">
			<h2 class="large-text">Program Result</h2>
			<input id="outputResult" class="large-textbox" type="text" placeholder="Output" />
		</div>
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		align-items: center;
		flex: 1;
	}

	.container {
		display: grid;
		grid-template-columns: repeat(2, 1fr); /* Two columns */
		gap: 20px; /* Adjust the gap between items */
	}

	.textbox,
	.large-textbox {
		width: 300px; /* Default width for regular textboxes */
		height: 50px; /* Default height for regular textboxes */
		background-color: #e8f8f5; /* Soothing pale teal background */
		border: 2px solid #008080; /* Teal border for better visibility */
		border-radius: 10px;
		padding: 2px; /* Padding inside the textbox for inner space */
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
		transition: box-shadow 0.3s ease-in-out, background-color 0.3s ease-in-out; /* Smooth transitions */
	}

	.large-textbox {
		width: 500px; /* Specific width for larger textbox */
		height: 200px; /* Specific height for larger textbox */
		background-color: #e8f8f5; /* Consistent soothing pale teal for larger textbox */
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Consistent shadow with regular textboxes */
		transition: box-shadow 0.3s ease-in-out, background-color 0.3s ease-in-out; /* Consistent transitions */
	}

	h2 {
		margin-bottom: 20px;
		color: #008080; /* Teal color for headings */
	}

	.large-text {
		font-size: 1.5em;
	}
	.larger-text {
		font-size: 2em;
	}

	/* Styles for input fields inside textboxes */
	input[type='text'] {
		width: 100%; /* Full width of the textbox */
		height: 46px; /* Slightly smaller to fit within 50px height of textbox */
		border: none;
		border-radius: 8px; /* Slightly less than textbox for aesthetic purpose */
		padding: 0 10px;
		font-size: 16px;
		box-sizing: border-box; /* Padding and border included in width/height */
		background-color: transparent; /* Ensure input background matches textbox */
		color: #333333; /* Dark gray for text */
	}

	input[type='text']:focus {
		outline: none;
		border-color: #ff6f61; /* Coral color when focused */
	}

	/* Button styles */
	button,
	.button {
		background-color: #ff6f61; /* Coral for buttons */
		color: #ffffff; /* White text for contrast */
		border: none;
		padding: 10px 20px;
		border-radius: 5px;
		cursor: pointer;
		transition: background-color 0.3s ease-in-out; /* Smooth transition for color change */
	}

	button:hover,
	.button:hover {
		background-color: #e65550; /* Darker coral on hover */
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Shadow effect on hover for button */
	}

	/* Hover effects for textboxes to improve interactivity */
	.textbox:hover,
	.large-textbox:hover {
		box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15); /* Larger shadow on hover for a lifting effect */
	}
</style>
