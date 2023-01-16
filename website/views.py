from django.http import HttpResponse,HttpResponseRedirect 
from django.shortcuts import render
from product.models import Product
from homeproduct.models import homeProduct


from contact.models import Contact
def homePage(request):
    productData=homeProduct.objects.all().order_by('product_name')
    
    if request.method =='GET':
        pn=request.GET.get('productname')
        if pn!=None:
            productData=homeProduct.objects.filter(product_name__icontains=pn)
 
    
    data ={
       'productData':productData,
       
    }
    
    
    
    return render(request,'index.html',data)


   

'''
    data={
        'title': 'Home Page',
        'bdata': 'Welcome to Website',
        'alist': ['Java','Python','c','php'],
        'number': [10,20,30,40,50,60],
        'student_detail': [
        {'name':'Arun','phone':7007722437},
        {'name':'Amit', 'phone': 8182817823}

        ]
    }'''





def about(request):
    return render(request,'about.html')
 
def contact(request):
    if request.method=='POST':
        
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        item=request.POST.get('item')
        en = Contact(username=username,phone=phone,address=address,item=item)
        en.save()
        
    return render(request,'contact.html')



def price(request):
    productData=Product.objects.all().order_by('product_name')
    
    if request.method =='GET':
        pn=request.GET.get('productname')
        if pn!=None:
            productData=Product.objects.filter(product_name__icontains=pn)

    
    data ={
       'productData':productData,
       
    }
    
    return render(request,'price.html',data)

def term(request):
    return render(request,'term.html')



    