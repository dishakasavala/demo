from django.shortcuts import render,redirect
from webapp.models import slider,enter,catagory,Category,Product
from adminapp.models import cart,cartForm
# Create your views here.
def index(request):
    sdata = slider.objects.all()
    catd = catagory.objects.all()
    cdata = Category.objects.all()
    pdata = Product.objects.all()
    return render(request,'index.html',{'sdata':sdata,'catd':catd,'cdata':cdata,'pdata':pdata})
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contactp(request):
    return render(request,'contact.html')
def shop(request):
    return render(request,'shop.html')
def singlepost(request):
    return render(request,'single-post.html')
def styles(request):
    return render(request,'styles.html')
def thankyou(request):
    return render(request,'thank-you.html')
def blogmasony(request):
    return render(request,'blog-masonry.html')
def blogsidebar(request):
    return render(request,'blog-sidebar.html')
def cartp(request):
    pdata = Product.objects.all()
    return render(request,'cart.html',{'pdata':pdata})
def checkout(request):
    return render(request,'checkout.html')
def comingsoon(request):
    return render(request,'coming-soon.html')
def error(request):
    return render(request,'error.html')
def faqs(request):
    return render(request,'faqs.html')
def loginadmin(request):
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
            return redirect("/data")
        else:
            print('failer')
            msg = "Invalid email and password"
    return render(request,'ad_login.html')
def shpogrid(request):
    return render(request,'shop-grid.html')
def shoplist(request):
    return render(request,'shop-list.html')
def shopslider(request):
    return render(request,'shop-slider.html')
def singleproduct(request,p_id):
    user = ''
    if 'user_id' in request.session:
        uid = enter.objects.filter(id=request.session['user_id']).get()
        print(uid)
    # if 'wid' not in request.session:
    #     return redirect('/login')
    obj = Product.objects.filter(id=p_id).get() 
    cat_id = obj.category.category
    
    crt = cartForm(request.POST)
    if 'add' in request.POST:
        crt = cartForm(request.POST)
        crt.save()
        return redirect('/cart')
    # c = Category.objects.filter(id=cat_id).get()
    # cate = c.category
    return render(request,'single-product.html',{'obj':obj,'crt':crt,'user_id':uid,'user':user,'pro_id':p_id})
def wishlist(request):
    return render(request,'wishlist.html') 