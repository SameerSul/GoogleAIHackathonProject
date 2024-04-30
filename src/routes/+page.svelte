<script>
    import logo from '$lib/images/LogoAI.png';
</script>

<section>
    <h1>RejuvAI - Your Personal AI Healthcare Overseer</h1>

    <div class="container">
       <h2 class="larger-text">Current Diseases</h2> 
																				<div class="textbox"></div>
        <div class="textbox"></div>
        <div class="textbox"></div>
        <div class="textbox"></div>
        <div class="large-textbox"></div>
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
        display: grid;
        grid-template-columns: repeat(2, 1fr); /* Two columns */
        gap: 20px; /* Adjust the gap between items */
    }

    .textbox {
        width: 300px;
        height: 50px;
        background-color: #A4F7C5; /* Fill color */
        border-radius: 10px;
    }

    .large-textbox {
        width: 500px;
        height: 200px;
        background-color: #A4F7C5; /* Fill color */
        border-radius: 10px;
    }

    h2 {
        margin-bottom: 20px;
    }

.larger-text {

    font-size:2em;
																				
}
</style>
