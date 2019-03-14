<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="2.0">
    
<xsl:template match="/">
    <html>
        <head> <title>Output</title></head>
        <body>
            <h2>Analysis of <xsl:value-of select="substring-before(replace(document-uri(.), '.*/', '') , '.xml')"/></h2>
            <table border="1">
                <thead><th>Subject</th><th>Property</th><th>Object</th><th>Number</th></thead>
                <tbody>
                    <xsl:for-each select="/analysis/output">
                        <xsl:for-each select="ns1:sparql/ns1:results/ns1:result" xmlns:ns1="http://www.w3.org/2005/sparql-results#">
                            <tr><td><xsl:value-of select="ns1:binding[@name='class_subject']"/></td><td>
                                <xsl:value-of select="../../../@property"/>
                                </td><td><xsl:value-of select="ns1:binding[@name='class_object']"/></td><td><xsl:value-of select="ns1:binding[@name='s_count']/ns1:literal"/></td></tr>
                        </xsl:for-each>
                        </xsl:for-each>
                </tbody>                
            </table>
        </body>
    </html>

</xsl:template>


</xsl:stylesheet>