<script>
    // Optional scripting here
  </script>
  
  <main>
    <h1>Welcome to TRACE Dashboard <span>💻</span></h1>
    <h2>~ Team 11 - MinerSoft ~</h2>
  
    <div class="card">
      <h2>What would you like to do today?</h2>
      <div class="button-group">
        <a href="/crawler" class="button purple">🕷️ Go to Crawler</a>
        <a href="/ml" class="button blue">🤖 Go to ML Generator</a>
      </div>
    </div>
  
    <footer>© 2025 Team 11 - MinerSoft 🚀</footer>
  </main>
  
  <style>
    main {
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      padding: 2rem;
      background: linear-gradient(135deg, #d9cedf 0%, #6746a4 100%);
      color: #4c1d95;
    }
  
    h1 {
      font-size: 3.5rem;
      margin-top: 2rem;
      color: #fff;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
    }
  
    h2 {
      font-size: 1.8rem;
      margin: 1rem 0 2rem;
      color: #fff;
      font-weight: 600;
    }
  
    .card {
      background: linear-gradient(145deg, #c3b6ee, #a89bd4);
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
      border-radius: 20px;
      padding: 2.5rem;
      max-width: 600px;
      width: 100%;
      text-align: center;
      color: #fff;
    }
  
    .button-group {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-top: 1.5rem;
    }
  
    a.button {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 1rem 2rem;
      border-radius: 50px;
      font-size: 1.2rem;
      font-weight: 600;
      text-decoration: none;
      color: white;
      transition: all 0.3s ease;
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
      cursor: pointer;
    }
  
    a.button.purple {
      background: linear-gradient(90deg, #7e40c6, #431176);
    }
  
    a.button.blue {
      background: linear-gradient(90deg, #8b35d6, #55107d);
    }
  
    a.button:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
  
    footer {
      margin-top: auto;
      padding: 1rem;
      font-size: 0.9rem;
      color: #ffffff;
    }
  </style>