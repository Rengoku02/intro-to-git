"""
Collaboration Example
=====================
This file is used to practice remote Git workflows.
Try adding your name to the contributors list and
submitting a Pull Request!
"""

# Add your name to this list via a Pull Request
contributors = [
    "Your Name Here",
]


def show_contributors():
    """Display all contributors."""
    print("Contributors to this project:")
    print("-" * 30)
    for name in contributors:
        print(f"  - {name}")
    print(f"\nTotal contributors: {len(contributors)}")


if __name__ == "__main__":
    show_contributors()
