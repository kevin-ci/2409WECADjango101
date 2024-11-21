from django.shortcuts import render, get_object_or_404, redirect
from .models import List, Item
from .forms import ListForm, ItemForm
from django.forms import modelformset_factory

# Create your views here.
def all_lists(request):
    all_lists = List.objects.all()

    context = {
        'lists': all_lists,
    }

    return render(request, 'todo/home.html', context)

def view_list(request, list_id):
    todo_list = get_object_or_404(List, id=list_id)

    context = { 
        'list': todo_list,
    }

    return render(request, 'todo/view_list.html', context)

def create_list(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "List created successfully.")
            return redirect('all_lists')
        else:
            return redirect('create_list')
    else:
        form = ListForm()
        context = {
            "form": form,
        }
        return render(request, 'todo/create_list.html', context)


def add_items(request, list_id):
    # retrieve the list we want to add to
    list_instance = get_object_or_404(List, id=list_id)
    
    # create a form factory which creates item forms; 
    # the extra kwarg will put n extra empty forms at the bottom of the page; 
    # can_delete determines whether the formset can delete items or just create them
    ItemFormSet = modelformset_factory(Item, form=ItemForm, extra=0, can_delete=True)


    if request.method == "POST":
        # create a new ItemFormSet which contains any existing items from our list
        formset = ItemFormSet(request.POST, queryset=Item.objects.filter(parent_list=list_instance))
        
        
        if formset.is_valid():
            # Save valid forms
            items = formset.save(commit=False)
            for item in items:
                # add the list id to the items
                item.parent_list = list_instance
                item.save()

            # Delete items marked for deletion
            for obj in formset.deleted_objects:
                obj.delete()

            return redirect('view_list', list_id=list_id)  # Adjust the redirect URL
        else:
            print(formset.errors)  # Debugging: Print errors in formset
    else:
        formset = ItemFormSet(queryset=Item.objects.filter(parent_list=list_instance))

    return render(request, 'todo/add_items.html', {'formset': formset, 'list_instance': list_instance})