# coding: utf-8

from django.utils import timezone
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rango.models import Category, CatPage, SubPage, Answers, CategoryUserLikes, Subject
from rango.forms import CategoryForm, CatPageForm, SubPageForm, UserForm, UserProfileForm, TestUeditorModelForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from forms import TestUeditorModelForm
from django.http import JsonResponse

# def index(request):
#     print request.META
#     print request.method
#
#     return HttpResponse("Rango says hey there world<br>"
#                         "<a href='/rango/about'>About</a>")


def index(request):
    category_list = Category.objects.order_by('-likes')[0:5]
    page_list = CatPage.objects.order_by('-views')[0:5]

    context_dict = {'categories': category_list, 'pages': page_list}

    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if(datetime.now() - last_visit_time).seconds > 0:
            visits += 1
            reset_last_visit_time = True
    else:
        reset_last_visit_time = True

    if reset_last_visit_time:
        last_visit_time = str(datetime.now())
        request.session['last_visit'] = last_visit_time
        request.session['visits'] = visits

    context_dict['last_visit'] = last_visit
    context_dict['visits'] = visits

    response = render(request, 'rango/index.html', context_dict)

    return response


def about(request):
    content_dict = {'boldmessage': 'Could u tell me something about yourself?'}

    if request.session.get('visits'):
        count = request.session.get('visits')
    else:
        count = 0

    content_dict['visits'] = count

    return render(request, 'rango/about.html', content_dict)


def category(request, cat_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=cat_name_slug)
        print cat_name_slug
        pages = CatPage.objects.filter(category=category)
        answers = Answers.objects.filter(category=category)
        user = request.user
        if user.is_authenticated():
            is_liked = CategoryUserLikes.objects.filter(category=category).filter(user=request.user)
        else:
            is_liked = None
        # print is_liked

        context_dict['pages'] = pages
        context_dict['answers'] = answers
        context_dict['category'] = category
        context_dict['cat_name_slug'] = cat_name_slug

        editor = TestUeditorModelForm()
        context_dict['editor'] = editor

        context_dict['is_liked'] = is_liked

        context_dict['subject'] = category.subject

    except Category.DoesNotExist:
        context_dict = {}

    return render(request, 'rango/category.html', context_dict)


def subject(request, sub_name_slug):
    context_dict = {}

    try:
        subject = Subject.objects.get(slug=sub_name_slug)

        context_dict['subject'] = subject
        # context_dict['act_sub'] = subject
    except Subject.DoesNotExist:
        context_dict = {}

    return render(request, 'rango/subject.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print "form.errors", form.errors

        return HttpResponseRedirect('/rango/')
    else:
        form = CategoryForm()
        return render(request, 'rango/add_category.html', {'form': form})


def add_cat_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        if request.COOKIES["postToken"] != 'allow':
            pass
            # return HttpResponse("you can't post it again.")
        else:
            form = CatPageForm(request.POST)

            if form.is_valid():
                page = form.save(commit=False)
                page.user = request.user
                page.category = cat
                page.views = 0
                page.save()
                # response = category(request, category_name_slug)
                response = HttpResponseRedirect('/rango/category/'+category_name_slug)

                # response.set_cookie("postToken",value='disable')
            else:
                print "form.errors", form.errors

    else:

        form = CatPageForm()

        context_dict = {'form': form, 'category': cat, 'category_name_slug': category_name_slug}
        response = render(request, 'rango/add_page.html', context_dict)
        response.set_cookie("postToken", value='allow')

    return response
    # return HttpResponseRedirect('/rango/category/'+category_name_slug)


@login_required
def restricted(request):
    # return HttpResponse("Since you're logged in, you can see this text!")
    return render(request, 'rango/restricted.html', {})


def track_url(request):
    if "page_id" in request.GET:
        page_id = request.GET['page_id']
        page = CatPage.objects.get(id=page_id)

        page.views += 1
        page.save()

    return HttpResponseRedirect(page.url)


@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))

        if cat:
            likes = cat.likes + 1
            cat.likes = likes
            cat.save()

            user = request.user
            cat_user_like = CategoryUserLikes(
                user=user,
                category=cat
            )
            cat_user_like.save()

    return HttpResponse(likes)


@login_required
def dislike_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))

        if cat:
            likes = cat.likes - 1
            cat.likes = likes
            cat.save()

            user = request.user
            cat_user_like = CategoryUserLikes.objects.filter(user=user).filter(category=cat)
            cat_user_like.delete()

    return HttpResponse(likes)


def get_category_list(max_results=0, cat_search_keyword=''):
    cat_list = []
    if cat_search_keyword:
        cat_list = Category.objects.filter(name__contains=cat_search_keyword)
        # print cat_list
        cat_list = Category.objects.filter(no__contains=cat_search_keyword)
        cat_list = list(set(cat_list))
    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list


def suggest_category(request):
    cat_list = []
    cat_search_keyword = ''
    if request.method == 'GET':
        cat_search_keyword = request.GET['suggestion']

    if cat_search_keyword != '' and cat_search_keyword is not None:
        cat_list = get_category_list(0, cat_search_keyword)
    else:
        cat_list = Category.objects.order_by('-likes')[0:5]

    return render(request, 'rango/parts/nav/cats_search_list.html', {'cats': cat_list})
    # return render(request, 'rango/cats.html', {'cats': cat_list})
    # return HttpResponse({'cat_list': cat_list})


def edit_description_view(request):
    # form = TestUEditorForm()
    form = TestUeditorModelForm()
    return render(request, 'rango/edit-description.html', {"form": form})


def add_answer(request, category_name_slug):
    answered = False

    if request.method == 'POST':
        form = TestUeditorModelForm(request.POST)

        if form.is_valid():
            content = form.save(commit=True)
            content.save()

            cat = Category.objects.get(slug=category_name_slug)
            user = request.user
            print user
            title = request.POST.get('title')
            content = request.POST.get('content')
            current_time = timezone.now()
            # current_time = datetime.now()

            answer = Answers(
                category=cat,
                author=user,
                title=title,
                content=content,
                post_date=current_time
            )
            answer.save()
            answered = True

            return HttpResponseRedirect('/rango/category/'+category_name_slug)


@login_required
def delete_cat_page(request):
    page_id = None
    if request.method == 'GET':
        page_id = request.GET['page_id']

    return_code = -1
    if page_id:
        page = CatPage.objects.get(id=int(page_id))

        page.delete()
        return_code = 1

    date = {"return_code": return_code}
    return JsonResponse(date)


def get_subject_list(max_results=0, cat_search_keyword=''):
    cat_list = []
    if cat_search_keyword:
        sub_list = Subject.objects.filter(name__contains=cat_search_keyword)
        # print cat_list
        sub_list = Subject.objects.filter(no__contains=cat_search_keyword)
        sub_list = list(set(cat_list))
    else:
        sub_list = Subject.objects.all()

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list
