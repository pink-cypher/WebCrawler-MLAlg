<script>
  import { goto } from '$app/navigation';

  let tools = [
    { name: "Web Crawler", progress: 0, status: "Ready to Go!" },
    { name: "ML Generator", progress: 0, status: "Ready to Go!" },
    { name: "Parameter Fuzzing", progress: 0, status: "Ready to Go!" },
    { name: "Brute Force Tester", progress: 0, status: "Ready to Go!" },
    { name: "SQL Injection", progress: 0, status: "Ready to Go!" },
    { name: "HTTP Tester", progress: 0, status: "Ready to Go!" }
  ];

  /**
   * @param {{ name: any; progress: any; status?: string; }} tool
   */
    function handleAction(tool) {
    // Only act if progress is 0 ("Set Up" button)
    if (tool.progress === 0) {
      if (tool.name === "Web Crawler") {
        goto('/crawler');
      } else if (tool.name === "ML Generator") {
        goto('/ml');
      } else {
        alert("This tool is not ready yet.");
      }
    } else {
      // If progress is non-zero, you could display the tool's dashboard or details.
    }
  }
</script>
  
  <div class="container">
    <div class="sidebar">
        <div class="logo">
          <!-- svelte-ignore a11y_consider_explicit_label -->
          <a href="/" class="logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="#55B7B9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M2 17L12 22L22 17" stroke="#55B7B9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M2 12L12 17L22 12" stroke="#55B7B9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
        </div>
    
        <div class="sidebar-icons">
          <div class="sidebar-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="12" cy="12" r="3" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="sidebar-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <polyline points="14 2 14 8 20 8" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <line x1="16" y1="13" x2="8" y2="13" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <line x1="16" y1="17" x2="8" y2="17" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <polyline points="10 9 9 9 8 9" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="sidebar-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="12" cy="12" r="10" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <polyline points="12 6 12 12 16 14" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>
    
        <div class="settings-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="3" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" stroke="#718096" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
    </div>
  
  <!-- Main Content -->
  <main class="main-content">
    <header class="crawler-header">
      <h1>Tool Dashboard</h1>
      <p class="subheader">Select a tool from the menu below.</p>
    </header>
    
    {#each tools as tool}
      <div class="tool-item">
        <span>{tool.name}</span><br>
        <div class="progress-bar">
          <div class="progress-fill" style="width: {tool.progress}%;"></div>
        </div>
        <span class="status">{tool.status}</span>
        <button class="info-btn">Info</button>
        <button class="action-btn" on:click={() => handleAction(tool)}>
          {tool.progress === 0 ? 'Set Up' : 'View'}
        </button>
      </div>
    {/each}
  </main>
  </div>

  
  <style>
    /* Base styles */
    :global(body) {
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: #f5f7fa;
      color: #2d3748;
      line-height: 1.5;
    }
  
    .container {
      display: flex;
      min-height: 100vh;
    }
  
    /* Sidebar styles */
    .sidebar {
      width: 60px;
      background-color: #f5f7fa;
      border-right: 1px solid #e2e8f0;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 20px;
    }
  
    .logo {
      margin-bottom: 20px;
    }
  
    .sidebar-icons {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }
  
    .sidebar-icon {
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      cursor: pointer;
    }
  
    .sidebar-icon:hover {
      background-color: #e2e8f0;
    }
  
    .settings-icon {
      margin-top: auto;
      margin-bottom: 20px;
      cursor: pointer;
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
    }
  
    .settings-icon:hover {
      background-color: #e2e8f0;
    }
  
    /* Main content styles */
    .main-content {
      flex: 1;
      padding: 30px;
      max-width: 1200px;
      margin: 0 auto;
    }
  
    .crawler-header {
      margin-bottom: 30px;
      position: relative;
    }
  
    .crawler-header h1 {
      font-size: 24px;
      margin: 0;
      margin-bottom: 5px;
    }
  
    .subheader {
      font-size: 16px;
      color: #718096;
    }
  
    /* Progress indicator */
    .progress-indicator {
      display: flex;
      align-items: center;
      margin-top: 20px;
      max-width: 600px;
    }
  
    .progress-step {
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }
  
    .step-circle {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background-color: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: bold;
      margin-bottom: 8px;
    }
  
    .progress-step.active .step-circle {
      background-color: #48BB78;
      color: white;
    }
  
    .progress-step.completed .step-circle {
      background-color: #38A169;
      color: white;
    }
  
    .progress-step span {
      font-size: 12px;
      color: #718096;
    }
  
    .progress-line {
      flex: 1;
      height: 2px;
      background-color: #e2e8f0;
      margin: 0 10px;
      margin-bottom: 30px;
    }
  
    .progress-line.completed {
      background-color: #38A169;
    }
  
    /* Form styles */
    .crawler-configuration {
      background-color: white;
      border-radius: 8px;
      padding: 30px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
  
    .form-group {
      margin-bottom: 20px;
    }
  
    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-size: 14px;
      color: #4A5568;
    }
  
    .required {
      color: #E53E3E;
    }
  
    .form-group input {
      width: 100%;
      padding: 10px;
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      font-size: 16px;
      box-sizing: border-box;
    }
  
    .form-group input:focus {
      outline: none;
      border-color: #4299e1;
      box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.15);
    }
  
    .btn {
      padding: 10px 15px;
      border-radius: 4px;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      border: none;
      transition: background-color 0.2s;
    }
  
    .start-btn {
      background-color: #4299e1;
      color: white;
    }
  
    .start-btn:hover {
      background-color: #3182ce;
    }
  
    .secondary-btn {
      background-color: #e2e8f0;
      color: #4A5568;
    }
  
    .secondary-btn:hover {
      background-color: #cbd5e0;
    }
  
    .error-message {
      color: #E53E3E;
      margin-top: 15px;
      font-size: 14px;
    }
  
    /* Running and Results styles */
    .crawler-running, .crawler-results {
      background-color: white;
      border-radius: 8px;
      padding: 30px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
  
    .scan-progress {
      margin-bottom: 30px;
    }
  
    .scan-progress-icon {
      display: inline-block;
      margin-right: 10px;
    }
  
    .scan-circle {
      width: 15px;
      height: 15px;
      border-radius: 50%;
      background-color: #48BB78;
      position: relative;
    }
  
    .scan-circle::after {
      content: '';
      position: absolute;
      top: -3px;
      left: -3px;
      right: -3px;
      bottom: -3px;
      border: 2px solid #48BB78;
      border-radius: 50%;
      opacity: 0.4;
    }
  
    .scan-progress-text {
      display: inline-block;
      font-weight: 600;
      margin-bottom: 10px;
    }
  
    .scanning-text {
      color: #718096;
      font-weight: normal;
    }
  
    .scan-progress-bar {
      height: 6px;
      background-color: #e2e8f0;
      border-radius: 3px;
      overflow: hidden;
    }
  
    .scan-progress-fill {
      height: 100%;
      background-color: #48BB78;
      border-radius: 3px;
      transition: width 0.3s ease;
    }
  
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 30px;
    }
  
    .metric-box {
      background-color: #f7fafc;
      padding: 15px;
      border-radius: 4px;
    }
  
    .metric-label {
      font-size: 14px;
      color: #718096;
      margin-bottom: 5px;
    }
  
    .metric-value {
      font-size: 18px;
      font-weight: 600;
    }
  
    .results-table {
      margin-bottom: 30px;
      overflow-x: auto;
    }
  
    table {
      width: 100%;
      border-collapse: collapse;
    }
  
    th, td {
      padding: 12px 15px;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
    }
  
    thead tr {
      background-color: #f7fafc;
    }
  
    th {
      font-weight: 600;
      color: #4A5568;
    }
  
    tbody tr:nth-child(even) {
      background-color: #f7fafc;
    }
  
    .url-cell {
      max-width: 300px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
  
    .action-buttons {
      display: flex;
      gap: 10px;
    }
  
    .spacer {
      flex: 1;
    }
  
    .terminal-btn {
      background-color: #edf2f7;
    }
  
    .export-icon {
      margin-left: 8px;
      vertical-align: middle;
    }
    .main-content {
      flex: 1;
      padding: 30px;
    }
    .tool-item {
      display: flex;
      align-items: center;
      gap: 15px;
      margin-bottom: 15px;
      padding: 10px;
      background: white;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .progress-bar {
      flex: 1;
      height: 6px;
      background: #e2e8f0;
      border-radius: 3px;
    }
    .progress-fill {
      height: 100%;
      background: #48BB78;
      border-radius: 3px;
    }
    .info-btn, .action-btn {
      padding: 5px 10px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .info-btn {
      background: #e2e8f0;
    }
    .action-btn {
      background: #4299e1;
      color: white;
    }
  </style>