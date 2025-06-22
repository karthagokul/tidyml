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

###  Quick Tutorial

This tutorial introduces TidyML through a series of feature-focused examples. Each section includes a `.tml` snippet and a plain explanation. TidyML is a lightweight, human-readable markup language designed to be as readable as YAML, as structured as XML, and as safe and simple as JSON.

#### Basic Data Types
    # TidyML - Basic Data Types
    app {
        name = "TidyML Demo"
        version = 1.2
        active = true
        max_users = 1000
        release_date = "2024-06-22"
        description = null
    }

-   Strings can be quoted or left unquoted if safe.    
-   Numbers are typed automatically as integers or floats.    
-   Booleans must be lowercase: `true` or `false`.    
-   Null is explicitly written as `null`.    
-   No commas or quotes around keys.    
-   Comments start with `#`.
    
#### Nested Objects

    # TidyML - Nested Objects    
    user {
        name = "Alice"
        contact {
            email = "alice@example.com"
            phone = "+31-123456789"
        }
        address {
            street = "Main Street 123"
            city = "Amsterdam"
            zip = "1011AB"
        }
    }
-   Use `{}` blocks to represent nested structures.    
-   Nesting is clear and does not require indentation rules.    
-   Good for representing relationships like JSON or XML.
    

####  Lists

    # TidyML - Lists    
    project {
        name = "OpenRoadSim"
        tags = ["simulation", "python", "automotive"]
        contributors = [
            {
                name = "Gokul"
                role = "creator"
            },
            {
                name = "Jane"
                role = "contributor"
            }
        ]
    }

-   Lists use square brackets `[]`.    
-   Lists can contain scalars or nested objects.    
-   Each item can optionally end with a comma.

#### Comments and Trailing Commas
    # TidyML - Comments and Trailing Commas
    
        settings {
            mode = "production"  # environment mode
            debug = false
            features = [
                "logging",
                "monitoring",
                "alerts",  # trailing comma allowed
            ]
        }

-   Inline and full-line comments are allowed using `#`.    
-   Trailing commas in lists or blocks are accepted.
    
####  Multiline Strings

    # TidyML - Multiline Strings
    
        email_template {
            subject = "Welcome to TidyML"
            body = """
                Hello {{name}},
        
                Thank you for joining the TidyML community.
        
                Regards,
                TidyML Team
            """
        }

-   Use triple quotes `"""` for multiline strings.    
-   Preserves line breaks and indentation.    
-   Useful for emails, documentation, scripts, etc.
    
#### Explicit Typing  

    # TidyML - Explicit Typing (optional concept)
    
    database {
        host = "localhost"
        port: int = 5432
        ssl: bool = true
        timeout: float = 30.5
    }
            
-   Add `: type` hints to enforce specific data types.    
-   Supported types: int, float, bool, string (default).    
-   Typing is optional but useful for validation.


#### Config-Style Real-World Example   

    # TidyML - Real-World Config Structure
    
    server {
        host = "0.0.0.0"
        port = 8080
        log_level = "info"
    }
    
    auth {
        enabled = true
        token_expiry = "2h"
        providers = ["google", "github"]
    }

-   Realistic structure for applications or APIs.    
-   Logical separation of config sections.    
-   Can replace YAML/INI with safer, cleaner format.
    
#### Edge Cases

    # TidyML - Edge Cases
    
    cases {
        empty_string = ""
        quoted_number = "12345"
        special_chars = "@value$%&"
        tricky_key = "value with spaces"
        trailing_list = [
            "one",
            "two",
            "three",
        ]
    }


-   Strings with special characters should be quoted.    
-   Values with spaces must be quoted.    
-   Trailing commas don’t cause parse failures.
    
#### Comparison with Other Formats

    # TidyML - Comparison Examples
    
    example {
        key = "value"
        nested {
            item = 123
        }
        list = ["a", "b", "c"]
        # In YAML this would require proper indentation
        # In JSON this would need quotes and commas
    }

-   TidyML provides the clarity of YAML without indentation sensitivity.    
-   It offers JSON’s simplicity with added readability and comments.    
-   Unlike XML, it avoids verbose tags and boilerplate.
    
### Conclusion
This completes the basic TidyML tutorial covering all major features. You can now use these examples to build real-world configurations or structured data files that are easy to read, write, and maintain.