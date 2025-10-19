function simulateRealGPU(units = 1) {
  console.log(`🎮 Simulating ${units} GPU units...`);

  const gpu = new GPU();
  const compute = gpu.createKernel(function (a) {
    return Math.sqrt(a[this.thread.x]);
  }).setOutput([100]);

  for (let i = 0; i < Math.floor(units); i++) {
    const input = Array.from({ length: 100 }, (_, k) => k * i);
    const result = compute(input);
    console.log(`🚀 GPU unit ${i + 1} computed:`, result.slice(0, 5));
  }
}
