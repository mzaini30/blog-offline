document.writeln(" \
    <div class='w3-red w3-container w3-center'>\
        <h1>Blog</h1>\
    </div>\
    <div class='w3-container'>\
        <div class='markdown'></div>\
    </div>\
    <div class='w3-red w3-container w3-center'>\
        <p><a href='a.html'>Kembali ke halaman beranda</a></p>\
    </div>\
    <scr"+"ipt src='../bin/jquery.min.js'></scr"+"ipt>\
    <scr"+"ipt src='../bin/marked30.min.js'></scr"+"ipt>\
    <scr"+"ipt>\
    $('div.markdown').html(marked($('textarea.markdown').val()))\
    </scr"+"ipt>\
</body>\
</html>\
")