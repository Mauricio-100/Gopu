export function simulateGPU({ units = 1 }) {
  console.log(`🎮 Simulating ${units} GPU units...`);
  for (let i = 0; i < Math.floor(units); i++) {
    setTimeout(() => {
      console.log(`🚀 GPU unit ${i + 1} rendered`);
    }, Math.random() * 1500);
  }
}
