function fetchData() {
    fetch('output.json')
      .then(response => response.json())
      .then(data => displayData(data))
      .catch(error => console.error(error));
  }
  
  function displayData(data) {
    const container = document.getElementById('data-container');
  
    // Create a heading
    const heading = document.createElement('h1');
    heading.textContent = 'Web Scraping Data';
    container.appendChild(heading);
  
    // Loop through the paragraphs and create <p> elements
    for (const paragraph of data.paragraphs) {
      const p = document.createElement('p');
      p.textContent = paragraph;
      container.appendChild(p);
    }
  }
  
  document.addEventListener('DOMContentLoaded', fetchData);
  