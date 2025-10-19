import riscv from 'riscv-js';

export function runEmulator() {
  const cpu = new riscv.CPU();
  cpu.loadProgram([0x13, 0x00, 0x00, 0x00]); // NOP
  cpu.step();
  console.log('🧬 RISC-V PC:', cpu.pc);
}
