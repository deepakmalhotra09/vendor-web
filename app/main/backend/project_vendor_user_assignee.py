from app.models import ProjectVendorAssign, ProjectVendorUserAssign


class ProjectVendorUserAssigneeService(object):
    def __init__(self):
        self.ProjectVendorAssign = ProjectVendorAssign

    @staticmethod
    def add_update_project_vendor_user_assignee(project_vendor_user_assign: ProjectVendorUserAssign):
        project_vendor_user_assign.save()

    @staticmethod
    def get_project_vendor_user_assignees():
        project_vendor_user_assign_obj = ProjectVendorUserAssign.objects.all()
        return project_vendor_user_assign_obj

    @staticmethod
    def delete_project_vendor_user_assignee(project_vendor_user_assign_id: int) -> None:
        ProjectVendorUserAssign.objects.filter(id=project_vendor_user_assign_id).delete()
        return None

    @staticmethod
    def get_project_vendor_user_assignee(id: int):
        project_vendor_user_assign = ProjectVendorUserAssign.objects.get(id=id)
        if project_vendor_user_assign:
            return project_vendor_user_assign
        return ProjectVendorUserAssign()

    @staticmethod
    def get_project_vendor_user_assignee_by_project_vendor_user_id(client_project_id: int, vendor_id: int,
                                                                   user_id) -> ProjectVendorUserAssign:
        project_vendor_user_assign = ProjectVendorUserAssign.objects.get(client_project_id=client_project_id,
                                                                         vendor_id=vendor_id, user_id=user_id)
        if project_vendor_user_assign:
            return project_vendor_user_assign
        return None
