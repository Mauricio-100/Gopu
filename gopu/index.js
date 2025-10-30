#!/usr/bin/env node
import { Command } from "commander";
import chalk from "chalk";
import { runStatus } from "./lib/status.js";
import { runInfer } from "./lib/infer.js";
import { runToken } from "./lib/token.js";
import { runDB } from "./lib/db.js";
import { runDeploy } from "./lib/deploy.js";
import { runSSH } from "./lib/ssh.js";
import { runGitHub } from "./lib/github.js";
import { runNetcheck } from "./lib/netcheck.js";
import { runUpload } from "./lib/upload.js";

const program = new Command();

program
  .name("gopu")
  .description("🌀 GopuOS — Agent Terminal")
  .version("1.0.0");

program
  .command("status")
  .description("Infos système")
  .action(runStatus);

program
  .command("infer")
  .argument("<prompt>", "Interroger Gopu")
  .action(runInfer);

program
  .command("token")
  .option("--generate", "Créer un token")
  .option("--verify <token>", "Vérifier un token")
  .action(runToken);

program
  .command("db")
  .option("--test", "Tester la DB")
  .action(runDB);

program
  .command("deploy")
  .description("Déployer sur VPS")
  .action(runDeploy);

program
  .command("ssh")
  .argument("<host>", "Connexion SSH")
  .action(runSSH);

program
  .command("github")
  .argument("<action>", "Commandes GitHub")
  .action(runGitHub);

program
  .command("netcheck")
  .description("Vérifier connectivité PyPI")
  .action(runNetcheck);

program
  .command("upload")
  .description("Publier sur PyPI ou TestPyPI")
  .action(runUpload);

program.parse();
