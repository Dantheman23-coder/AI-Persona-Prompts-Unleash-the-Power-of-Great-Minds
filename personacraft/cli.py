"""Command line interface for PersonaCraft."""

from __future__ import annotations

import argparse

from .prompt import load_personas


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="PersonaCraft CLI")
    parser.add_argument("command", choices=["persona"], help="Command")
    parser.add_argument("--name", required=True, help="Persona name")
    parser.add_argument("--task", default="perform the task", help="Task")
    args = parser.parse_args(argv)

    personas = load_personas()

    if args.command == "persona":
        persona = personas.get(args.name)
        if not persona:
            matches = [p for n, p in personas.items() if args.name.lower() in n.lower()]
            if matches:
                persona = matches[0]
        if not persona:
            raise SystemExit(f"Persona '{args.name}' not found")
        print(persona.render(args.task))


if __name__ == "__main__":
    main()
