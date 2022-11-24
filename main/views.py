from django.shortcuts import render
from django.http import HttpResponse
from main.models import Post
from django.core.paginator import Paginator
from django.conf import settings
import mimetypes

def homepage(request):
	template_name = "main/index.html"
	all_videos =  Post.objects.all().order_by('id')
	paginator = Paginator(all_videos, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, template_name, {"page_videos": page_obj})

def video(request, id):
	template_name = "main/video.html"
	video =  Post.objects.get(id=id)
	return render(request, template_name, {"video": video})

def tabs(request):
	template_name = "main/tabs.html"
	all_videos =  Post.objects.exclude(tab_gp="").order_by('id')
	paginator = Paginator(all_videos, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, template_name, {"page_videos": page_obj})

def download(request, id, fformat):
	video =  Post.objects.get(id=id)
	if fformat == "pdf":
		file_path = str(settings.BASE_DIR) + video.tab_pdf.url
		file_name = video.tab_pdf.name
	else:
		file_path = str(settings.BASE_DIR) + video.tab_gp.url
		file_name = video.tab_gp.name

	path = open(file_path, 'rb')
	mime_type, _ = mimetypes.guess_type(file_path)
	response = HttpResponse(path, content_type=mime_type)
	response['Content-Disposition'] = "attachment; filename=%s" % file_name
	return response

def contact(request):
	template_name = "main/contact.html"
	return render(request, template_name)
