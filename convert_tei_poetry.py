import re
import lxml.etree as ET
from greek_normalisation.utils import nfc
from collections import defaultdict



GR = defaultdict(list)

BASE = 'book1.xml'
DATA_DIR = ".\\source_data\\"

GR_SRC = DATA_DIR + BASE


   


def process_file(xml):
    chapter = '0'
    output = {}
    p = xml.find('//p')
    for node in p.getchildren():
        unit = node.get('unit')
        if unit == 'chapter':
            chapter = node.get('n')
            if node.tail:
                output[f"{chapter}.0"] = node.tail.strip()
        if unit == 'section':
            output[f"{chapter}.{node.get('n')}"]  = node.tail.strip()
    return output





GRFILE = ET.parse(GR_SRC)





HEADER = """<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Argonautica</title>
		<meta name="viewport" content="width=device-width,initial-scale=1">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/alpheios-components@latest/dist/style/style-components.min.css"/>
        <link rel="stylesheet" href="typebase.css" type="text/css" />
        <link rel="stylesheet" href="normalize.css" type="text/css" />
        <link rel="stylesheet" href="fonts.css" type="text/css" />
    </head>
    <body>
    <div >
    """

FOOTER ="""</div>
</body>
<style>
    .wrapper {
        display: flex;
        margin: 4px;

    }

    .gr {
        flex:1;
        margin-right:2px;
    }
    .en { flex: 0;}
    .en-data { display: none; }
    .marker {margin-right: 0.5em;}
    .number {margin-right: 0.25em;}
</style>
<script>
    function toggleEn(e) {
        console.log('clicked');
        let par = e.target.parentElement;
        let x = par.querySelector('.en-data');
        if (x.style.display === "none") {
            x.style.display = "inline";
            par.style.flex = 1;
        } else {
            x.style.display = "none";
            par.style.flex = 0;
        }
    }

    function toggleMe(e) {
        console.log('clicked');
        let par = e.target;
        let x = par.querySelector('.en-data');
        if (x.style.display === "none") {
            x.style.display = "inline";
            par.style.flex = 1;
        } else {
            x.style.display = "none";
            par.style.flex = 0;
        }
    }

    const elems = document.getElementsByClassName('marker');

    for (var i=0; i < elems.length; i ++) {
        elems[i].addEventListener('click', toggleEn);
    }

    const elemsB = document.getElementsByClassName('en-data');
    for (var i=0; i < elemsB.length; i ++) {
        elemsB[i].addEventListener('click', toggleEn);
    }

</script>
<script type="text/javascript">
        document.addEventListener("DOMContentLoaded", function(event) {
        import ("https://cdn.jsdelivr.net/npm/alpheios-embedded@latest/dist/alpheios-embedded.min.js").then(embedLib => {
            window.AlpheiosEmbed.importDependencies({ 
            mode: 'cdn'
            }).then(Embedded => {
            new Embedded({clientId: "thrax-grammar-fhard"}).activate();
            }).catch(e => {
            console.error(`Import of Alpheios embedded library dependencies failed: ${e}`)
            })

        }).catch(e => {
            console.error(`Import of Alpheios Embedded library failed: ${e}`)
        })
        });
    </script>
</body></html>"""

with open('.\\docs\\index.html', 'w', encoding="UTF-8") as f:
    print(HEADER, file=f)
    print("<h1>Argonautica, Book 1</h1>", file=f)
    print('<div class="poetry-wrapper alpheios-enabled" lang="grc">', file=f)
    for lb in GRFILE.findall('//lb'):
        print(f'<div class="poetry-line">{(lb.tail or "")}</div>', file=f)
    print("</div>", file=f)
        
        
    print(FOOTER, file=f)




    



