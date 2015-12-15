from lxml import etree
from six.moves import urllib

inputquery = "(x^2 - 4)(x+1)(4 - y)"
appid = "834JUH-LUV8EVJ928"


query = urllib.parse.urlencode(dict(
    input=inputquery,
    appid=appid
))

url = 'http://api.wolframalpha.com/v2/query?' + query + "&format=mathml"

x = "http://api.wolframalpha.com/v2/query?input=%28x%5E2+-+4%29&appid=834JUH-LUV8EVJ928&format=mathml"
print x == url
print x
print url
#tree = etree.parse("http://api.wolframalpha.com/v2/query?input=%28x%5E2+-+4%29&appid=834JUH-LUV8EVJ928&format=mathml")
tree = etree.parse(url)


def works(someXML):
  #don't even open() the XSL file ...
  xslt_tree = etree.parse("./xsltml_2.0/mmltex.xsl")
  transform = etree.XSLT(xslt_tree)
  result = transform(someXML)
  return result


l = tree.xpath("//pod[contains(@title, 'Alternate form')]")[0]
NSMAP = {'mw':'http://www.w3.org/1998/Math/MathML'}
subpods = l.findall('.//mw:math', namespaces=NSMAP)
print subpods
print len(subpods)
i = 0
for pod in subpods:
  print pod
  print works(pod)

print "here"
