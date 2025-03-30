<script>
  // Optional logic
</script>

<main>
  <!-- Top Navigation with Logo and Links -->
  <nav class="top-nav">
    <!-- Left: Logo -->
    <div class="logo-svg" aria-label="TRACE Logo">
      <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="36" height="36">
        <!-- Hexagon -->
        <polygon points="50,5 93,27 93,73 50,95 7,73 7,27"
          fill="none"
          stroke="#3bb3bd"
          stroke-width="5"
        />
        <!-- Stylized "C" inside -->
        <path d="M65 35 Q55 25, 40 35 Q25 50, 40 65 Q55 75, 65 65"
          fill="none"
          stroke="#3bb3bd"
          stroke-width="5"
          stroke-linecap="round"
        />
      </svg>
    </div>

    <!-- Right: Navigation Links -->
    <div class="nav-links">
      <a href="/dashboard">Dashboard</a>
      <a href="/settings">Settings</a>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero">
    <h1>
      Elevate Your Security Strategy with
      <span class="trace-highlight">TRACE</span>
    </h1>
    <p class="subtitle">
      A Cybersecurity Platform to Protect Your Digital Assets. Detect<br />
      Vulnerabilities, Strengthen Defense, and Secure Your Network Seamlessly.<br />
      Gain Real-Time Insights and Proactive Protection.
    </p>
    <a class="start-btn" href="/crawler">START</a>
  </section>

  <footer>© 2025 Team 11 - MinerSoft 🚀</footer>
</main>

<style>
  main {
    background-color: #f6f6f6;
    min-height: 100vh;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 2rem;
    position: relative;
    overflow: hidden;
  }

  .top-nav {
    width: 100%;
    position: absolute;
    top: 1.5rem;
    left: 2rem;
    right: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }

  .logo-svg svg {
    display: block;
  }

  .nav-links {
    display: flex;
    gap: 2rem;
    font-weight: 500;
  }

  .nav-links a {
    color: #444;
    text-decoration: none;
    font-size: 1rem;
  }

  .nav-links a:hover {
    color: #3bb3bd;
  }

  .hero {
    z-index: 1;
    padding: 3rem 2rem;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: #111;
    margin-bottom: 1rem;
  }

  .trace-highlight {
    color: #3bb3bd;
    border: 2px solid #3bb3bd;
    padding: 0.25rem 0.5rem;
    background-color: #e6f9fa;
    border-radius: 6px;
  }

  .subtitle {
    font-size: 1rem;
    color: #444;
    max-width: 600px;
    margin: 0 auto 2rem;
    line-height: 1.6;
  }

  .start-btn {
    background-color: #3bb3bd;
    color: white;
    padding: 0.6rem 2rem;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.2s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    display: inline-block;
  }

  .start-btn:hover {
    background-color: #329da5;
  }

  footer {
    margin-top: auto;
    padding: 1rem;
    font-size: 0.9rem;
    color: #999;
    z-index: 2;
  }

  main::before {
    content: "";
    position: absolute;
    inset: 0;
    background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25'%3E%3Cg stroke='%23cccccc' stroke-width='1' stroke-linecap='round'%3E%3Cpath d='M0 160 H300 L380 200 H1440'/%3E%3Cpath d='M0 200 H200 L280 240 H1440'/%3E%3Cpath d='M0 240 H150 L230 280 H1440'/%3E%3C/g%3E%3C/svg%3E") no-repeat center center / cover;
    opacity: 0.1;
    z-index: 0;
    pointer-events: none;
  }
</style>