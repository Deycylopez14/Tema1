import tkinter as tk
from tkinter import ttk
import re

class LexicalAnalyzer:
    def __init__(self):
        self.keywords = ['while', 'do', 'for']
        self.types = ['int', 'float']
        self.symbols = ['[', ']', '(', ')', '{', '}', ',', ';']
        self.patterns = [
            (r'\b(while|do|for)\b', 'Palabra reservada'),
            (r'\b(int|float)\b', 'Tipo de dato'),
            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'Identificador'),
            (r'\[', 'Corchete de apertura'),
            (r'\]', 'Corchete de cierre'),
            (r'\(', 'Parentesis de apertura'),
            (r'\)', 'Parentesis de cierre'),
            (r'\{', 'Llave de apertura'),
            (r'\}', 'Llave de cierre'),
            (r'\;', 'Punto y coma'),
            (r'\+\+', 'Operador de incremento')
        ]

    def analyze(self, code):
        lines = code.split('\n')
        tokens = []
        for i, line in enumerate(lines, start=1):
            for pattern, token_type in self.patterns:
                matches = re.findall(pattern, line)
                for match in matches:
                    tokens.append((i, match, token_type))
        tokens.sort(key=lambda x: x[0])  # Ordena los tokens por el número de línea
        return tokens

analyzer = LexicalAnalyzer()

def analyze_code():
    code = code_text.get("1.0", tk.END)
    tokens = analyzer.analyze(code)
    result_tree.delete(*result_tree.get_children())
    for token in tokens:
        result_tree.insert("", "end", values=token)

def clear_code():
    code_text.delete("1.0", tk.END)
    result_tree.delete(*result_tree.get_children())

root = tk.Tk()
root.title("Analizador Léxico")
root.geometry("800x600")  # Ajusta el tamaño de la ventana principal

code_label = ttk.Label(root, text="Código:")
code_label.pack()

code_text = tk.Text(root, height=10, width=40)
code_text.pack()

analyze_button = ttk.Button(root, text="Analizar", command=analyze_code)
analyze_button.pack()

clear_button = ttk.Button(root, text="Limpiar", command=clear_code)
clear_button.pack()

result_tree = ttk.Treeview(root, columns=("Linea", "Token", "Tipo"), show="headings")
result_tree.heading("Linea", text="Linea")
result_tree.heading("Token", text="Token")
result_tree.heading("Tipo", text="Tipo")

# Ajusta el ancho de las columnas
result_tree.column("Linea", width=50)
result_tree.column("Token", width=250)
result_tree.column("Tipo", width=250)

result_tree.pack()

root.mainloop()