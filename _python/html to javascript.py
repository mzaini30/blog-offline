import re


html = """
    <div class="w3-red w3-container w3-center">
        <h1>Blog</h1>
    </div>
    <div class="w3-container">
        <div class="markdown"></div>
    </div>
    <div class="w3-red w3-container w3-center">
        <p><a href="a.html">Kembali ke halaman beranda</a></p>
    </div>
    <script src="../bin/jquery.min.js"></script>
    <script src="../bin/marked.min.js"></script>
    <script>
    $("div.markdown").html(marked($("textarea.markdown").val()))
    </script>
</body>
</html>
"""


javascript = re.sub(r"\"", r"'", html)
javascript = re.sub(r"\n", r"\\\n", javascript)
javascript = re.sub(r"""<script""", r"""<scr"+"ipt""", javascript)
javascript = re.sub(r"""</script""", r"""</scr"+"ipt""", javascript)
print
print """document.writeln(\"""",
print javascript,
print """")"""