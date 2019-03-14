import requests
import urllib

preds = [ "http://purl.org/dc/terms/created" 	,
 "http://purl.org/dc/terms/modified" 	,
 "http://purl.org/dc/terms/extent" 	,
 "http://www.w3.org/2000/01/rdf-schema#isDefinedBy" 	,
 "http://www.w3.org/2000/01/rdf-schema#comment" 	,
 "http://www.w3.org/2002/07/owl#versionInfo" 	,
 "http://www.w3.org/2002/07/owl#priorVersion" 	,
 "http://purl.org/dc/terms/description" 	,
 "http://purl.org/dc/terms/title" 	,
 "http://www.w3.org/ns/dcat#themeTaxonomy" 	,
 "http://purl.org/dc/terms/publisher" 	,
 "http://xmlns.com/foaf/0.1/name" 	,
 "http://purl.org/dc/terms/issued" 	,
 "http://purl.org/dc/terms/spatial" 	,
 "http://www.w3.org/ns/dcat#dataset" 	,
 "http://www.w3.org/ns/dcat#record" 	,
 "http://purl.org/dc/terms/identifier" 	,
 "http://www.w3.org/ns/adms#identifier" 	,
 "http://www.w3.org/2006/vcard/ns#hasEmail" 	,
 "http://www.w3.org/ns/dcat#keyword" 	,
 "http://www.w3.org/ns/dcat#contactPoint" 	,
 "http://www.w3.org/2006/vcard/ns#fn" 	,
 "http://xmlns.com/foaf/0.1/mbox" 	,
 "http://xmlns.com/foaf/0.1/primaryTopic" 	,
 "http://www.w3.org/ns/adms#status" 	,
 "http://www.w3.org/ns/dcat#distribution" 	,
 "http://www.w3.org/ns/dcat#accessURL" 	,
 "http://purl.org/dc/terms/license" 	,
 "http://purl.org/dc/terms/format" 	,
 "http://www.w3.org/ns/dcat#theme" 	,
 "http://www.w3.org/ns/dcat#landingPage" 	,
 "http://purl.org/dc/terms/provenance" 	,
 "http://www.w3.org/ns/locn#geometry" 	,
 "http://purl.org/dc/terms/language" 	,
 "http://purl.org/dc/terms/temporal" 	,
 "http://schema.org/startDate" 	,
 "http://schema.org/endDate" 	,
 "http://purl.org/dc/terms/accrualPeriodicity" 	,
 "http://purl.org/dc/terms/rights" 	,
 "http://www.w3.org/ns/dcat#downloadURL" 	,
 "http://purl.org/dc/terms/type" 	,
 "http://purl.org/dc/terms/conformsTo" 	,
 "http://www.w3.org/ns/dcat#mediaType" 	,
 "http://xmlns.com/foaf/0.1/page" 	,
 "http://purl.org/dc/terms/source" 	,
 "http://purl.org/dc/terms/accessRights" 	,
 "http://www.w3.org/ns/dcat#byteSize" 	,
 "http://xmlns.com/foaf/0.1/homepage" 	,
 "http://purl.org/dc/terms/relation" 	,
 "http://purl.org/dc/terms/isVersionOf" 	,
 "http://www.w3.org/ns/adms#versionNotes" 	]


sparql = """select (count(?s) as ?s_count) ?class_subject ?class_object

WHERE { 
?s  <%s> ?o ;  a ?class_subject .
  optional {?o a ?class_object . }
  
}
group by ?class_subject ?class_object
limit 10""" 


endpoint = "https://www.europeandataportal.eu/sparql?query="


f=open(r'C:\Users\pedro\Documents\DXWG_DCAT_work\2019-03-14_edp_output.xml', 'wb')
f.write('<analysis>')
for i in preds:
    s = sparql % i
    squoted = urllib.quote(s)
    link = endpoint + squoted
    ret = requests.get(link)
    f.write('<output property="%s">' % (i))
    f.write(ret.text)
    f.write('</output>')
f.write('</analysis>')
f.flush()
f.close()

    

    
