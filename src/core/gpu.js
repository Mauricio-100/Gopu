import { GPU } from 'gpu.js';

export function runGPU() {
  const gpu = new GPU();
  const kernel = gpu.createKernel(function(a) {
    return a[this.thread.x] * 2;
  }).setOutput([100]);

  const input = Array.from({ length: 100 }, (_, i) => i);
  const result = kernel(input);
  console.log('🚀 GPU computed:', result.slice(0, 5));
}
