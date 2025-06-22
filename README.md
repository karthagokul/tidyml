## Why Another Markup Language?

Despite the popularity of JSON, YAML, and XML, developers and teams often run into problems when using these formats for configuration or structured data. TidyML is designed to address the most common frustrations with a clear, lightweight, and safe syntax that balances human readability with machine usability.

### JSON: Machine-friendly, but not human-friendly

- No support for comments — making it hard to document or disable sections.
- Requires strict syntax (quotes, commas, braces).
- Trailing commas are disallowed, making edits error-prone.
- Multiline strings and advanced types (e.g., dates) are awkward.
- Any small mistake (like a missing comma) causes hard parse errors.

### YAML: Readable, but fragile and inconsistent

- Sensitive to indentation — a misplaced space can break everything.
- Implicit type conversion can lead to unexpected behavior (`no` becomes `false`, `ON` becomes `true`, etc.).
- Security concerns — past parsers could execute code on load.
- Difficult to validate consistently across implementations.
- Merge conflicts and debugging are hard due to whitespace sensitivity.

### XML: Structured, but verbose and outdated for config

- Verbose syntax with opening/closing tags clutters simple data.
- Hard to edit manually — every value is wrapped in multiple layers.
- Prone to strict errors if a single tag or quote is missing.
- Originally meant for document markup, not config files.
- Tooling and schemas can be complex and overkill for basic needs.

## How TidyML Solves These Problems

TidyML is a new markup language designed to be:

- **Readable**: Clean block-based syntax that is easy to scan and edit.
- **Safe**: No implicit type guessing, no code execution risks.
- **Lightweight**: Minimal syntax, no angle brackets or excessive nesting.
- **Comment-friendly**: Supports `#` comments anywhere in the file.
- **Trailing comma-tolerant**: Easier edits with fewer syntax errors.
- **Easy to parse and diff**: Clear structure that avoids indentation pitfalls.
- **Built for configs**: Designed specifically for configuration, not general-purpose document markup.

## When to Use TidyML

- Writing configuration files for applications, CI/CD, IoT, or simulations.
- Replacing fragile YAML or rigid JSON with something more developer-friendly.
- Sharing structured data with both humans and machines.
- Embedding human-readable settings that won’t break on a missing comma or indentation.


TidyML is in early development, but aims to become a practical alternative for everyday config and structured data tasks — simple, tidy, and safe by default.


## TidyML Syntax

TidyML uses a minimalistic syntax that's easy to understand.

    # A sample user record
    
    user {
        name = "Alice"
        age = 30
        active = true
        roles = ["admin", "editor"]
    
        address {
            city = "Amsterdam"
            zip = "1011AB"
        }
    }
