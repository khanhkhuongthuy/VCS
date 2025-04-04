class calculator:
    def RemoveTheLargest():
        list=[]
        num=int(input("Enter a number:"))
        if num not in list:
            list.append(num)
        if len(list)==10:
            max=max(list)
            list.remove(max)
        return list
    pass
