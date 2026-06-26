import streamlit as st
import streamlit.components.v1 as components

# baca file html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# baca css
with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# baca js
with open("dashboard.js", "r", encoding="utf-8") as f:
    js = f.read()

# gabungkan
final_html = f"""
<style>
{css}
</style>

{html}

<script>
{js}
</script>
"""

components.html(final_html, height=3000, scrolling=True)