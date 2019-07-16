from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .code.algorithm_call import drug_predict
from .code.algorithm_call import batch_drug_predict
from .code.batch_predict import read_batch_file
from .code.batch_predict import write_to_txt
import os
# Create your views here.


# 系统首页
def get_index_page(request):
    return render(request, 'classification/index.html')


# SMILES输入格式展示页面
def get_smiles_page(request):
    return render(request, 'classification/SMILES.html')


# 系统描述页面
def get_description_page(request):
    return render(request, 'classification/description.html')


# 主要参考文献页面
def get_references_page(request):
    return render(request, 'classification/references.html')


# 批量预测页面
def batch_predict(request):
    return render(request, 'classification/batch_predict.html')


# 药物ATC类别预测
def predict_result(request):
    data = request.GET.get('data')
    predict_dict = drug_predict(data)

    return render(request, 'classification/predict.html',
                  {
                      "predict_dict": predict_dict
                  })


# 发送邮件
def send_email(request):
    recipient_list = []
    if request.method == 'POST':
        file = request.FILES.get('data')
        # 判断是否上传了文件
        if file is None:
            return HttpResponse("请选择要上传的文件！")
        # 判断是否上传了邮箱
        email = request.POST.get('email')
        if email is None:
            return HttpResponse("请输入邮箱！")
        # 判断上传的文件的格式是否为txt
        ext = file.name.split('.')[-1].lower()
        if ext not in ["txt"]:
            return HttpResponse("上传文件格式错误！")
        # 保存文件到static/in_txt
        filename = '%s/%s' % (settings.MEDIA_ROOT, file.name)
        with open(filename, 'wb') as f:
            for ftxt in file.chunks():
                f.write(ftxt)

        # 读取待预测数据
        data = read_batch_file(filename)

        # 进行预测
        predict_result = batch_drug_predict(data)

        # 写入txt文件
        out_path = 'classification/static/out_txt/result.txt'
        write_to_txt(predict_result, out_path)

        # 测试邮箱：gxb55212@163.com
        # 读预测结果，并通过邮箱发送
        content = read_batch_file(out_path)
        recipient_list.append(email)

        # email_msg = EmailMessage("预测结果", from_email=settings.EMAIL_FROM, to=recipient_list)

        # email_msg.attach('prdict_result', content, 'txt')
        # result = email_msg.send()

        result = send_mail('预测结果', content, settings.EMAIL_FROM, recipient_list)
        if result != 0:
            os.remove(filename)
            f = open(out_path, "r+")
            f.truncate()
            return HttpResponse('预测结束，请查看邮箱！')
        else:
            return HttpResponse('预测失败！')


# 打开参考文献
def get_reference(request):
    pdf_name = request.GET.get("pdf")
    pdf_path = 'classification/static/pdf/' + str(pdf_name)
    return HttpResponse(pdf_path)
