"""

The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'

"""
def make_tags(tag, word):
    brack1="<"
    brack2=">"
    slash="/"
    quote="'"
    return quote+brack1+tag+brack2+word+brack1+slash+tag+brack2+quote

print(make_tags('i', 'Yay'))