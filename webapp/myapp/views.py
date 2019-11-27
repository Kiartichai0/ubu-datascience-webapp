from django.shortcuts import render
import numpy as np

def convert_to_ndarray(x):
    #y = np.random.random((6,5))
    x.replace('[','')
    x.replace(']','')
    y=[]
    for line in x.split('\n'):
        y.append(list(map(float, line.split())))
    return np.array(y)


def matmul(req):
    a = convert_to_ndarray('1 2 3\n6 7 8\n8 9 6')
    b = convert_to_ndarray('1 2 3 4 5\n6 7 8 9 1 \n9 8 7 6 4')
    if req.method == 'POST':
        #print('POST เด้อ')
        #print(req.POST['A'])
        a = convert_to_ndarray(req.POST['A'])
        #print(req.POST['B'])
        b = convert_to_ndarray(req.POST['B'])
        #print(req.POST)
        pass
    else:
        pass
        #print('GET เด้อ')
    return render(req,'myapp/matmul.html',{
        'A':a,
        'B':b,
        'C': np.dot(a,b)
        })