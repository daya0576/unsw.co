# coding: utf-8

from django.utils import timezone
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from rango.models import Category, CatPage, SubPage, Answers, CategoryUserLikes, Subject, AnswerUserLikes, AnswerUserDislikes, User, UserOOXX
from rango.forms import CategoryForm, CatPageForm, SubPageForm, UserForm, TestUeditorModelForm, UserOOXXForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Q


# def index(request):
#     print request.META
#     print request.method
#
#     return HttpResponse("Rango says hey there world<br>"
#                         "<a href='/rango/about'>About</a>")


def index(request):
    category_list = Category.objects.extra(
            select={
                'answer_count': 'select count(*) from rango_answers where rango_answers.category_id = rango_category.id'
            },
        ).order_by('-answer_count')[0:10]
    # page_list = CatPage.objects.order_by('-views')[0:5]
    subject_list = Subject.objects.order_by('-likes').filter(~Q(slug="both"))

    context_dict = {'categories': category_list, 'subs': subject_list}

    # visits = request.session.get('visits')
    # if not visits:
    #     visits = 1
    # reset_last_visit_time = False
    #
    # last_visit = request.session.get('last_visit')
    # if last_visit:
    #     last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
    #
    #     if(datetime.now() - last_visit_time).seconds > 0:
    #         visits += 1
    #         reset_last_visit_time = True
    # else:
    #     reset_last_visit_time = True
    #
    # if reset_last_visit_time:
    #     last_visit_time = str(datetime.now())
    #     request.session['last_visit'] = last_visit_time
    #     request.session['visits'] = visits
    #
    # context_dict['last_visit'] = last_visit
    # context_dict['visits'] = visits

    response = render(request, 'rango/index.html', context_dict)
    # response = HttpResponseRedirect('/rango/subject/master-of-information-technology/')
    # response = category(request, "master-of-information-technology")

    return response


def about(request):
    content_dict = {'boldmessage': 'Could u tell me something about yourself?'}

    if request.session.get('visits'):
        count = request.session.get('visits')
    else:
        count = 0

    content_dict['visits'] = count

    return render(request, 'rango/about.html', content_dict)


def get_answer_like_users(answer):
    like_users_str = ""

    users_like = AnswerUserLikes.objects.filter(answer=answer).order_by("-time")
    users_dislike = AnswerUserDislikes.objects.filter(answer=answer)
    users_like_num = len(users_like)
    users_dislike_num = len(users_dislike)

    for i in range(len(users_like)):
        if users_like[i].user.first_name != "" and users_like[i].user.first_name is not None:
            users_like[i].user.username = users_like[i].user.first_name

    if users_like_num == 0:
        like_users_str = ""
    elif users_like_num == 1:
        like_users_str = users_like[0].user.username+" likes this"
    elif 0 <= users_like_num <= 3:
        like_users_str = ""
        for i, user_like in enumerate(users_like):
            if i == len(users_like)-1:
                like_users_str += user_like.user.username+" "
            else:
                like_users_str += user_like.user.username+", "
        like_users_str += "like this"
    else:
        like_users_str = users_like[0].user.username + ', ' + \
                         users_like[1].user.username + ', ' + \
                         users_like[2].user.username
        like_users_str += ".. like this"

    # print users_dislike_num, users_like_num
    if users_dislike_num > 0 and users_like_num > 0:
        like_users_str += ", %d person dislike" % users_dislike_num
    elif users_dislike_num > 0 and users_like_num == 0:
        like_users_str += "%d person dislike" % users_dislike_num

    return like_users_str


