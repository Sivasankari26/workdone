from lxml import html
import cssselect
import glob
import sys
link_list = glob.glob("./www.allitebooks.org/*")
for filename in link_list:
	try:
		content = open(filename).read()
		tree = html.fromstring(content)
	except UnicodeError:
		print("error: " + filename)
		continue
	except:
		print("Unexpected error:", sys.exc_info()[0])
		pass
	hrefs = tree.cssselect('span.download-links a')
	for href in hrefs:
		print(href.attrib['href'])
