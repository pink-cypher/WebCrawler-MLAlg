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
  
  <h1>ML Credential Generator</h1>
  
  <button on:click={generateCredentials}>Generate Credentials</button>
  
  {#if error}
    <p style="color: red;">{error}</p>
  {/if}
  
  {#if generatedCredentials.length > 0}
    <h2>Generated Credentials:</h2>
    <ul>
      {#each generatedCredentials as cred}
        <li>{cred}</li>
      {/each}
    </ul>
  {/if}