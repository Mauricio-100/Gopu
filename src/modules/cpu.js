import Parallel from 'paralleljs';

export function runCPU() {
  const data = Array.from({ length: 1e5 }, (_, i) => i);
  const p = new Parallel(data);

  p.map(n => Math.sqrt(n)).then(result => {
    console.log('🧠 CPU parallel result:', result.slice(0, 5));
  });
}
