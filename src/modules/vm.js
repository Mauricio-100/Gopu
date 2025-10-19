import { VM } from 'vm2';

export function runVM() {
  const vm = new VM();
  const result = vm.run(`(() => '🧪 VM2 sandboxed code')()`);
  console.log('🧱 VM2 result:', result);
}
