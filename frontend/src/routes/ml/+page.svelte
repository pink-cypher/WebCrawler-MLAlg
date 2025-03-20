<script lang="ts">
  import "./ml.css"; // Import the CSS file from the same folder

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
      <h2 class="credentials">Generated Credentials:</h2>
      <ul>
        {#each generatedCredentials as cred}
          <li class="credential-item">{cred}</li>
        {/each}
      </ul>
    {/if}
  </div>
</div>