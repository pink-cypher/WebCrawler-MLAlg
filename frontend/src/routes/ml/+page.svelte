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


<style>
  
  .page-container {
    background: linear-gradient(to bottom right, #6b46c1, #805ad5);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    margin:0;
    font-family: 'Arial', sans-serif;
  }

  .content-box {
    max-width: 400px;
    width: 100%;
    background: rgba(128, 90, 213, 0.9);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  }

  h1 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
  }

  button {
    background-color: #9f7aea;
    border: none;
    color: white;
    padding: 10px 15px;
    font-size: 1rem;
    border-radius: 8px;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  button:hover {
    background-color: #805ad5;
  }

  .error {
    color: #ff6b6b;
    margin-top: 10px;
  }

  .credentials {
    margin-top: 20px;
  }

  .credential-item {
    background: rgba(175, 32, 219, 0.2);
    padding: 8px;
    border-radius: 6px;
    margin-top: 5px;
  }
</style>

<div class="page-container">
  <div class="content-box">
    <h1>ML Credential Generator</h1>

    <button on:click={generateCredentials}>Generate Credentials</button>

    {#if error}
      <p class="error">{error}</p>
    {/if}

    {#if generatedCredentials.length > 0}
      <h2 class="credentials">Generated Credentials:</h2>
      <ul>
        {#each generatedCredentials as cred}
          <li class="credential-item">{cred}</li>
        {/each}
      </ul>
    {/if}
  </div>
</div>