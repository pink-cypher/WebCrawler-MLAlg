<script lang="ts">
  import { onMount } from 'svelte';

  let url = '';
  let depth = 2;
  let crawledResults = [];
  let isLoading = false;
  let error = '';
  let activeTab = 'crawler';
  let setupExpanded = true;
  let outputExpanded = true;
  let crawlStatus = 'idle'; // idle, running, completed
  let executedTools = [
    { name: 'Web Crawler', status: 'in progress' },
    { name: 'Database Enumerator', status: 'launched' },
    { name: 'Traffic Interceptor', status: 'launched' }
  ];

  const API_URL = 'http://localhost:8000';

  async function startCrawl() {
    if (!url) {
      error = 'Please enter a URL';
      return;
    }

    error = '';
    crawledResults = [];
    isLoading = true;
    crawlStatus = 'running';
    
    try {
      const response = await fetch(`${API_URL}/crawl?url=${encodeURIComponent(url)}&depth=${depth}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });

      if (!response.ok) {
        throw new Error(`Failed to crawl: ${response.statusText}`);
      }

      const data = await response.json();
      crawledResults = data.crawled_urls;
      crawlStatus = 'completed';
    } catch (err) {
      console.error(err);
      error = err.message;
      crawlStatus = 'idle';
    } finally {
      isLoading = false;
    }
  }

  async function cleanData() {
    isLoading = true;
    
    try {
      const response = await fetch(`${API_URL}/nlp/clean`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });

      if (!response.ok) {
        throw new Error(`Failed to clean data: ${response.statusText}`);
      }

      await response.json();
    } catch (err) {
      console.error(err);
      error = err.message;
    } finally {
      isLoading = false;
    }
  }

  async function generateCredentials() {
    isLoading = true;
    
    try {
      const response = await fetch(`${API_URL}/ml/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });

      if (!response.ok) {
        throw new Error(`Failed to generate credentials: ${response.statusText}`);
      }

      await response.json();
    } catch (err) {
      console.error(err);
      error = err.message;
    } finally {
      isLoading = false;
    }
  }

  function setActiveTab(tab) {
    activeTab = tab;
  }
</script>

<div class="app-container">
  <div class="sidebar">
    <div class="logo-container">
      <div class="logo">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        </svg>
      </div>
      <span>FortiTRACE</span>
    </div>

    <div class="menu-section">
      <div class="menu-title">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
          <line x1="9" y1="3" x2="9" y2="21"></line>
        </svg>
        <span>Main Menu</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </div>
    </div>

    <div class="menu-section expanded">
      <div class="menu-title">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
        </svg>
        <span>FortiTRACE</span>
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="18 15 12 9 6 15"></polyline>
        </svg>
      </div>
      <ul class="menu-items">
        <li class="active">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
          </svg>
          <span>Projects</span>
        </li>
      </ul>
    </div>

    <div class="progress-section">
      <h3>Progress:</h3>
      <div class="progress-item">
        <span>Web Crawler</span>
        <div class="spinner" class:active={crawlStatus === 'running'}>
          <svg viewBox="0 0 50 50">
            <circle cx="25" cy="25" r="20" fill="none" stroke-width="5"></circle>
          </svg>
        </div>
      </div>
    </div>

    <div class="executed-tools-section">
      <h3>Tools Executed:</h3>
      {#each executedTools as tool}
        <div class="tool-status">
          <span>{tool.name}</span>
          <div class="status-badge {tool.status.replace(' ', '-')}">{tool.status}</div>
        </div>
      {/each}
    </div>

    <div class="exit-button">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
        <polyline points="16 17 21 12 16 7"></polyline>
        <line x1="21" y1="12" x2="9" y2="12"></line>
      </svg>
      <span>Exit FortiTRACE</span>
    </div>
  </div>

  <div class="main-content">
    <div class="header">
      <div class="breadcrumb">
        <span>FortiTRACE/Projects/Tools</span>
      </div>

      <div class="user-actions">
        <div class="notification-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
        </div>
        <div class="help-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
            <line x1="12" y1="17" x2="12.01" y2="17"></line>
          </svg>
        </div>
        <div class="avatar">
          <img src="https://via.placeholder.com/35" alt="User avatar" />
        </div>
      </div>
    </div>

    <div class="page-title">
      <h1>FortiTrace/Projects/Tools/Web Crawler</h1>
      <button class="main-menu-btn">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        Main Menu
      </button>
    </div>

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
              {#if crawlStatus === 'running'}
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
                  <button class="secondary-btn" on:click={cleanData}>Process with NLP</button>
                  <button class="secondary-btn" on:click={generateCredentials}>Generate Credentials</button>
                </div>
              {:else if crawlStatus === 'completed'}
                <p>No URLs were found during the crawl.</p>
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
  </div>
</div>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
  }
  
  .app-container {
    display: flex;
    min-height: 100vh;
  }
  
  .sidebar {
    width: 220px;
    background-color: white;
    box-shadow: 2px 0 5px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    padding: 20px 0;
  }
  
  .logo-container {
    display: flex;
    align-items: center;
    padding: 0 20px;
    margin-bottom: 20px;
  }
  
  .logo {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 10px;
    color: #5d4b8c;
  }
  
  .menu-section {
    margin-bottom: 15px;
  }
  
  .menu-title {
    display: flex;
    align-items: center;
    padding: 10px 20px;
    cursor: pointer;
    font-weight: bold;
  }
  
  .menu-title svg {
    margin-right: 10px;
  }
  
  .menu-title svg:last-child {
    margin-left: auto;
    margin-right: 0;
  }
  
  .menu-items {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  .menu-items li {
    display: flex;
    align-items: center;
    padding: 8px 20px 8px 40px;
    cursor: pointer;
  }
  
  .menu-items li.active {
    background-color: #f0f0f0;
  }
  
  .menu-items li svg {
    margin-right: 10px;
  }
  
  .progress-section, .executed-tools-section {
    padding: 0 20px;
    margin-top: 20px;
  }
  
  .progress-section h3, .executed-tools-section h3 {
    color: #666;
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  .progress-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .spinner {
    width: 24px;
    height: 24px;
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
  
  .tool-status {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .status-badge {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 12px;
    text-transform: capitalize;
  }
  
  .status-badge.in-progress {
    background-color: #e0e7ff;
    color: #4f46e5;
  }
  
  .status-badge.launched {
    background-color: #e0f2fe;
    color: #0ea5e9;
  }
  
  .status-badge.completed {
    background-color: #dcfce7;
    color: #16a34a;
  }
  
  .exit-button {
    margin-top: auto;
    display: flex;
    align-items: center;
    padding: 10px 20px;
    cursor: pointer;
    color: #666;
  }
  
  .exit-button svg {
    margin-right: 10px;
  }
  
  .main-content {
    flex: 1;
    padding: 0;
    background-color: #f8f8fb;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background-color: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }
  
  .breadcrumb {
    color: #5d4b8c;
    font-weight: 500;
  }
  
  .user-actions {
    display: flex;
    align-items: center;
  }
  
  .notification-icon, .help-icon {
    margin-right: 20px;
    cursor: pointer;
  }
  
  .avatar {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    overflow: hidden;
  }
  
  .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .page-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 30px;
  }
  
  .page-title h1 {
    font-size: 20px;
    color: #333;
    margin: 0;
  }
  
  .main-menu-btn {
    display: flex;
    align-items: center;
    padding: 8px 12px;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .main-menu-btn svg {
    margin-right: 8px;
  }
  
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