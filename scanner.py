from check import analyze_file, is_package_on_pypi

found_packages = analyze_file("test_script.py")
print(f"Packages found: {found_packages}")
for pkg in found_packages:
    if is_package_on_pypi(pkg):
        print(f"[SAFE] {pkg} exists on PyPI")
    else:
        print(f"[SAFE] {pkg} was not foun on PyPI-possible hallucination")