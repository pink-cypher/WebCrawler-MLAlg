<script lang="ts">
  let url: string = '';
  let depth: number = 2;
  let crawledResults: string[] = [];
  let error: string = '';
  let isLoading = false;
  let setupExpanded = true;
  let outputExpanded = true;
  let activeTab = 'crawler';

  async function startCrawl() {
    error = '';
    crawledResults = []; // reset
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
      console.log('Response data:', data);
      crawledResults = data.crawled_urls;
    } catch (err) {
      console.error(err);
      error = (err as Error).message;
    } finally {
      isLoading = false;
    }
  }

  async function processWithNLP() {
    try {
      const response = await fetch('http://localhost:8000/nlp/clean', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      
      if (!response.ok) {
        throw new Error('Failed to process with NLP');
      }
      
      alert('Data processed with NLP successfully!');
    } catch (err) {
      console.error(err);
      error = (err as Error).message;
    }
  }

  async function generateCredentials() {
    try {
      const response = await fetch('http://localhost:8000/ml/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      
      if (!response.ok) {
        throw new Error('Failed to generate credentials');
      }
      
      const data = await response.json();
      alert('Credentials generated successfully!');
    } catch (err) {
      console.error(err);
      error = (err as Error).message;
    }
  }

  function setActiveTab(tab: string) {
    activeTab = tab;
  }
</script>

<div class="crawler-container">
  <h2 class="crawler-title">Web Crawler:</h2>

  <div class="crawler-content">
    <div class="crawler-section setup">
      <div class="section-header" on:click={() => setupExpanded = !setupExpanded}>
        <h3>Set-up:</h3>
        <button class="toggle-btn">
          {#if setupExpanded}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
          {:else}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          {/if}
        </button>
      </div>
      
      {#if setupExpanded}
        <div class="section-content">
          <div class="form-group">
            <label for="url">Target URL:</label>
            <input type="text" id="url" bind:value={url} placeholder="https://example.com" />
          </div>
          
          <div class="form-group">
            <label for="depth">Crawl Depth:</label>
            <input type="number" id="depth" bind:value={depth} min="1" max="5" />
            <span class="hint">Higher values take longer but find more pages</span>
          </div>
          
          <button class="primary-btn" on:click={startCrawl} disabled={isLoading}>
            {isLoading ? 'Crawling...' : 'Start Crawling'}
          </button>
          
          {#if error}
            <div class="error-box">
              <p>{error}</p>
            </div>
          {/if}
        </div>
      {/if}
    </div>

    <div class="crawler-section output">
      <div class="section-header" on:click={() => outputExpanded = !outputExpanded}>
        <h3>Output:</h3>
        <button class="toggle-btn">
          {#if outputExpanded}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="18 15 12 9 6 15"></polyline>
            </svg>
          {:else}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          {/if}
        </button>
      </div>
      
      {#if outputExpanded}
        <div class="section-content">
          {#if isLoading}
            <div class="loading-state">
              <div class="spinner active">
                <svg viewBox="0 0 50 50">
                  <circle cx="25" cy="25" r="20" fill="none" stroke-width="5"></circle>
                </svg>
              </div>
              <p>Crawling in progress... Please wait.</p>
            </div>
          {:else if crawledResults.length > 0}
            <div class="results-summary">
              <p>Successfully crawled {crawledResults.length} URLs.</p>
            </div>
            
            <div class="url-list">
              <ul>
                {#each crawledResults as link}
                  <li>{link}</li>
                {/each}
              </ul>
            </div>
            
            <div class="action-buttons">
              <button class="secondary-btn" on:click={processWithNLP}>Process with NLP</button>
              <button class="secondary-btn" on:click={generateCredentials}>Generate Credentials</button>
            </div>
          {:else}
            <p>No crawl has been performed yet.</p>
          {/if}
        </div>
      {/if}
    </div>
  </div>

  <div class="tools-section">
    <h3>Tools</h3>
    <div class="tools-grid">
      <div class="tool-card" class:active={activeTab === 'sql'} on:click={() => setActiveTab('sql')}>
        <span>SQL Injection</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'credentials'} on:click={() => setActiveTab('credentials')}>
        <span>AI Credentials</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'bruteforce'} on:click={() => setActiveTab('bruteforce')}>
        <span>Bruteforce</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'traffic'} on:click={() => setActiveTab('traffic')}>
        <span>Traffic Interceptor</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'database'} on:click={() => setActiveTab('database')}>
        <span>Database Enumerator</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'repeater'} on:click={() => setActiveTab('repeater')}>
        <span>Repeater</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'fuzzing'} on:click={() => setActiveTab('fuzzing')}>
        <span>Parameter Fuzzing</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'crawler'} on:click={() => setActiveTab('crawler')}>
        <span>Web Crawler</span>
      </div>
      <div class="tool-card" class:active={activeTab === 'intruder'} on:click={() => setActiveTab('intruder')}>
        <span>Intruder</span>
      </div>
    </div>
  </div>
</div>

<style>
  .crawler-container {
    padding: 0 30px 30px;
  }
  
  .crawler-title {
    color: white;
    background-color: #7b69b3;
    padding: 15px 20px;
    margin: 0;
    border-radius: 8px 8px 0 0;
  }
  
  .crawler-content {
    background-color: #7b69b3;
    padding: 0 20px 20px;
    border-radius: 0 0 8px 8px;
    margin-bottom: 20px;
  }
  
  .crawler-section {
    background-color: #c3b6ee;
    border-radius: 8px;
    margin-bottom: 20px;
  }
  
  .section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    cursor: pointer;
  }
  
  .section-header h3 {
    margin: 0;
    color: #333;
  }
  
  .toggle-btn {
    background: none;
    border: none;
    cursor: pointer;
    color: #666;
  }
  
  .section-content {
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .form-group input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    box-sizing: border-box;
  }
  
  .hint {
    display: block;
    font-size: 12px;
    color: #666;
    margin-top: 5px;
  }
  
  .primary-btn, .secondary-btn {
    padding: 8px 15px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
    cursor: pointer;
    margin-right: 10px;
  }
  
  .primary-btn {
    background-color: #5d4b8c;
    color: white;
  }
  
  .primary-btn:disabled {
    background-color: #9E9E9E;
    cursor: not-allowed;
  }
  
  .secondary-btn {
    background-color: #e0e0e0;
    color: #333;
  }
  
  .error-box {
    background-color: #ffebee;
    color: #c62828;
    padding: 10px;
    border-radius: 4px;
    margin-top: 15px;
  }
  
  .loading-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 30px 0;
  }
  
  .loading-state .spinner {
    width: 40px;
    height: 40px;
    margin-bottom: 15px;
  }
  
  .spinner svg {
    width: 100%;
    height: 100%;
  }
  
  .spinner circle {
    stroke: #ccc;
    stroke-dasharray: 150;
    stroke-dashoffset: 150;
    transform-origin: center;
  }
  
  .spinner.active circle {
    animation: rotate 2s linear infinite;
    stroke: #5d4b8c;
  }
  
  @keyframes rotate {
    100% {
      transform: rotate(360deg);
    }
  }
  
  .results-summary {
    background-color: #e8f5e9;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 15px;
  }
  
  .url-list {
    max-height: 200px;
    overflow-y: auto;
    margin-bottom: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    background-color: white;
  }
  
  .url-list ul {
    list-style-type: none;
    padding-left: 0;
    margin: 0;
  }
  
  .url-list li {
    padding: 5px 0;
    border-bottom: 1px solid #f0f0f0;
    word-break: break-all;
  }
  
  .url-list li:last-child {
    border-bottom: none;
  }
  
  .action-buttons {
    display: flex;
    gap: 10px;
    margin-top: 15px;
  }
  
  .tools-section {
    background-color: #c3b6ee;
    border-radius: 8px;
    padding: 20px;
  }
  
  .tools-section h3 {
    margin-top: 0;
    margin-bottom: 15px;
    color: #333;
  }
  
  .tools-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
  }
  
  .tool-card {
    background-color: #b3a4e3;
    padding: 15px;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .tool-card:hover {
    background-color: #9d8ad8;
  }
  
  .tool-card.active {
    background-color: #5d4b8c;
    color: white;
  }
</style>