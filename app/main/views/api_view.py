from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect

from app.models import ProjectVendorUserAssign
from main.backend.factory import Factory


def api_vendor_view(request: HttpRequest, params: str):
    vendor_project_id = request.GET['pid']
    user_id = request.GET['uid']
    vendor_project_id_arr = vendor_project_id.split('_')
    vendor_id = vendor_project_id_arr[0]
    project_id = vendor_project_id_arr[1]
    factory = Factory()
    project_assignee_service = factory.get_service('project-assignee')
    project_vendor_user_assignee_service = factory.get_service('project-vendor-user-assignee')
    project_vendor_assignee = project_assignee_service.get_project_vendor_assignee_by_vendor_project_id(vendor_id,
                                                                                                        project_id)
    if project_vendor_assignee:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            user_ip_address = x_forwarded_for.split(',')[0]
        else:
            user_ip_address = request.META.get('REMOTE_ADDR')
        client_project_id = project_vendor_assignee.client_project_id
        project_vendor_user_assign = ProjectVendorUserAssign()
        project_vendor_user_assign.vendor_id = vendor_id
        project_vendor_user_assign.project_id = project_id
        project_vendor_user_assign.client_project_id = client_project_id
        project_vendor_user_assign.user_id = user_id
        project_vendor_user_assign.ip_address = user_ip_address
        try:
            project_vendor_user_assignee_service.add_update_project_vendor_user_assignee(project_vendor_user_assign)
        except Exception:
            return JsonResponse('Something went wrong', safe=False)
        project_service = factory.get_service('project')
        project = project_service.get_project(project_id)
        client_project_link = project.link
        client_link = "{0}?pid={1}&uid={2}_{3}".format(client_project_link, client_project_id, vendor_id, user_id)
        return redirect(client_link)
    return JsonResponse('You are not assign for this Project', safe=False)


def api_client_view(request: HttpRequest, params: str):
    client_project_id = request.GET['pid']
    client_user_id = request.GET['uid']
    status = request.GET['status']
    client_user_id_arr = client_user_id.split('_')
    vendor_id = client_user_id_arr[0]
    user_id = client_user_id_arr[1]
    factory = Factory()
    project_vendor_user_assignee_service = factory.get_service('project-vendor-user-assignee')
    project_vendor_user_assignee = project_vendor_user_assignee_service.get_project_vendor_user_assignee_by_project_vendor_user_id(
        client_project_id, vendor_id, user_id)
    if project_vendor_user_assignee:
        project_vendor_user_assignee.status = status
        project_vendor_user_assignee_service.add_update_project_vendor_user_assignee(project_vendor_user_assignee)
        project_vendor_assignee_service = factory.get_service('project-assignee')
        project_id = project_vendor_user_assignee.project_id
        try:
            project_vendor_assignee = project_vendor_assignee_service.get_project_vendor_assignee_by_vendor_project_id(vendor_id, project_id)
        except Exception:
            return JsonResponse('Something went wrong', safe=False)
        vendor_links = eval(project_vendor_assignee.links)
        vendor_link = vendor_links.get(status, '')
        if vendor_link:
            return redirect(vendor_link)
        else:
            return JsonResponse('Error found', safe=False)
    return JsonResponse('You are not assign for this Project', safe=False)
