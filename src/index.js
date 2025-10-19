import { detectGopuOS, debugGopuOS } from './os.js';
import { runGPU } from './modules/gpu.js';
import { runCPU } from './modules/cpu.js';
import { runEmulator } from './modules/emulator.js';
import { runVM } from './modules/vm.js';
import chalk from 'chalk';

const args = process.argv.slice(2);
const command = args[0];

if (command === '--help') {
  console.log(chalk.blue.bold('\n🧠 GopuOS — Commandes disponibles'));
  console.log(`
  --help        Affiche cette liste
  --debug       Affiche les infos système
  --version     Affiche la version
  cpu           Simulation CPU
  gpu           Simulation GPU
  emulate       Émulation RISC-V/QEMU
  vm            Machine virtuelle JS
  --strict      Mode Linux natif uniquement
  --lang [xx]   Affichage multilingue
  `);
  process.exit(0);
}

if (command === '--debug') {
  debugGopuOS();
  process.exit(0);
}

if (command === '--version') {
  console.log(chalk.magenta.bold('🧬 GopuOS v1.0.0'));
  process.exit(0);
}

detectGopuOS(); // bloque si non-Linux

switch (command) {
  case 'gpu': return runGPU();
  case 'cpu': return runCPU();
  case 'emulate': return runEmulator();
  case 'vm': return runVM();
  default:
    console.log(chalk.red.bold(`❌ Commande inconnue: ${command}`));
    console.log(chalk.gray(`Utilisez --help pour voir les commandes disponibles.`));
    process.exit(1);
}
