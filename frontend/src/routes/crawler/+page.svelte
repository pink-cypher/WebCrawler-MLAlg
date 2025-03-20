<script lang="ts">
  let url: string = '';
  let depth: number = 2;
  let crawledResults: string[] = [];
  let error: string = '';

  async function startCrawl() {
    error = '';
    crawledResults = []; // reset
    try {
      const response = await fetch(`http://localhost:8000/crawl?url=${encodeURIComponent(url)}&depth=${depth}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });

      if (!response.ok) {
        throw new Error('Failed to crawl');
      }

      const data = await response.json();
      console.log('Response data:', data); // ✅ Debug
      crawledResults = data.crawled_urls;   // ✅ Make sure it's this
    } catch (err) {
      console.error(err);
      error = (err as Error).message;
    }
  }
</script>

<h1>Web Directory Crawler</h1>

<input type="text" bind:value={url} placeholder="Enter target URL" />
<input type="number" bind:value={depth} min="1" placeholder="Depth" />
<button on:click={startCrawl}>Start Crawl</button>

{#if error}
<p style="color: red;">{error}</p>
{/if}

{#if crawledResults.length > 0}
<h2>Results:</h2>
<ul>
  {#each crawledResults as link}
    <li>{link}</li>
  {/each}
</ul>
{/if}