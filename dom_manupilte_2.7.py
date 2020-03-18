from xml.dom import minidom

text = "<div><p>xxxx</p></div>"
doc = minidom.parseString(text)

# For each div in the root document
for tag in doc.childNodes:
    # If it's a <p> and there's only one
    if len(tag.childNodes) == 1 and tag.childNodes[0].tagName == 'p':
        # p_node = <p>xxx</p>
        p_node = tag.childNodes[0]
        # p_text_node = xxx
        p_text_node = p_node.childNodes[0]
        value = p_node.nodeValue
        # Delete the <p>xxx</p>
        p_node.parentNode.removeChild(p_node)
        # Set the <div></div> -> <div>xxx</div>
        tag.appendChild(p_text_node)

print doc.toxml()
