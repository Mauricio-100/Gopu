import { pipeline } from '@xenova/transformers';

let llm;

export async function initLLM() {
  llm = await pipeline('text2text-generation', 'Xenova/t5-small');
}

export async function queryLLM(input) {
  if (!llm) await initLLM();
  const result = await llm(input);
  return result[0].generated_text;
}
