import requests
import ast
import esprima

def analyze_js_file(path):
    with open(path, "r", encoding="utf-8") as file:
        source_code=file.read()

    tree= esprima.parseModule(source_code)
    imports = []

#esprima returns a body list of nodes  
    for node in tree.body:
        # Check for 'import ... from "package"'
        if node.type == 'ImportDeclaration':
            # The source is the string part (e.g., 'express')
            pkg = node.source.value
            imports.append(pkg)
            
    return set(imports)

def is_package_on_pypi(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200# 200 means it exists
    except requests.RequestException:
        return False#assumes fals if it doesn't exist
   
def analyze_py_file(path):
    with open(path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())#parse file into an AST

    imports = []#list to store filtered data

#isinstance checks for the current object/statement if it has
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):#cathes standard import statements
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):#catches from import statements
            if node.module:
                imports.append(node.module)
    return set(imports)

 
def is_package_on_npm(package_name):
    url = f"https://registry.npmjs.org/{package_name}"
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200# 200 means it exists
    except requests.RequestException:
        return False