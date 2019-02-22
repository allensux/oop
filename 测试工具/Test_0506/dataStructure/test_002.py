# coding:utf8

def test002():
    # str=input("输入字段：")
    str = 'lxs,hqq,lj,xc'
    List = str.split(',')

    # str_xml=input("输入替换的模板：")
    str_xml = '<step id="xml_set_xml_value" comment="value" isrun="true"><param id="xml">VAR_XML</param><param id="xpath">//MbfBody/value</param><param id="value">COLUMN(VALUE,y)</param></step>'

    # 列表追加，回车成多行
    def add_xml(L):
        xml_list = []
        s1 = '\n'  # 回车换行符
        for value in L:
            VAULE = value.upper()
            xml = str_xml.replace('value', value, 2).replace('VALUE', VAULE, 1)  # 替换模板中的值为列表中的值，小写两次，大写一次
            xml_list.append(xml)
        xml_str = s1.join(xml_list)  # list 更新成str
        return xml_str

    # 字符串追加，一行
    # def add_xml(L):
    #   xml_list=''
    #   for value in L:
    #     VAULE=value.upper()
    #     xml= str_xml.replace('value',value,2).replace('VALUE',VAULE,1) #替换模板中的值为列表中的值，小写两次，大写一次
    #     xml_list+=xml
    #   # xml_str=s1.join(xml_list) #list 更新成str
    #   return xml_list

    test = add_xml(List)
    print(test)
test002()