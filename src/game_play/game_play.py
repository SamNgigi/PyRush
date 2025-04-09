import os
import ast
import re
import shutil
import platform
import subprocess


from typing import Optional
from collections import defaultdict

class GamePlay:

    @staticmethod
    def init_game()->None:
        """
        Encapsulates game logic and runs the game
        """

        

        print("Hi! Welcome to PyRush")

        this_dir: str = os.path.dirname(os.path.abspath(__file__))
        default_path = os.path.join(this_dir, "..", "data_structures_algorithms")
        methods_by_file: dict = GamePlay.get_available_methods(default_path)
        menu,selector_map = GamePlay.build_menu(methods_by_file)

        while True:
            GamePlay.clear_screen()

            GamePlay.display_menu(menu)

            selected = GamePlay.get_method_choice(selector_map)

            if selected['selector'] == "q":
                break
            if selected['selector'] == "t":
                # TODO: Run pytests on new window
                print("TODO: Exiting game to run tests")
                break

            GamePlay.edit_method(selected)



    @staticmethod
    def clear_screen()->None:

        os.system('cls' if os.name == 'nt' else 'clear')


    @staticmethod
    def edit_method(selected_function: dict)->None:

        file_path: str = selected_function['file_path']
        method_name: str = selected_function['function_name']

        # Reading original source code
        with open(file_path, "r", encoding="utf-8") as f:
            original_code = f.read()

        # Parse into AST
        tree = ast.parse(original_code, filename=file_path)

        # Searching for the function definition name
        target_node = None
        for node in ast.walk(tree):
            # Checking standard (non_async) functions
            if isinstance(node, ast.FunctionDef) and node.name == method_name:
                target_node = node
                break

        if not target_node:
            print(f"Method '{method_name}' not found in '{file_path}'")
            return
        
        # Stripping existing statements but retains docstring(if at the beginning) and decorators
        new_body = []
        # If the first statement is an Expr(Str), that's a docstring
        if(
            target_node.body and
            isinstance(target_node.body[0], ast.Expr) and
            isinstance(target_node.body[0].value, ast.Constant)
        ):
            new_body.append(target_node.body[0])

        # Insert placeholder
        placeholder = ast.Expr(value=ast.Constant(value=f"#TODO: implement {method_name}"))
        new_body.append(placeholder)

        # Replacing the older body
        target_node.body = new_body

        # Reconstructing the entire module as a string
        new_code = ast.unparse(tree)

        # Writing to a temporary file
        temp_path = os.path.join(
            os.path.dirname(file_path),
            f"temp_{os.path.basename(file_path)}"
        )
        with open(temp_path, "w", encoding="utf-8") as temp:
            temp.write(new_code)

        # We open the editor roughly around the old function's line number
        # ast.unparse can shift lines, but this is usually "close enough"
        cursor_line = target_node.lineno + 1
        
        GamePlay.open_editor(temp_path, cursor_line)
        
        # Replacing original with temp
        shutil.move(temp_path, file_path)

        

    @staticmethod
    def open_editor(file_path, cursor_line=1)->None:
        editor = os.getenv("EDITOR", "nvim")

        if platform.system().lower().startswith("win"):
            # use Gitbash for Windows
            command = f"bash -c \"{editor} '+call cursor({cursor_line},0)' '{file_path}'\""
        else:
            # Linux/Mac
            command = f"{editor} '+call cursor({cursor_line}, 0)' '{file_path}'"

        subprocess.call(command, shell=True)

    @staticmethod
    def get_method_choice(selector_map: dict)-> dict:
        
        while True:
            selection = input().strip()
            if selection in ("q", "t"):
                return {"selector": selection}
            if selection in selector_map:
                return selector_map[selection]
            print("Invalid choice. Please try again")

        

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
        current_class: Optional[str] = None
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
                    "end_lineno": tree_node.end_lineno,
                    "col_offset": tree_node.col_offset,
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
    def build_menu(methods_by_file: dict)->tuple[dict, dict]:
        """
        Build a nested structure suitable for display our game menu
        
        Returns 2 dicts:
        MENU
        {
            "FolderName":{
                "ShortFileName": [
                    {
                        "selector": "1.01", 
                        "display_name": "Search.binary_search_iterative",
                        "file_path": "search/search.py",
                        "lineno": 24,
                        "end_lineno": 50,
                        "col_offset": 10
                    },
                    ...
                ]
            },
            ...
        }
        SELECTOR_MAP
        {"1.01": {<the same dict>}}

        """
        menu = defaultdict(lambda: defaultdict(list))
        selector_map = {}

        # Counter to keep track of global file index
        file_counter: int = 1

        # Sort the files to have consistent output
        sorted_files = sorted(methods_by_file.keys())

        for file_path in sorted_files:
            top_folder = GamePlay.get_top_folder(file_path)
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

                selector_info = {
                    "selector": selector, 
                    "display_name": method_name,
                    "function_name": method['name'],
                    "file_path": file_path,
                    "lineno": method['lineno'],
                    "end_lineno": method['end_lineno'],
                    "col_offset": method['col_offset'],
                }

                menu[top_folder][short_file_name].append(selector_info)
                selector_map[selector] = selector_info

                method_counter += 1

            file_counter += 1


        return menu, selector_map

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
            print(f"{'File':<20}Method") # Performance wise print("File" + " " * 20 + Menu) is considered faster
            print("-"*100)

            for short_filename, methods in file_dict.items():
                print(f"\n{short_filename.title()}")
                for method in methods:
                    # For fixed-width formatting with appropriate spacing
                    selector = method['selector']
                    display_name = method['display_name']
                    
                    print(f"    {selector:<15} {display_name:<40}")
            print()
            print("q - Quit")
            print("t - Run Tests and Quit")
            print("Choose a method to implement (e.g., 1.02) 'q' to quit or 't' to run tests and Exit")





    

if __name__ == "__main__":

    # Getting this file current directory
    # this_dir = os.path.dirname(os.path.abspath(__file__))
    # ds_algo_path = os.path.join(this_dir, "..", "data_structures_algorithms")
    #
    # methods_dict = GamePlay.get_available_methods(ds_algo_path)
    # menu, selector_map = GamePlay.build_menu(methods_dict)
    # GamePlay.display_menu(menu)
    GamePlay.init_game()
