from django.shortcuts import render , redirect
import markdown
from . import util
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view_entry(request , title):
    md = markdown.Markdown()
    return render(request , "encyclopedia/entry.html" , {
        "entry": md.convert(util.get_entry(title)),
        "title":title })



def search(request):
    entry_name = request.GET['q']
    entries = []

    if entry_name == '':
        return render(request , "encyclopedia/entry.html" , {
        "entry": "You Searched None",
        "title": "search_results" })

    for entry in util.list_entries():
        if entry_name == entry:
            return redirect('view_entry' , title=entry)

    for entry in util.list_entries():
        if entry_name in entry :
            entries.append(entry)
    
    return render(request , "encyclopedia/search_results.html" , { "entries":entries })


def new_page(request):
    if request.method == 'POST':
        if not request.POST['title'] or not request.POST['content'] :
            return render(request , "encyclopedia/new_page.html" , {'error':True,
                                                                    'message': 'fill the form '} )

        list = util.list_entries()
        if request.POST['title'] in list :
            return render(request , "encyclopedia/new_page.html" , {'error':True,
                                                'message':'this entry already exists',
                                                'title':request.POST['title'] , 
                                                'content':request.POST['content']} )
        
        util.save_entry(request.POST['title'] , request.POST['content'])
        return redirect('view_entry' , title=request.POST['title'])

    else :
        return render(request , "encyclopedia/new_page.html" , {'error':False})

def edit_page(request , title ):
    if request.method == 'POST' :

        util.save_entry(request.POST['title'] , request.POST['content'])

        return redirect('view_entry' , title=request.POST['title'] )
    
    else : 
        return render(request , "encyclopedia/new_page.html" , {'error': False, 
                                                                'title':title,
                                                                'content':util.get_entry(title)})

def random_page(request):
    list = util.list_entries()
    entry = random.choice(list)
    return redirect('view_entry' , title=entry)



    

    

    


