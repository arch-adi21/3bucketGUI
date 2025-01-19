// Fetch the current state of the buckets
async function fetchState() {
    const response = await fetch("/get_state");
    const data = await response.json();
    updateBuckets(data);
  }
  
  // Update the buckets' levels visually
  function updateBuckets(state) {
    const levels = [state.x, state.y, state.z];
    const capacities = [8, 5, 3];
  
    // Update water levels and text
    levels.forEach((level, index) => {
      const waterElement = document.getElementById(`water${index + 1}`);
      const textElement = document.getElementById(`level${index + 1}`);
      const heightPercent = (level / capacities[index]) * 100;
  
      // Update the water height and text
      waterElement.style.height = `${heightPercent}%`;
      textElement.textContent = level;
    });
  }
  
  // Pour water from one bucket to another
  async function pour(from, to) {
    const response = await fetch("/pour", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ from, to }),
    });
    const data = await response.json();
  
    if (data.goal) {
      alert("Congratulations! You achieved the goal!");
    }
  
    updateBuckets(data.state);
  }
  
  // Fetch the initial state when the page loads
  document.addEventListener("DOMContentLoaded", fetchState);
  