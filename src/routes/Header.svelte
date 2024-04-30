<script>
    import { page } from '$app/stores';
    import logo from '$lib/images/LogoAI.png';
    import rectangle from '$lib/images/Rectangle 1.png';
</script>

<header>
    <div class="container">
        <img src={rectangle} alt="Logo" class="rectangle" />
        <nav>
            <ul>
                <li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
                    <a href="/">Home</a>
                </li>
                <li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
                    <a href="/about">About</a>
                </li>
                <li aria-current={$page.url.pathname === '/faq' ? 'page' : undefined}>
                    <a href="/faq">FAQ</a>
                </li>
                <li aria-current={$page.url.pathname === '/contact' ? 'page' : undefined}>
                    <a href="/contact">Contact</a>
                </li>
            </ul>
        </nav>
        <img src={logo} alt="Logo" class="logo" />
    </div>
</header>

<style>
    header {
        position: relative; /* Ensure proper positioning for child elements */
    }

    .container {
        position: relative; /* Position the container */
    }

    .rectangle {
        width: 100%; /* Cover the entire row */
    }

    nav {
        position: absolute; /* Position the navigation bar */
        top: 20%; /* Adjust the top value to move the nav down */
        left: 50%; /* Align the left of the nav to the center of the rectangle */
        transform: translateX(-50%); /* Center the nav horizontally */
        z-index: 1; /* Ensure the nav is above the logo */
    }

    ul {
        padding: 0;
        margin: 0;
        list-style: none;
        display: flex; /* Ensure flexbox layout for the navigation links */
    }

    li {
        margin: 0 40px; /* Adjust the margin to increase spacing between nav elements */
    }

    nav a {
        color: white; /* Adjust color as needed */
        text-decoration: none;
        font-weight: bold;
        font-size: 1.75em; /* Adjust font size as needed */
    }

    .logo {
        position: absolute; /* Position the logo */
        top: 0px; /* Adjust the top position as needed */
        left: 20px; /* Adjust the left position as needed */
        z-index: 2; /* Ensure the logo is above the nav */
    }

    a:hover {
        color: #bfd1e5; /* Change color on hover */
    }
</style>
