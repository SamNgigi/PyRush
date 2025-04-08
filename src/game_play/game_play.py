import os
import ast


from dataclasses import dataclass
from typing import List, OrderedDict, Union
from collections import defaultdict

class GamePlay:

    @staticmethod
    def init_game()->None:
        """
        Encapsulates game logic and runs the game
        """

        print("Hello World")
        print("Type q to quit")

        while True:
            name:str = input("What's your name: ")
            if name == "q":
                break

            print(f"Hi {name}")
    
    @staticmethod
    def get_available_methods(_path: str) -> dict[str, list[dict]]:
        """
        Recursively walks through the path provided looking for .py files.
        Parses each file into an AST and extracts all function definitions
        including class methods

        Returns a dict of the form
            {
                full_file_path: [
                    {
                        "name": function_name,
                        "lineno": line_number,
                        "class": parent_class_name or None,
                        "":
                    },
                    ...
                ]
            }
        """
        methods_by_file = defaultdict(list)

        for root, _, files in os.walk(_path):
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

                    # Gathering only module-level and class-level function definitions
                    # We do a custome alk and pass the parent type
                    method_nodes = GamePlay.gather_functions(tree)

                    # Adding them to our structure
                    for method in method_nodes:
                        methods_by_file[full_path].append(method)

        return methods_by_file


    @staticmethod
    def gather_functions(
        tree_node: ast.AST,
        parent_is_class: bool = False,
        parent_is_function: bool = False,
        current_class: Union[str, None] = None
    ) -> list:
        
        results = []

        # If this node is a class, any functions in its body will be considere "class methods"
        if isinstance(tree_node, ast.ClassDef):
            current_class = tree_node.name
            parent_is_class = True
            parent_is_function = False # you can't be a function if you're in a class
        
        elif isinstance(tree_node, ast.FunctionDef):
            # Only keep this function if parent is module or class
            if not parent_is_function:
                function_info = {
                    "name": tree_node.name,
                    "class": current_class ,
                    "lineno": tree_node.lineno,
                }
                results.append(function_info)
            # Updateing the state so that children of this function are considered nested
            parent_is_function = True

        # Recurse into child nodes
        for child in ast.iter_child_nodes(tree_node):

            results.extend(
                GamePlay.gather_functions(
                    child,
                    parent_is_class = parent_is_class,
                    parent_is_function = parent_is_function,
                    current_class = current_class
                )
            )

        return results

    @staticmethod
    def get_enclosing_class_name(func_node: ast.AST, tree:ast.AST) -> Union[str, None]:
        """
        Given a function node and the full AST, tries to find the immediate class that
        enclosed this function, if any. Returns Noe if not enclosed by a class.
        """
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                for subnode in node.body:
                    if subnode is func_node:
                        return node.name
                    # If subnode is also a compound (nexted classes, etc) we can go deeper
        return None


    @staticmethod
    def build_menu(methods_by_file: dict)->dict:
        """
        Build a nested structure suitable for display our game menu
        
        Returns dict of the form

        {
            "FolderName":{
                "ShortFileName": [
                    {"selector": "1.01", "display_name": "Search.binary_search_iterative"},
                    ...
                ]
            },
            ...
        }

        """
        menu = defaultdict(lambda: defaultdict(list))

        # Counter to keep track of global file index
        file_counter: int = 1

        # Sort the files to have consistent output
        sorted_files = sorted(methods_by_file.keys())

        for file_path in sorted_files:
            folder_name = GamePlay.get_top_folder(file_path)
            short_file_name = os.path.splitext(os.path.basename(file_path))[0]

            # Sorting methods for consistency
            method_list = sorted(methods_by_file[file_path], key=lambda method: method['lineno'])

            # Numbering them with the form "1.01","1.02"
            method_counter: int = 1

            for method in method_list:
                method_name = f"{method['class']}.{method['name']}" if method['class'] else method['name']

                # Formatting "method_counter" as 01, 02 etc
                method_suffix = f"{method_counter:02d}" #zero-padded to 2 digits

                selector = f"{file_counter}.{method_suffix}"

                selector_info = {"selector": selector, "display_name": method_name }

                menu[folder_name][short_file_name].append(selector_info)

                method_counter += 1

            file_counter += 1


        return menu

    @staticmethod
    def get_top_folder(file_path: str) -> str:

        # Noramlize path
        path_parts = os.path.normpath(file_path).split(os.sep)

        # We find 'src' folder and take the next part as top_folder
        try:
            idx = path_parts.index("src")
            if idx + 1 < len(path_parts):
                return path_parts[idx + 1].replace("_", " ").title()
        except ValueError:
            pass

        # Fallback if we cannot find 'src' or out of range
        return "Unknown"

    @staticmethod
    def display_menu(menu: dict) -> None:
        """
        Display the method
        """
        print("PyRush Practice Menu")
        # For each top-level folder
        for folder_name, file_dict in menu.items():
            print(folder_name)
            print(f"{'File':<25}Method") # Performance wise print("File" + " " * 20 + Menu) is considered faster
            print("-"*40)

            for short_filename, methods in file_dict.items():
                print(short_filename.title())
                for method in methods:
                    print(f"    {method['selector']:6}      {method['display_name']}")
            print()





    

if __name__ == "__main__":

    # Getting this file current directory
    this_dir = os.path.dirname(os.path.abspath(__file__))
    ds_algo_path = os.path.join(this_dir, "..", "data_structures_algorithms")

    methods_dict = GamePlay.get_available_methods(ds_algo_path)
    menu = GamePlay.build_menu(methods_dict)
    GamePlay.display_menu(menu)