def get_category(request, cat_name_slug):
    context_dict = {}
    return_code = 1

    if request.method == 'POST':
        editor_form = TestUeditorModelForm(request.POST)

        if editor_form.is_valid():
            content = editor_form.save(commit=True)
            content.save()

            cat = Category.objects.get(slug=cat_name_slug)
            user = request.user
            content = request.POST.get('content')
            current_time = timezone.now()
            # current_time = datetime.now()

            answer = Answers(
                category=cat,
                author=user,
                content=content,
                post_date=current_time,
                edit_date=current_time
            )
            answer.save()
            return HttpResponseRedirect('/rango/category/' + cat_name_slug)
        else:
            print "form.errors", editor_form.errors
            return_code = -1
    else:
        editor_form = TestUeditorModelForm()
        return_code = 0

    try:
        user = request.user
        if user.is_authenticated():
            user_id = user.id
        else:
            user_id = -1

        category = Category.objects.get(slug=cat_name_slug)
        pages = CatPage.objects.filter(category=category)
        answers = Answers.objects.filter(category=category).extra(
        #     select={
        #         'answer_likes': 'select count(*) from rango_answeruserlikes where rango_answers.id = rango_answeruserlikes.answer_id'
        #     },
        # ).extra(
        #     select={
        #         'answer_dislikes': 'select count(*) from rango_answeruserdislikes where rango_answers.id = rango_answeruserdislikes.answer_id'
        #     },
        # ).extra(
            select={
                'is_liked': 'select count(*) from rango_answeruserlikes where rango_answers.id = rango_answeruserlikes.answer_id and rango_answeruserlikes.user_id = ' + str(user_id)
            },
        ).extra(
            select={
                'is_disliked': 'select count(*) from rango_answeruserdislikes where rango_answers.id = rango_answeruserdislikes.answer_id and rango_answeruserdislikes.user_id = ' + str(user_id)
            },
        ).order_by("-likes")

        # answers.order_by('-edit_date')

        if user.is_authenticated():
            is_liked = CategoryUserLikes.objects.filter(category=category).filter(user=request.user)
        else:
            is_liked = None

        # like persons.
        is_answered = False
        for answer in answers:
            # print answer.likes
            answer.like_users_str = get_answer_like_users(answer)

            if answer.author == user:
                is_answered = True

            answer.user_id = answer.author.id

        context_dict['pages'] = pages
        context_dict['answers'] = answers
        context_dict['category'] = category
        context_dict['cat_name_slug'] = cat_name_slug
        context_dict['editor'] = editor_form
        context_dict['is_liked'] = is_liked
        context_dict['is_answered'] = is_answered
        context_dict['subject'] = category.subject

        context_dict['return_code'] = return_code

    except Category.DoesNotExist:
        context_dict = {}

    return render(request, 'rango/category.html', context_dict)


def subject(request, sub_name_slug):
    context_dict = {}
    if "order" in request.GET:
        order = int(request.GET['order'])
    else:
        order = 0

    if "keyword" in request.GET:
        keyword = request.GET['keyword']
    else:
        keyword = ''

    try:
        subject = Subject.objects.get(slug=sub_name_slug)
        subject_both = Subject.objects.get(slug="both")

        if subject.name == "UEEC":
            cats = Category.objects.filter(subject=subject).extra(
                select={
                    'answer_count': 'select count(*) from rango_answers where rango_answers.category_id = rango_category.id'
                },
            )
        else:
            cats = Category.objects.filter(Q(subject=subject) | Q(subject=subject_both)).extra(
                select={
                    'answer_count': 'select count(*) from rango_answers where rango_answers.category_id = rango_category.id'
                },
            )

        # searching by keyword
        if keyword is not '':
            cats = cats.filter(Q(name__contains=keyword) | Q(no__contains=keyword))
            context_dict['keyword'] = keyword
        else:
            context_dict['keyword'] = ""

        # sort by answers, likes or level
        if order == 0:
            cats = cats.order_by('-answer_count')
        elif order == 1:
            cats = cats.order_by('-likes')
        elif order == 2:
            cats = cats.order_by('level')
        elif order == 20:
            cats = cats.filter(level=0).order_by('-answer_count')
        elif order == 21:
            cats = cats.filter(level=1).order_by('-answer_count')
        elif order == 22:
            cats = cats.filter(level=2).order_by('-answer_count')
        elif order == 23:
            cats = cats.filter(level=3).order_by('-answer_count')

        # get the first one useful tips.
        # for cat in cats:
        #     if cat.no == "Other useful info":
        #         context_dict["cat_tips"] = cat
        #
        #         break

        context_dict['subject'] = subject
        context_dict['cats'] = cats
        context_dict['sub_name_slug'] = sub_name_slug
        context_dict['order'] = order
        # context_dict['act_sub'] = subject
    except Subject.DoesNotExist:
        context_dict = {}

    return render(request, 'rango/subject.html', context_dict)


