import { cpus } from 'os';
import { Worker } from 'worker_threads';
import { GPU } from 'gpu.js';

const mode = process.argv[2] || 'cpu';

if (mode === 'cpu') {
  simulateRealCPU(18);
} else if (mode === 'gpu') {
  simulateRealGPU(5.6);
} else {
  console.log('❌ Mode inconnu. Utilisez "cpu" ou "gpu".');
}
