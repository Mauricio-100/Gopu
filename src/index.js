#!/usr/bin/env node
import { runGPU } from './modules/gpu.js';
import { runCPU } from './modules/cpu.js';
import { runEmulator } from './modules/emulator.js';
import { runVM } from './modules/vm.js';

const mode = process.argv[2] || 'cpu';

switch (mode) {
  case 'gpu': return runGPU();
  case 'cpu': return runCPU();
  case 'emulate': return runEmulator();
  case 'vm': return runVM();
  default: console.log('❌ Mode inconnu. Utilisez cpu | gpu | emulate | vm');
}
