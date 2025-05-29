import os

EXCLUDED_DIRS = {'.venv', '__pycache__', '.pytest_cache', '.git'}
OUTPUT_FILE = "tree.txt"

def list_dir(base_path, prefix=""):
    lines = []
    entries = sorted(os.listdir(base_path))
    for i, entry in enumerate(entries):
        path = os.path.join(base_path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        if os.path.isdir(path) and entry not in EXCLUDED_DIRS:
            lines.append(f"{prefix}{connector}{entry}/")
            extension = "    " if i == len(entries) - 1 else "│   "
            lines.extend(list_dir(path, prefix + extension))
        elif os.path.isfile(path):
            lines.append(f"{prefix}{connector}{entry}")
    return lines

if __name__ == "__main__":
    root_dir = "."  # Diretório atual
    tree = list_dir(root_dir)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(tree))
    print(f"Árvore salva em {OUTPUT_FILE}")
