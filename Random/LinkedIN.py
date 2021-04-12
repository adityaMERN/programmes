parents = [{"name": "p1"},
    {"name": "p2"},
    {"name": "p3"},
    {"name": "p4"},
]
children = [
    {"name":"c1", "parent":"p1"},
    {"name":"c2", "parent":"p2"},
    {"name":"c3", "parent":"p2"},
    {"name":"c4", "parent":"p3"},
    {"name":"c5", "parent":"p3"},
    {"name":"c6", "parent":"p3"},
    {"name":"c7", "parent":"p4"},
    {"name":"c8", "parent":"p4"},
    {"name":"c9", "parent":"p4"},
    {"name":"c10", "parent":"p4"},
]
output=[]
nameOfParent=[]   
for each in parents:
    for i in each:
	    nameOfParent.append(each[i])
nameOfPair=[] 
for each in children:
    inter=[]
    for key,value in each.items():
        x=value
        inter.append(x)
    nameOfPair.append(inter)
	    
#print(nameOfParent)
#['p1', 'p2', 'p3', 'p4']
#print(nameOfPair)
#[['c1', 'p1'], ['c2', 'p2'], ['c3', 'p2'], ['c4', 'p3'], ['c5', 'p3'], ['c6', 'p3'], ['c7', 'p4'], ['c8', 'p4'], ['c9', 'p4'], ['c10', 'p4']]
for eachPair in nameOfPair:
    #eachPair=[c1,p1]
    
    eachFamily=[]
    childrenSubList=[]
    for parent in nameOfParent :
        #parent=p1
        
        if eachPair[1]==parent:
            childrenSubList.append(eachPair[0])
        eachFamily.append([parent,childrenSubList])
    output.append(eachFamily)
print(output)
        
  	 
  	        
  	    


