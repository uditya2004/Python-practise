#!/usr/bin/env python3
import cgi

print("Content-Type: text/html\n")

print("<html><body>")
print("<h1>Simple CGI Example</h1>")

form = cgi.FieldStorage()
name = form.getvalue("name", "No name entered")

print(f"<p>Hello, {name}!</p>")
print("</body></html>")

#=================================================

"""
STEPS TO USE THIS:-
1. Run:-
    cd CGI
    python -m http.server --cgi 8000

2. Then in webbrowser open http://localhost:8000/hello_form.html
"""