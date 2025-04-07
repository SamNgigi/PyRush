import os
import ast


from dataclasses import dataclass
from typing import List, OrderedDict
from collections import defaultdict

class GamePlay:
    
    @staticmethod
    def get_available_methods(_path: str) -> dict[str, list[dict]]:
        
        methods_by_file = defaultdict(list)

        for root, dirs, files in os.walk(_path):
            for filename in files:
                if filename.endswith(".py"):
                    full_path = os.path.join(root, filename)

                    # Reading file contents
                    with open(full_path, "r", encoding = "utf-8") as f:
                        file_contents = f.read()

                    try:
                        # Parsing with AST
                        tree = ast.parse(file_contents, filename=filename)
                    except SyntaxError:
                        # If the file cannot be parsed (syntax error or otherwise)
                        # we skip it for now. We may log it
                        continue

                    # We can walk the AST, looking for FunctionDef nodes
                    for node in ast.walk(tree):
                        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            
                            class_name = GamePlay.get_enclosing_class_name(node, tree)

                            method_info = {
                                "name": node.name,
                                "lineno": node.lineno,
                                "class": class_name
                            }

                            methods_by_file[full_path].append(method_info)

        return methods_by_file

    @staticmethod
    def get_enclosing_class_name(func_node: ast.AST, tree:ast.AST) -> str:

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for subnode in node.body:
                    if subnode is func_node:
                        return node.name
                    # If subnode is also a compound (nexted classes, etc) we can go deeper
        return ""

if __name__ == "__main__":

    # Getting this file current directory
    this_dir = os.path.dirname(os.path.abspath(__file__))
    ds_algo_path = os.path.join(this_dir, "..", "data_structures_algorithms")

    methods_dict = GamePlay.get_available_methods(ds_algo_path)

    for filepath, methods in methods_dict.items():
        print(f"File: {filepath}")
        for method_info in methods:
            class_prefix = f"{method_info['class']}." if method_info['class'] else ""
            print(f"    - {class_prefix}{method_info['name']} (line {method_info['lineno']})")
