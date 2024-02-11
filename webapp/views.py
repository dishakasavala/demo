from django.shortcuts import render,redirect
from webapp.models import enter,enterForm,slider,sliderForm,catagory,catForm,Category,CategoryForm,Product,ProductForm

# Create your views here.
def loginpage(request):
    msg = ''
    if 'user_id' in request.session:
        return redirect('/data')
    if 'login' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        obj = enter.objects.filter(email=email,password=password)
        if obj.count()==1:
            print('success')
            row = obj.get() 
            request.session['user_id'] = row.id
            return redirect('/data')
        else:
            print('failer')
            msg = "Invalid email and password"
    return render(request,'login.html',{'msg':msg})
def enterpage(request):
    s = ''
    frm = enterForm()
    if 'register' in request.POST:
        frm = enterForm(request.POST)
        frm.save()
        s = "suceessfully enter"
        return redirect('/login')
    return render(request,'enter.html',{'ans':s,'frm':frm})
def logout(request):
    del request.session['user_id']
    return redirect('/login')
def datapage(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    user_id = request.session['user_id']
    return render(request,'data.html',{'id':user_id})



def sliderpage(request):
    frmobj = sliderForm()
    if 'submit' in request.POST:
        frmobj = sliderForm(request.POST,request.FILES)
        frmobj.save()
        print('sucees')
        return redirect('/tables')
    return render(request,'slider.html',{'frm':frmobj})
def slidertable(request):
    sdata = slider.objects.all()
    return render(request,'slider-table.html',{'sdata':sdata})
def editslider(request,sed_id):
    obj = slider.objects.filter(id=sed_id).get()
    frmobj = sliderForm(instance=obj)
    if 'submit'in request.POST:
        frmobj = sliderForm(request.POST,request.FILES,instance=obj)
        frmobj.save()
        return redirect('/tables')
    return render(request,'edit_slider.html',{'frm':frmobj})
def deleteslider(request,sdel_id):
    slider.objects.filter(id=sdel_id).delete()
    return redirect('/tables')


def cattable(request):
    catd = catagory.objects.all()
    return render(request,'catagory-table.html',{'catd':catd})
def addcatagory(request):
    frm = catForm()
    if 'submit' in request.POST:
        frm = catForm(request.POST,request.FILES)
        frm.save()
        return redirect('/cat_table')
    return render(request,'catagory.html',{'frm':frm})
def editcat(request,ced_id):
    s=''
    obj = catagory.objects.filter(id=ced_id).get()
    frm = catForm(instance=obj)
    if 'submit' in request.POST:
        frm = catForm(request.POST,request.FILES,instance=obj)
        frm.save()
        return redirect('/cat_table')
    return render(request,'edit-cat.html',{'frm':frm})
def delcat(request,cdel_id):
    catagory.objects.filter(id=cdel_id).delete()
    return redirect('/cat_table')


def catetable(request):
    cted = Category.objects.all()
    return render(request,'table-category.html',{'cted':cted})
def addcategory(request):
    frm = CategoryForm()
    if 'submit' in request.POST:
        frm = CategoryForm(request.POST,request.FILES)
        frm.save()
        return redirect('/category_table')
    return render(request,'add-category.html',{'frm':frm})
def editcate(request,caed_id):
    obj = Category.objects.filter(id=caed_id).get()
    frm = CategoryForm(instance=obj)
    if 'submit' in request.POST:
        frm = CategoryForm(request.POST,request.FILES,instance=obj)
        frm.save()
        return redirect('/category_table')
    return render(request,'edit-category.html',{'frm':frm})
def delcate(request,cadel_id):
    Category.objects.filter(id=cadel_id).delete()
    return redirect('/category_table')


def producttable(request):
    pdata = Product.objects.all()
    return render(request,'table-product.html',{'pdata':pdata})
def addproduct(request):
    cats = Category.objects.all()
    frm = ProductForm()
    if 'submit' in request.POST:
        frm = ProductForm(request.POST,request.FILES)
        frm.save()
        return redirect('/product_table')
    return render(request,'add-product.html',{'cats':cats,'frm':frm})
def editproduct(request,proed_id):
    obj = Product.objects.filter(id=proed_id).get()
    frm = ProductForm(instance=obj)
    if 'submit' in request.POST:
        frm = ProductForm(request.POST,request.FILES,instance=obj)
        frm.save()
        return redirect('/product_table')
    return render(request,'edit-product.html',{'frm':frm})
def delproduct(request,prodel_id):
    Product.objects.filter(id=prodel_id).delete()
    return redirect('/product_table')

def carttable(request):
    return render(request,'cart-table.html')