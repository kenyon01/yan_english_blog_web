from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import AnswerForm

def my_new_page(request):
    question = Question.objects.first()  # 示例：获取第一个问题
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            Answer.objects.create(
                question=question,
                text=form.cleaned_data['text']
            )
            return redirect('displaytext:my_new_page')  # 重定向以避免重复提交
    else:
        form = AnswerForm()
    
    return render(request, 'displaytext/my_new_page.html', {'question': question, 'form': form})


