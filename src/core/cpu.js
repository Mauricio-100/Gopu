export function simulateCPU({ threads = 4 }) {
  console.log(`🧠 Simulating ${threads} CPU threads...`);
  for (let i = 0; i < threads; i++) {
    setTimeout(() => {
      console.log(`✅ Thread ${i + 1} completed`);
    }, Math.random() * 1000);
  }
}