def add_category(request, sub_name_slug):
    context_dict = {}
    try:
        subject = Subject.objects.get(slug=sub_name_slug)
    except Subject.DoesNotExist:
        print "Subject does not exit!"

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat = form.save(commit=False)
            cat.subject = subject
            cat.save()
        else:
            print "form.errors", form.errors

        return HttpResponseRedirect('/rango/'+'subject/'+sub_name_slug)
    else:
        form = CategoryForm()
        context_dict['form'] = CategoryForm()
        context_dict['sub_name_slug'] = sub_name_slug

        return render(request, 'rango/add_category.html', context_dict)


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
                # response.set_cookie("postToken",value='disable')
                response = HttpResponseRedirect('/rango/category/'+category_name_slug)
            else:
                # print "form.errors", form.errors

                context_dict = {'form': form, 'category': cat, 'category_name_slug': category_name_slug}
                response = render(request, 'rango/add_page.html', context_dict)
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
        cat_list = list(Category.objects.filter(name__contains=cat_search_keyword))
        cat_list += list(Category.objects.filter(no__contains=cat_search_keyword))
        cat_list = list(set(cat_list))
    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list


def suggest_category(request):
    cats = []
    cat_search_keyword = ''
    if request.method == 'GET':
        cat_search_keyword = request.GET['suggestion']
        cat_search_keyword = cat_search_keyword.rstrip()

        if cat_search_keyword != '' and cat_search_keyword is not None:
            cats = get_category_list(0, cat_search_keyword)
            context_dict = {'cats': cats}
        else:
            subs = Subject.objects.all().filter(~Q(slug="both"))
            context_dict = {'subs': subs}

        return render(request, 'rango/parts/navbar/cats_li.html', context_dict)
        # return render(request, 'rango/cats.html', {'cats': cat_list})
        # return HttpResponse({'cat_list': cat_list})


@login_required
def add_answer(request, category_name_slug):

    if request.method == 'POST':
        form = TestUeditorModelForm(request.POST)

        if form.is_valid():
            content = form.save(commit=True)
            content.save()

            cat = Category.objects.get(slug=category_name_slug)
            user = request.user
            content = request.POST.get('content')
            current_time = timezone.now()
            # current_time = datetime.now()

            answer = Answers(
                category=cat,
                author=user,
                content=content,
                post_date=current_time,
                edit_date=current_time
            )
            answer.save()
        else:
            print "form.errors", form.errors

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
        sub_list.filter(~Q(slug="both"))
        sub_list = list(set(cat_list))
    else:
        sub_list = Subject.objects.all().filter(~Q(slug="both"))

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list


@login_required
def delete_answer(request):
    answer_id = None
    if request.method == 'GET':
        answer_id = request.GET['answer_id']
    return_code = -1
    if answer_id:
        answer = Answers.objects.get(id=int(answer_id))

        answer.delete()
        return_code = 1

    date = {"return_code": return_code}
    return JsonResponse(date)


