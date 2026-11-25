"""The Most Shameless Lie — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The lie: I deleted nothing important. (I deleted something important.)
TEXT = "I deleted nothing important."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
