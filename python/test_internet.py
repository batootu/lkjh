import internet
from internet import *

import os
import glob

def search(se, q):
    r = se.search(q)
    se.parse(r)
    #~ se.tohtml()
    #~ se.tojson()

def devine(q, f=None):
    se = HornywhoresSearchEngine()
    search(se, q)
    #~ print(se)
    
    if len(se.results) == 0:
        none
    elif len(se.results) > 0:
        q2 = se.results[0]['text']
        if f:
            f.write(("<h2>{0}</h2>\n".format(q)).encode('utf-8'))
            f.write(("<h3>{0}: {1}</h3>\n".format(len(se.results), q2)).encode('utf-8'))
        q2 += " -torrent -torrentz -pastebin"
        se2 = GoogleSearchEngine()
        search(se2, q2)
        if f:
            for r in se2.results:
                host = r['link'][7:].split('/')[0].replace('www.', '')
                f.write(('<li>{0} <a href="{1}" target="_blank">{2}</a></li>\n'.format(host, r['link'], r['text']).encode('utf-8')))
        else:
            print(q, [r['text'].encode('utf-8') for r in se2.results])

if __name__ == "__main__":

    print(myip())
    
    f = open("test_internet_results.html", 'wb')
    for path in glob.glob("d:/.lkjhdata/dl/tbs3/*.*")[:5]:    
        bn = os.path.basename(path)
        bn = os.path.splitext(bn)[0]
        print(bn)
        q = bn
        devine(q, f)
    f.close()
    
    #~ se = GoogleSearchEngine()
    #~ se = IndexxxSearchEngine()
    #~ se = ThenudeSearchEngine()
