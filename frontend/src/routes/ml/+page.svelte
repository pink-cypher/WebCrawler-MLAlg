<script lang="ts">
    let generatedCredentials: string[] = [];
    let error: string = '';
  
    async function generateCredentials() {
      error = '';
      try {
        const response = await fetch('http://localhost:8000/ml/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });
  
        if (!response.ok) {
          throw new Error('Failed to generate credentials');
        }
  
        const data = await response.json();
        generatedCredentials = data.credentials;
      } catch (err) {
        error = (err as Error).message;
      }
    }
  </script>
  
  <div class="page-container">
    <div class="content-box">
      <h1>ML Credential Generator</h1>
  
      <button on:click={generateCredentials}>Generate Credentials</button>
  
      {#if error}
        <p class="error">{error}</p>
      {/if}
  
      {#if generatedCredentials.length > 0}
        <h2>Generated Credentials</h2>
        <ul class="credentials-list">
          {#each generatedCredentials as cred}
            <li>{cred}</li>
          {/each}
        </ul>
      {/if}
    </div>
  </div>
  
  <style>
    /* Background and Layout */
    .page-container {
      background-color: #7b69b3; /* Same as crawler */
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 2rem;
    }
  
    /* Main Card Styling */
    .content-box {
      background-color: #ffffff;
      padding: 2rem 3rem;
      border-radius: 12px;
      width: 100%;
      max-width: 600px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
  
    /* Typography */
    h1, h2 {
      color: #5d4b8c;
      margin-bottom: 1.5rem;
    }
  
    /* Buttons */
    button {
      background-color: #5d4b8c;
      color: #fff;
      border: none;
      padding: 0.75rem 1.5rem;
      border-radius: 6px;
      cursor: pointer;
      transition: background-color 0.3s ease;
      font-size: 1rem;
    }
  
    button:hover {
      background-color: #4a3b75;
    }
  
    /* Credentials List */
    .credentials-list {
      background-color: #f3f3f3;
      padding: 1rem;
      border-radius: 6px;
      list-style: none;
      max-height: 300px;
      overflow-y: auto;
      margin: 1rem 0 0 0;
      text-align: left; /* Left align list items inside the centered box */
    }
  
    .credentials-list li {
      padding: 0.5rem;
      border-bottom: 1px solid #ddd;
      color: #333;
    }
  
    /* Error Message */
    .error {
      color: #c62828;
      background-color: #ffebee;
      padding: 0.75rem;
      margin-top: 1rem;
      border-radius: 4px;
    }
  </style>