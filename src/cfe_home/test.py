import pathlib

this_dir = pathlib.Path(__file__).resolve().parent
html_ = ""
html_file_path = this_dir / "home.html"
html_ = html_file_path.read_text()
print(type(html_))