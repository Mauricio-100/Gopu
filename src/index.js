#!/usr/bin/env node
import { simulateCPU } from './core/cpu.js';
import { simulateGPU } from './core/gpu.js';
import { logStart } from './utils/logger.js';

const args = process.argv.slice(2);
const mode = args[0] || 'cpu';

logStart(mode);

if (mode === 'gpu') {
  simulateGPU({ units: 5.6 });
} else {
  simulateCPU({ threads: 18.1 });
}
