import re

class SnailScriptAI:
    def __init__(self):
        # Full list of SnailScript keyword commands
        self.keyword_commands = [
            r"print",
            r"reint_load<p::\{\}<load_krnl\.exe>",
            r"kernel<load\{\*\}\{\}input::<>loader>",
            r"kernel::Loader\.exe\{\*\*\}",
            r"load::operating_system<load_new::\{\}>function\{\*\}\{<void>\?:load\}",
            r"Type<operating_system::load\?>::function\\load

\[\*\]

"
        ]

    def analyze(self, code):
        errors = []
        lines = code.split("\n")

        for line_number, line in enumerate(lines, start=1):
            stripped = line.strip()

            if stripped == "":
                continue

            # Check if line contains ANY known command
            if not any(re.search(cmd, stripped) for cmd in self.keyword_commands):
                errors.append(f"[Line {line_number}] Unknown or invalid command: '{stripped}'")

            # Check for missing semicolon
            if not stripped.endswith(";") and not stripped.endswith("}"):
                errors.append(f"[Line {line_number}] Missing semicolon")

            # Basic variable declaration check
            if stripped.startswith("var"):
                if "=" not in stripped:
                    errors.append(f"[Line {line_number}] Invalid variable declaration")

            # Object creation syntax check
            if "new" in stripped:
                if "(" not in stripped or ")" not in stripped:
                    errors.append(f"[Line {line_number}] Invalid object creation syntax")

        return errors


# Example usage
if __name__ == "__main__":
    code = """
var system_sandbox = new sandbox();
system_sandbox.load_sandbox();
reint_load<p::{}<load_krnl.exe>;
"""

    ai = SnailScriptAI()
    result = ai.analyze(code)

    if not result:
        print("No errors found. SnailScript is valid.")
    else:
        print("Errors detected:")
        for err in result:
            print(err)
