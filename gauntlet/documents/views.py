from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from . import models


def _get_documents(parent_id):
    documents_to_check = list(models.Document.objects.filter(parent=parent_id))
    documents = []

    while documents_to_check:
        document = documents_to_check.pop(0)
        documents.append(document)

        documents_to_check.extend(
            list(models.Document.objects.filter(parent=document.pk))
        )

    return documents


@login_required
def index(request):
    documents = _get_documents(None)

    return render(request, 'index.html', {'documents': documents})


@login_required
def read(request, document_id):
    document = get_object_or_404(models.Document, pk=document_id)
    document.last_accessed = datetime.now()
    document.save()

    if request.method == 'POST':
        new_content = request.POST['pageContent']
        document.content = new_content
        document.last_updated = datetime.now()
        document.save()

    children = _get_documents(document_id)
    all_docs = _get_documents(None)

    return render(
        request,
        'read.html',
        {'document': document, 'children': children, 'all_docs': all_docs}
    )


@login_required
@require_http_methods(['POST'])
def create(request, document_id):
    parent = get_object_or_404(models.Document, pk=document_id)
    title = request.POST['name']

    document = models.Document.objects.create(
        title=title, content='Content here.', parent=parent
    )

    return redirect('read', document_id=document.pk)


@login_required
@require_http_methods(['POST'])
def create_new(request):
    title = request.POST['name']

    document = models.Document.objects.create(
        title=title, content='Content here.'
    )

    return redirect('read', document_id=document.pk)


@login_required
def delete_doc(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)

    document.delete()

    if not document.parent:
        return redirect('index')
    else:
        return redirect('read', document_id=document.parent.id)
