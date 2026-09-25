#!/usr/bin/env python3
"""
Simple Hello World Python Script
Demonstrates basic Python hello-world functionality
"""

def greet(name="World"):
    """Print a greeting message"""
    return f"Hello, {name}!"

def main():
    """Main function"""
    print(greet())
    print(greet("Vellai"))
    
    # Additional hello world variations
    languages = {
        "Python": "Hello, World!",
        "JavaScript": "console.log(Hello, World!)",
        "Java": "System.out.println(\"Hello, World!\");",
        "C": "printf(\"Hello, World!\\n\");",
        "Go": "fmt.Println(\"Hello, World!\")"
    }
    
    print("\nHello World in different languages:")
    for lang, code in languages.items():
        print(f"{lang}: {code}")

if __name__ == "__main__":
    main()
