from django.shortcuts import render, reverse, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from . import models
from mainapp.models import Course, Section, CourseItem
import requests


def home(request):
    courses = Course.objects.all()
    sections = Section.objects.all()
    items = CourseItem.objects.all()
    context = {"courses": courses, "sections": sections, "items": items}
    return render(request, 'home.html', context)


def course(request, course_name):
    course = get_object_or_404(models.Course, title__iexact=course_name)
    context = {"course": course}
    return render(request, 'course.html', context)


def section(request, course_name, section_name):
    section = models.Section.objects.filter(title=section_name)
    context = {"section": section}
    return render(request, 'section.html', context)


def item(request, course_name, section_name, item_name):
    item = models.CourseItem.objects.filter(title=item_name)
    context = {"item": item}
    return render(request, 'item.html', context)


def update_course(request):
    data = requests.get("http://iq.opengenus.org/ghost/api/v0.1/posts/?client_id=ghost-frontend&client_secret=06875a67"
                        "cb74").json()
    course_list = data.get("posts")
    for course in course_list:
        course_article_id = course.get("id")
        section_title = course.get("title")
        description = course.get("custom_excerpt")
        course_item_title = section_title + " Course Item"
        if ":" in section_title:
            course_title = section_title.substring(0, section_title.index(":"))
        else:
            course_title = section_title
        section_author = course.get("author")
        course_instance = Course.objects.create(title=course_title, description='',
                                                authors='', duration='', level='', audience='')
        new_course = Course.objects.get(title=course_title)
        section_instance = Section.objects.create(courseId=new_course, title=section_title,
                                                  description=description, authors=section_author, duration='')
        new_section = Section.objects.get(title=section_title)
        course_item_instance = CourseItem.objects.create(courseId=new_course, sectionId=new_section,
                                                         title=course_item_title, sideLink=course_article_id,
                                                         codeLink=course_article_id, textExplanation=description)
        course_instance.save()
        section_instance.save()
        course_item_instance.save()

    return render(request, 'home.html')
