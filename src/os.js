import os from 'os';
import fs from 'fs';
import chalk from 'chalk';

export function detectGopuOS() {
  const platform = os.platform(); // 'linux', 'darwin', 'win32', etc.
  const userId = `user_id:${process.getuid?.() || 1000}`;
  const hostname = os.hostname();
  const distroInfo = getLinuxDistro();

  if (platform !== 'linux') {
    console.log(chalk.red.bold(`❌ GopuOS is Linux-only. Detected: ${platform}`));
    process.exit(1);
  }

  console.log(chalk.green.bold(`✅ GopuOS booted on ${hostname}`));
  console.log(chalk.cyan(`🔍 ${userId}:${platform}_${hostname.slice(0, 6)}`));
  console.log(chalk.yellow(`🧬 Distro: ${distroInfo}`));
}

function getLinuxDistro() {
  try {
    const release = fs.readFileSync('/etc/os-release', 'utf8');
    const nameLine = release.split('\n').find(line => line.startsWith('PRETTY_NAME='));
    return nameLine?.split('=')[1]?.replace(/"/g, '') || 'Unknown Linux';
  } catch {
    return 'Unknown Linux';
  }
}