@login_required
def add_answer(request, cat_name_slug):

    if request.method == 'POST':

        form = TestUeditorModelForm(request.POST)
        # answer_id = request.GET['answer_id']
        # next_page = request.GET['next']

        if form.is_valid():
            content = form.save(commit=True)
            content.save()

            cat = Category.objects.get(slug=cat_name_slug)
            user = request.user
            content = request.POST.get('content')
            current_time = timezone.now()
            # current_time = datetime.now()

            answer = Answers(
                category=cat,
                author=user,
                content=content,
                post_date=current_time,
                edit_date=current_time
            )
            answer.save()
        else:
            print "form.errors", form.errors

        return HttpResponseRedirect('/rango/category/'+cat_name_slug)
    else:
        form = TestUeditorModelForm()

    context = {"form": form, "cat_name_slug": cat_name_slug}

    return render(request, 'rango/edit-description.html', context)


@login_required
def edit_answer(request, cat_name_slug, answer_id):
    answer = Answers.objects.get(id=int(answer_id))
    if answer.author == request.user:
        if request.method == 'POST':
            form = TestUeditorModelForm(request.POST)
            # answer_id = request.GET['answer_id']
            # next_page = request.GET['next']

            if form.is_valid():
                answer = Answers.objects.get(id=int(answer_id))

                content = request.POST.get('content')
                current_time = timezone.now()

                answer.content = content
                answer.edit_date = current_time
                answer.save()

                return HttpResponseRedirect('/rango/category/'+cat_name_slug)

        else:
            form = TestUeditorModelForm(
                initial={
                    'content': answer.content,
                }
            )

        context = {"form": form, "answer_id": answer_id, "cat_name_slug": cat_name_slug}

        return render(request, 'rango/edit-description.html', context)
    else:
        return HttpResponse("<h1>Don't do it, stupid!</h1>")


def answer_up(request):
    likes_count = 0
    return_code = -1
    date = {}

    if request.method == 'GET':
        answer_id = request.GET['answer_id']
        if answer_id:
            user = request.user
            answer = Answers.objects.get(id=int(answer_id))
            current_time = timezone.now()

            answer_like = AnswerUserLikes(
                answer=answer,
                user=user,
                time=current_time
            )
            answer_like.save()

            user_dislike = AnswerUserDislikes.objects.filter(answer=answer).filter(user=user)
            if user_dislike.count() > 0:
                user_dislike.delete()

            likes = AnswerUserLikes.objects.filter(answer=answer)
            dislikes = AnswerUserDislikes.objects.filter(answer=answer)
            likes_count = likes.count() - dislikes.count()

            answer.likes = likes_count
            answer.save()

            return_code = 1

    date["return_code"] = return_code
    date["likes_count"] = likes_count
    date["likes_person"] = get_answer_like_users(answer)
    return JsonResponse(date)


def answer_up_off(request):
    likes_count = 0
    return_code = -1
    date = {}

    if request.method == 'GET':
        answer_id = request.GET['answer_id']
        if answer_id:
            user = request.user
            answer = Answers.objects.get(id=int(answer_id))

            dislikes = AnswerUserDislikes.objects.filter(answer=answer)
            likes = AnswerUserLikes.objects.filter(answer=answer)

            user_likes = AnswerUserLikes.objects.filter(answer=answer).filter(user=user)
            user_likes.delete()

            likes_count = likes.count() - dislikes.count()
            answer.likes = likes_count
            answer.save()

            return_code = 1

    date["return_code"] = return_code
    date["likes_count"] = likes_count
    date["likes_person"] = get_answer_like_users(answer)

    return JsonResponse(date)


