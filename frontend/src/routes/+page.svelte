<script>
  // Empty for now
</script>

<style>
  body {
    margin: 0;
    font-family: 'Poppins', sans-serif;
    background-color: #f3f4f6;
    color: #4c1d95;
    text-align: center;
  }

  h1 {
    font-size: 3rem;
    margin-top: 2rem;
    color: #000000;
  }

  .card {
    background-color: #c4b5fd;
    border-radius: 1rem;
    padding: 2.5rem;
    margin: 2rem auto;
    max-width: 800px;
    width: 80%;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  h2 {
    font-size: 1.8rem;
    margin-bottom: 2rem;
    color: #581c87;
  }

  .button-group {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    margin-top: 1rem;
  }

  a.button {
    background-color: #a78bfa;
    color: white;
    padding: 1rem;
    border-radius: 2rem;
    text-align: center;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.2rem;
    transition: background-color 0.3s, transform 0.2s;
  }

  a.button:hover {
    background-color: #7c3aed;
    transform: scale(1.03);
  }
</style>

<h1>Welcome to TRACE Dashboard 💻</h1>
<h2> ~Team 11 - MinerSoft~</h2>

<div class="card">
  <h2>What would you like to do today?</h2>
  <div class="button-group">
    <a href="/crawler" class="button">🕷️ Go to Crawler</a>
    <a href="/ml" class="button">🤖 Go to ML Generator</a>
  </div>
</div>