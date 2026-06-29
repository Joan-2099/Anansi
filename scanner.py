from check import analyze_js_file, analyze_py_file,is_package_on_npm, is_package_on_pypi

def get_imports(file_path):
    if file_path.endswith(".py"):
        imports = analyze_py_file(file_path)
        lang = "Python"
        check_func = is_package_on_pypi
    elif file_path.endswith(".js"):
        imports = analyze_js_file(file_path)
        lang = "JavaScript"
        check_func = is_package_on_npm
        return 
    else:
        print("Unsupported file")
        return

    for pkg in imports:
        if check_func(pkg):
            print(f"[✅ SAFE] {pkg} exists in the {lang} registry")
        else:
            print(f"[❌ Alert] {pkg} was not found in the {lang} registry")

get_imports("test_script.py")