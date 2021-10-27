from html import document
from html.tags import body

doc = document("page")
with doc:
    doc.head()
    with body(doc.file) as b:
        b.h1("Witaj na stronie testowej")
        b.p("To jest paragraf")
