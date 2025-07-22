#!/usr/bin/env python3
"""
CLI to run Snapshot games from prompt-playbook.

Usage:
  python scripts/play_snapshot.py --variant blank \
      --language "SQL" --features "JOINs, GROUP BY"
"""
import argparse, os, sys, textwrap, re
from pathlib import Path
from dotenv import load_dotenv
import openai


def load_prompt(variant: str, language: str, features: str) -> str:
    root = Path(__file__).resolve().parents[1]
    md_path = root / "patterns" / "snapshot_games.md"
    template = md_path.read_text()

    # Match the prompt skeleton block for the given variant
    variant_title = f"Snapshot ({variant.capitalize()})"
    pattern = re.compile(
        rf"##\s*\d+\. {re.escape(variant_title)}.*?```text(.*?)```",
        re.DOTALL
    )
    match = pattern.search(template)
    if not match:
        sys.exit(f"❌ Could not find skeleton for variant '{variant}'.")

    prompt_block = match.group(1).strip()

    return (
        prompt_block.replace("[language, packages]", language)
                    .replace("[features]", features)
    )


def main():
    root = Path(__file__).resolve().parents[1]
    load_dotenv(dotenv_path=root / ".env")

    # -------- provider switch --------
    provider = os.getenv("PROVIDER", "openai")  # default = openai
    if provider.lower() == "groq":
        openai.api_key  = os.getenv("GROQ_API_KEY")
        openai.base_url = os.getenv("GROQ_API_BASE", "https://api.groq.com/openai/v1")
        model_name      = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")
    else:
        openai.api_key  = os.getenv("OPENAI_API_KEY")
        openai.base_url = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
        model_name      = os.getenv("MODEL", "gpt-4o-mini")
    # ---------------------------------

    ap = argparse.ArgumentParser()
    ap.add_argument("--variant",  default="original", choices=["original", "blank", "bug"])
    ap.add_argument("--language", default="Python")
    ap.add_argument("--features", default="list comprehensions")
    ap.add_argument("--provider", default=provider, choices=["openai", "groq"])
    args = ap.parse_args()

    # allow CLI override
    if args.provider == "groq":
        openai.api_key  = os.getenv("GROQ_API_KEY")
        openai.base_url = os.getenv("GROQ_API_BASE", "https://api.groq.com/openai/v1")
        model_name      = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")

    prompt = load_prompt(args.variant, args.language, args.features)

    try:
        resp = openai.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        print("\n--- LLM OUTPUT ---\n")
        print(textwrap.fill(resp.choices[0].message.content, width=88))
    
    except openai.RateLimitError:
        sys.exit("❌ Quota exceeded—check billing or key validity.")


if __name__ == "__main__":
    main()