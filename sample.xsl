<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Products</h2>
                <table border="1">
                    <tr bgcolor="#ff8080">
                        <th>Name</th>
                        <th>Link</th>
                        <th>Rating</th>
                        <th>Price</th>
                    </tr>
                    <xsl:for-each select="Products/product">
                        <tr>
                            <td>
                                <xsl:value-of select="Name" />
                            </td>
                            <td>
                                <xsl:value-of select="Link" />
                            </td>
                            <td>
                                <xsl:value-of select="Rating" />
                            </td>
                            <td>
                                <xsl:value-of select="Price" />
                            </td>
                        </tr>
                         </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>