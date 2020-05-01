<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0">

    <xsl:template match="/">
        <html>

            <head>
                <style type="text/css">
                    table.tfmt {
                    border: 1px ;
                    }

                    td.colfmt {
                    border: 1px ;
                    background-color: white;
                    color: black;
                    text-align:right;
                    }

                    th {
                    background-color: cyan;
                    color: black;
                    }

                </style>
            </head>

            <body>
                <table class="tfmt">
                    <tr>
                        <th style="width:250px">Title:</th>
                        <th style="width:350px">Href:</th>
                        <th style="width:250px">Ratings:</th>
                        <th style="width:250px">Author:</th>
                        <th style="width:250px">Image:</th>>


                    </tr>

                    <xsl:for-each select="root/element">

                        <tr>
                            <td class="colfmt">
                                <xsl:value-of select="title"/>
                            </td>
                            <td class="colfmt">
                                <xsl:value-of select="href"/>
                            </td>

                            <td class="colfmt">
                                <xsl:value-of select="ratings"/>
                            </td>
                            <td class="colfmt">
                                <xsl:value-of select="author"/>
                            </td>
                             <td class="colfmt">
                                <xsl:value-of select="image"/>
                            </td>
                        </tr>

                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>