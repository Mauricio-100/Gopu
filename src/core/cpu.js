function simulateRealCPU(threadCount = 4) {
  console.log(`🧠 Spawning ${threadCount} CPU threads...`);

  for (let i = 0; i < threadCount; i++) {
    const worker = new Worker(`
      const { parentPort } = require('worker_threads');
      let result = 0;
      for (let j = 0; j < 1e7; j++) result += Math.sqrt(j);
      parentPort.postMessage(result);
    `, { eval: true });

    worker.on('message', msg => {
      console.log(`✅ Thread ${i + 1} done: ${msg.toFixed(2)}`);
    });
  }
}
