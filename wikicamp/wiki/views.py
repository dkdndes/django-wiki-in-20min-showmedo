from wiki.models import Page
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import markdown

def view_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
    except Page.DoesNotExist:
        return render_to_response ("create.html",
                {"page_name": page_name})
    content = page.content
    # transform content with markdown formating
    content = markdown.markdown(content)
    data_dictionary = {"page_name":page_name, "content":content}
    return render_to_response("view.html", data_dictionary) 

def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        # if the page exists we load the content from the database for display
        content = page.content
    except Page.DoesNotExist:
        # if the page does not exist we set the content to blank
        content = ""
    # we render the page edit.html and hand over the dict "page_name" 
    template = "edit.html"
    data_dictionary = {"page_name": page_name, "content":content} 
    context_instance=RequestContext(request)
    return render_to_response (template, data_dictionary, context_instance)

def save_page(request, page_name):
    # request the content from the form
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=page_name)
        # if the page exists we write the new content into the database
        page.content = content
    # if Page does not exist we save the page in the database
    except Page.DoesNotExist:
        page = Page(name=page_name, content=content)
    page.save()
    return HttpResponseRedirect("/wikicamp/" + page_name + "/")


