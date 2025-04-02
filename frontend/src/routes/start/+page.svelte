<script>
    // No logic needed here unless you want animations or effects
  </script>
  
  <main class="start-selection">
    <h1>Choose an Action</h1>
    <div class="options">
      <a href="/crawler" class="action-btn">🕷️ Go to Crawler</a>
      <a href="/ml" class="action-btn">🤖 Go to ML Generator</a>
    </div>
  </main>
  
  <style>
    .start-selection {
      min-height: 100vh;
      background-color: #f6f6f6;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: 'Segoe UI', sans-serif;
      text-align: center;
      padding: 2rem;
    }
  
    h1 {
      font-size: 2rem;
      margin-bottom: 2rem;
      color: #333;
    }
  
    .options {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }
  
    .action-btn {
      background-color: #3bb3bd;
      color: white;
      text-decoration: none;
      padding: 1rem 2rem;
      font-size: 1.2rem;
      font-weight: 600;
      border-radius: 8px;
      transition: all 0.3s ease;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
  
    .action-btn:hover {
      background-color: #329da5;
      transform: scale(1.05);
    }
  </style>