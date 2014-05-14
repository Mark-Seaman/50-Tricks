#!/usr/bin/env python
# Create a structured list for the menu

from sys  import argv
from json import dumps,loads

#-----------------------------------------------------------------------------
# Readers
#-----------------------------------------------------------------------------

def fix_menu(path, menu):
    results = []
    for item in menu.split('\n'):
        x = item.split(',')
        if len(x) > 4:
            print 'BAD: ', item
            item = ','.join([ '%s %s'%(x[0],x[1]), x[2], x[3], x[4] ])
        results.append(item)
    f = open(path,'w')
    f.write('\n'.join(results))
    f.close()
    
def add_menu_item(menu, item):
    x = item.split(',')
    if len(x) == 4:
        selection = x[0]+','+x[1]
        group = x[2]
        category = x[3]
    else:
        selection = x[0]+x[1]+','+x[2]
        group = x[3]
        category = x[4]
 
    if menu.has_key(category):
        if menu[category].has_key(group):
            menu[category][group].append(selection)
        else:
            menu[category][group] = [ selection ]
    else:
        menu[category] = { group: [ selection ] }

    return menu


def create_menu(menu_text):
    menu = {}
    for item in menu_text.split('\n'):
        menu = add_menu_item(menu, item) 
    return  menu


# Create a object list for the options
def data_structure(options):
    data = options.split('\n')
    data = filter(lambda x:len(x)>4, data)
    return [ i.split(',') for i in data ]


#-----------------------------------------------------------------------------
# Writers
#-----------------------------------------------------------------------------

def print_menu_json(menu):
    return  dumps(menu)


def print_menu(menu):
    print "Today's menu"
    for m in sorted(menu):
        print '\n.......................\n\n',m
        for group in menu[m]:
            print '\n    ', group
            for item in menu[m][group]:
                print '        ', item

layout_begin = open('layout1.html').read()
layout_end   = open('layout2.html').read()

ctrl_begin   = '<div ng-controller="food_selector">'
ctrl_end     = '</div>'

page_begin   = '''<h1>%s</h1>
<a href="Index">Index</a> * <a href='Select'>Select Food</a> * <a href="Summary">Data</a><br><br>'''
page_end     = ''

tabset_begin = '<tabset ng-show="true">\n'
tabset_end   = '</tabset>\n'

group_begin  = '<tab heading="%s"><div class="page"><ul>\n'
group_end    = '</ul></div></tab>\n'

def print_item(item):
    name,price = item.split(',')
    print "<li>"
    func = 'select_item("%s")'%item
    print "  <input type='checkbox' ng-click='%s'>"%func
    print "  <span>"
    print "     %s,  Price/serving: $%s"%(name,price)
    print "  </span>"
    print "</li>\n"

def print_item_list(menu):
    for m in sorted(menu):
        print group_begin%m
        for group in menu[m]:
            print '\n<br><b>%s</b>'%group
            print '<ul class="unstyled">'
            for item in menu[m][group]:
                print_item(item)
            print '</ul><br>\n'
        print group_end

def print_menu_html(menu):
    print layout_begin
    print ctrl_begin
    print page_begin%"Menu"
    print tabset_begin
    print_item_list(menu)
    print tabset_end
    print '<pre>Selected items:\n{{selection}}</pre>'
    print page_end
    print ctrl_end
    print layout_end

def print_html_summary(menu):
    
    print layout_begin
    print ctrl_begin
    print page_begin%"Summary"
    print tabset_begin
    print_item_list(menu)
    print tabset_end
    print '<pre>Selected items:\n{{selection}}</pre>'
    print page_end
    print ctrl_end
    print layout_end


# Print food selector
def  print_selector_data(menu):
    print layout_begin
    print ctrl_begin
    print page_begin%"Data"
 
    print tabset_begin
    print "<script> $scope.selection = [ 'None' ] </script>"
    for m in sorted(menu):
        print group_begin%m
        for group in menu[m]:
            print '\n<br><b>%s</b>'%group
            print '<ul>'
            for item in menu[m][group]:
                name,price = item.split(',')
                print "<li>"
                print "  <input type='checkbox' ng-click='select_item($item)'>"
                print "  <span>"
                print "     %s,  Price/serving: $%s"%(name,price)
                print "  </span>"
                print "</li>\n"
            print '</ul><br>\n'
        print group_end
    print tabset_end
    print '<pre>Selected items:{{selection}}</pre>'
    print page_end
    print ctrl_end
    print layout_end
  

#-----------------------------------------------------------------------------
# Top level scripts

def print_menu_file(f, format=print_menu):
    menu_text = open(f).read()[:-1]
    #if menu_ok(menu_text):
    menu = create_menu(menu_text)
    format(menu)
