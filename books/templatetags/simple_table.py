# -*- coding: utf-8 -*-

from django import template

register = template.Library()

def simple_table(table_dict):
    if type(table_dict) is dict:
        if 'title' in table_dict and 'content' in table_dict:
            table = """
<table class='table table-bordered'>
    <thead>
        <tr>
            %s
        </tr>
    </thead>
    <tbody>
        %s
    </tbody>
</table>"""
            thead = ""
            tbody = ""

            for i in table_dict["title"]:
                thead += "<th>%s</th>" % (i)

            for row in table_dict["content"]:
                for index, item in enumerate(row):
                    if index == 0:
                        tbody += "<tr><td>%s</td>" % (item)
                    elif index == (len(table_dict['content'])-1):
                        tbody += "<td>%s</td></tr>" % (item)
                    else:
                        # Any other
                        tbody += "<td>%s</td>" % (item)
            return table % (thead, tbody)
    else:
        template.TemplateSyntaxError("Para el render, el elemento debe ser un diccionario")
    return None

register.simple_tag(simple_table)


