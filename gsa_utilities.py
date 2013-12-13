import urllib2
from pprint import pprint
import xml.etree.ElementTree as ET

def get_gsa(keyword):
    url="http://gsa17.enterprisedemo-google.com/search?site=USER_APPS&output=xml_no_dtd&proxycustom=%3CHOME/%3E&getfields=*&q="+keyword

    try:
        result = urllib2.urlopen(url)
        return result.read().decode("latin-1").encode("UTF-8")
    except urllib2.URLError, e:
        print "ops.."

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    return root

def XMLtag_toExpert(xml_R):
    out = {}
    out["name"] = xml_R.find('MT[@N="name"]').attrib["V"]
    out["mail"] = xml_R.find('MT[@N="mail"]').attrib["V"]
    out["profileUrl"] = xml_R.find('MT[@N="profileUrl"]').attrib["V"]  
    out["company"] = xml_R.find('MT[@N="company"]').attrib["V"]
    out["department"] = xml_R.find('MT[@N="department"]').attrib["V"]
    out["title"] = xml_R.find('MT[@N="title"]').attrib["V"]
    out["locality"] = xml_R.find('MT[@N="locality"]').attrib["V"]
    out["address"] = xml_R.find('MT[@N="address"]').attrib["V"]
    out["manager"] = xml_R.find('MT[@N="manager"]').attrib["V"]  
    out["country"] = xml_R.find('MT[@N="country"]').attrib["V"]
    out["imageUrl"] = xml_R.find('MT[@N="imageUrl"]').attrib["V"]

    out["telephone work"] = xml_R.find('MT[@N="telephone work"]').attrib["V"] 
    out["telephone mobile"] = xml_R.find('MT[@N="telephone mobile"]').attrib["V"]
    out["expertise social"] = xml_R.find('MT[@N="expertise social"]').attrib["V"]  
    out["expertise"] = xml_R.find('MT[@N="expertise"]').attrib["V"]
     
    return out

def get_list_of_experts(keyword):
    xml_result=get_gsa(keyword)
    list_of_XML_R = parse_xml(xml_result).find("RES")
    if list_of_XML_R == None:
        return []
    else:
        list_of_XML_R = list_of_XML_R.findall("R")
    return [XMLtag_toExpert(x) for x in list_of_XML_R]