from check import analyze_js_file, analyze_py_file, is_package_on_pypi

def get_imports(file_path):
    if file_path.endswith(".py"):
        return analyze_py_file(file_path)
    elif file_path.endswith(".js"):
        return analyze_js_file(file_path)
    else:
        raise ValueError("Unsupported file type")
    
found_packages = get_imports("test_script.py")
print(f"Packages found: {found_packages}")
for pkg in found_packages:
    if is_package_on_pypi(pkg):
        print(f"[SAFE] {pkg} exists")
    else:
        print(f"[SAFE] {pkg} was not found")