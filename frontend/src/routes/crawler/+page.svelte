<script lang="ts">
    let url: string = '';
    let depth: number = 2;
    let crawledResults: string[] = [];
    let error: string = '';
    let isLoading = false;
  
    // Start Crawl Function
    async function startCrawl() {
      error = '';
      crawledResults = [];
      isLoading = true;
  
      try {
        const response = await fetch(`http://localhost:8000/crawl?url=${encodeURIComponent(url)}&depth=${depth}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' }
        });
  
        if (!response.ok) {
          throw new Error('Failed to crawl');
        }
  
        const data = await response.json();
        crawledResults = data.crawled_urls;
      } catch (err) {
        error = (err as Error).message;
      } finally {
        isLoading = false;
      }
    }
  
    // NLP Processing Function
    async function processWithNLP() {
      try {
        const response = await fetch('http://localhost:8000/nlp/clean', {
          method: 'POST'
        });
  
        if (!response.ok) {
          throw new Error('Failed to process with NLP');
        }
  
        alert('Data cleaned with NLP successfully!');
      } catch (err) {
        error = (err as Error).message;
      }
    }
  
    // Generate Credentials Function
    async function generateCredentials() {
      try {
        const response = await fetch('http://localhost:8000/ml/generate', {
          method: 'POST'
        });
  
        if (!response.ok) {
          throw new Error('Failed to generate credentials');
        }
  
        const data = await response.json();
        alert(`Generated credentials:\n${JSON.stringify(data.credentials, null, 2)}`);
      } catch (err) {
        error = (err as Error).message;
      }
    }
  </script>
  
  <!-- Layout Markup -->
  <div class="page-container">
    <div class="content-box">
      <h1>Web Crawler</h1>
  
      <!-- Form Section -->
      <div class="form-section">
        <label for="url">Target URL</label>
        <input id="url" type="text" bind:value={url} placeholder="https://example.com" />
  
        <label for="depth">Crawl Depth</label>
        <input id="depth" type="number" bind:value={depth} min="1" max="10" />
  
        <button on:click={startCrawl} disabled={isLoading}>
          {isLoading ? 'Crawling...' : 'Start Crawl'}
        </button>
  
        {#if error}
          <p class="error">{error}</p>
        {/if}
      </div>
  
      <!-- Results Section -->
      {#if crawledResults.length > 0}
        <h2>Crawled URLs</h2>
        <ul class="results-list">
          {#each crawledResults as link}
            <li>{link}</li>
          {/each}
        </ul>
  
        <div class="action-buttons">
          <button on:click={processWithNLP}>Process with NLP</button>
          <button on:click={generateCredentials}>Generate Credentials</button>
        </div>
      {/if}
    </div>
  </div>
  
  <!-- Styling -->
  <style>
    .page-container {
      background-color: #7b69b3; /* Purple background similar to ML */
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 2rem;
    }
  
    .content-box {
      background-color: #ffffff;
      padding: 2rem 3rem;
      border-radius: 12px;
      width: 600px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
      text-align: center;
    }
  
    h1, h2 {
      color: #5d4b8c;
      margin-bottom: 1rem;
    }
  
    .form-section {
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
      margin-bottom: 2rem;
      text-align: left;
    }
  
    label {
      font-weight: bold;
      color: #333;
    }
  
    input {
      padding: 0.75rem;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 1rem;
      width: 100%;
    }
  
    button {
      background-color: #5d4b8c;
      color: #fff;
      border: none;
      padding: 0.75rem;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      transition: background-color 0.3s ease, transform 0.2s ease;
    }
  
    button:disabled {
      background-color: #aaa;
      cursor: not-allowed;
    }
  
    button:hover:not(:disabled) {
      background-color: #4a3b75;
      transform: translateY(-1px);
    }
  
    .results-list {
      background: #f3f3f3;
      padding: 1rem;
      border-radius: 6px;
      list-style-type: none;
      max-height: 300px;
      overflow-y: auto;
      margin-bottom: 1.5rem;
    }
  
    .results-list li {
      padding: 0.5rem;
      border-bottom: 1px solid #ddd;
      color: #333;
      text-align: left;
    }
  
    .action-buttons {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
    }
  
    .error {
      color: #c62828;
      background-color: #ffebee;
      padding: 0.75rem;
      border-radius: 4px;
    }
  </style>