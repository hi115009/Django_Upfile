import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
	if request.method == "POST":
		files=[]
		location='media' # 想要儲存的目錄
		# 如果需要上傳一個以上的檔案，修改下方程式碼，並搭配for迴圈就可完成
		picurl=["file1"]		
		files.append(request.FILES.get(picurl[0]))

		for upfile in files:
			if upfile != '':
				if not os.path.exists(location):
					os.makedirs(location)
				fss = FileSystemStorage(location=location)
				file_save= fss.save(upfile.name,upfile)
	return render(request, "index.html",{})

# FileSystemStorage 文件 -> https://docs.djangoproject.com/en/2.0/ref/files/storage/