def answer_down(request):
    likes_count = 0
    return_code = -1
    date = {}

    if request.method == 'GET':
        answer_id = request.GET['answer_id']
        if answer_id:
            user = request.user
            answer = Answers.objects.get(id=int(answer_id))
            current_time = timezone.now()

            answer_dislike = AnswerUserDislikes(
                answer=answer,
                user=user,
                time=current_time
            )
            answer_dislike.save()

            user_like = AnswerUserLikes.objects.filter(answer=answer).filter(user=user)
            if user_like.count() > 0:
                user_like.delete()

            likes = AnswerUserLikes.objects.filter(answer=answer)
            dislikes = AnswerUserDislikes.objects.filter(answer=answer)
            likes_count = likes.count() - dislikes.count()

            answer.likes = likes_count
            answer.save()

            return_code = 1

    date["return_code"] = return_code
    date["likes_count"] = likes_count
    date["likes_person"] = get_answer_like_users(answer)

    return JsonResponse(date)


def answer_down_off(request):
    likes_count = 0
    return_code = -1
    date = {}

    if request.method == 'GET':
        answer_id = request.GET['answer_id']
        if answer_id:
            user = request.user
            answer = Answers.objects.get(id=int(answer_id))

            dislikes = AnswerUserDislikes.objects.filter(answer=answer)
            likes = AnswerUserLikes.objects.filter(answer=answer)

            user_dislikes = AnswerUserDislikes.objects.filter(answer=answer).filter(user=user)
            user_dislikes.delete()

            likes_count = likes.count() - dislikes.count()
            answer.likes = likes_count
            answer.save()

            return_code = 1

    date["return_code"] = return_code
    date["likes_count"] = likes_count
    date["likes_person"] = get_answer_like_users(answer)

    return JsonResponse(date)


def member(request, author):
    tar_user = User.objects.get(username=author)
    cur_user = request.user
    return_code = 0

    user_details = UserOOXX.objects.filter(user=tar_user)

    if request.method == 'POST':
        form = UserOOXXForm(request.POST)
        # answer_id = request.GET['answer_id']
        # next_page = request.GET['next']

        if form.is_valid():
            mem_ooxx = form.save(commit=False)
            mem_ooxx.user = request.user
            mem_ooxx.save()
            return_code = 1
            return HttpResponseRedirect('/rango/member/'+tar_user.username)
    else:
        if tar_user == cur_user:
            form = UserOOXXForm()
        else:
            form = None

    context = {"form": form, "member": tar_user, "user_details": user_details, "returncode": return_code}

    return render(request, 'rango/member.html', context)


def member_detail_delete(request, detail_id):
    member = UserOOXX.objects.get(id=int(detail_id))
    member.delete()
    returncode = 1

    date = {"return_code": returncode}
    return JsonResponse(date)


def sub_search(request):
    cats = []
    cat_search_keyword = ''
    if request.method == 'GET':
        cat_search_keyword = request.GET['suggestion']
        sub_name_slug = request.GET['sub_name_slug']

        cat_search_keyword = cat_search_keyword.rstrip()

        context_dict = {}

        try:
            subject = Subject.objects.get(slug=sub_name_slug)
            subject_both = Subject.objects.get(slug="both")

            if subject.name == "UEEC":
                cats = Category.objects.\
                        filter(Q(name__contains=cat_search_keyword) | Q(no__contains=cat_search_keyword)).\
                        filter(subject=subject).extra(

                    select={
                        'answer_count': 'select count(*) from rango_answers where rango_answers.category_id = rango_category.id'
                    },
                )
            else:
                cats = Category.objects. \
                        filter(Q(name__contains=cat_search_keyword) | Q(no__contains=cat_search_keyword)).\
                        filter(Q(subject=subject) | Q(subject=subject_both)).extra(

                    select={
                        'answer_count': 'select count(*) from rango_answers where rango_answers.category_id = rango_category.id'
                    },
                )

            context_dict['subject'] = subject
            context_dict['cats'] = cats
            context_dict['sub_name_slug'] = sub_name_slug
            # context_dict['act_sub'] = subject
        except Subject.DoesNotExist:
            context_dict = {}

        return render(request, 'rango/parts/subject/cats.html', context_dict)


def avatar_doom(request):
    return render(request, 'rango/doom/avatar.html', {})

