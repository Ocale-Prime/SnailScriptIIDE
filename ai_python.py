import difflib

# -----------------------------
# VALID SNAILSCRIPT COMMANDS
# -----------------------------
VALID_COMMANDS = [
    "print",
    "reint_load<p::{}<load_krnl.exe>",
    "kernel<load{*}{}input::<>loader>",
    "kernel::Loader.exe{**}"
]

def analyze_snailscript(code: str):
    errors = []
    suggestions = []

    lines = code.split("\n")

    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()

        if line == "":
            continue

        # Check if the line matches a valid command exactly
        if line not in VALID_COMMANDS:
            errors.append(f"Line {line_number}: Unknown command '{line}'")

            # Suggest closest valid command
            close = difflib.get_close_matches(line, VALID_COMMANDS, n=1)
            if close:
                suggestions.append(
                    f"Line {line_number}: Did you mean '{close[0]}'?"
                )
            else:
                suggestions.append(
                    f"Line {line_number}: No similar command found."
                )

    return errors, suggestions


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("Paste your SnailScript code below. End with an empty line.\n")

    user_code = []
    while True:
        line = input()
        if line.strip() == "":
            break
        user_code.append(line)

    code = "\n".join(user_code)

    errors, suggestions = analyze_snailscript(code)

    print("\n--- ERRORS ---")
    print("\n".join(errors) if errors else "No errors found.")

    print("\n--- SUGGESTIONS ---")
    print("\n".join(suggestions) if suggestions else "No suggestions.")
