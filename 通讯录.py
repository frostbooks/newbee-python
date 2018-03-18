print('---欢迎进入通讯录程序---')
print('---1:查询联系人资料---')
print('---2:插入新的联系人---')
print('---3:删除已有联系人---')
print('---4:推出通讯录程序---')
a = {'eddy':'13312344567','krystal':'123445678','jin':'1234567890'}
while True:
    code = int(input('请输入相关的指令代码：'))
    
    if code ==1:
        name = input('请输入联系人姓名：')
        if name in a:
            print(name+':'+a[name])
        else:
            print('抱歉，'+name+'不在通讯录当中')
            
    if code == 2:
        name =input('请输入联系人姓名：')
        phone = (input('请输入联系人电话：'))
        b={name:phone}
        a.update(b)

    if code ==3:
        name = input('请输入联系人姓名：')
        if name in a:
            if input('是否删除该联系人（是/否）：') =='是':
                    a.pop(name)
            

    if code ==4:
        print('感谢您使用通讯录程序')

        break

    
            
            
        
    
    
