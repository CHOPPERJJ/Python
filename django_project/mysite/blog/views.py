from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Context, Template
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count


# django内置CBV类ListView改写post_list
# class PostListView(ListView):
#     queryset = Post.objects.all()
#     context_object_name = 'posts'   #posts为模板变量名称
#     paginate_by = 3
#     template_name = 'blog/post/list.html'


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，传入首页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果传入的页码超出了限制,传入最后一页
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'tag': tag})


# 显示单独一篇文章的视图函数
def post_detail(request, year, month, days, post):
    post = get_object_or_404(Post,
                             status='published',
                             publish__year=year,
                             # publish__month=month,
                             # publish__day=days,
                             slug=post)

    # 列出文章对应的动态评论
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # 创建表单对象，不保存在数据库中
            new_comment = comment_form.save(commit=False)
            # 指定评论给当前文章
            new_comment.post = post
            # 保存评论到数据库中
            new_comment.save()
    else:
        comment_form = CommentForm()   #空表单

    # 显示相近Tag的文章列表
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:4]

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts})


# 文章表单分享视图界面
def post_share(request, post_id):
    # 通过id获取post对象
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # 表单被提交
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # 验证表单数据
            cd = form.cleaned_data
            # 发送邮件
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) 建议你阅读邮件 "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {} \n\n {}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            recipients = [cd['to']]
            send_mail(subject, message, 'chopper_jj@qq.com', recipients)
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

