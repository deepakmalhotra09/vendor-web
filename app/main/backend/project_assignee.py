from app.models import ProjectVendorAssign


class ProjectAssigneeService(object):
    def __init__(self):
        self.ProjectVendorAssign = ProjectVendorAssign

    @staticmethod
    def add_update_project_vendor_assignee(project_vendor_assign: ProjectVendorAssign):
        project_vendor_assign.save()

    @staticmethod
    def get_project_vendor_assignees():
        project_vendor_assign_obj = ProjectVendorAssign.objects.all()
        return project_vendor_assign_obj

    @staticmethod
    def delete_project_vendor_assignee(project_vendor_assign_id: int) -> None:
        ProjectVendorAssign.objects.filter(id=project_vendor_assign_id).delete()
        return None

    @staticmethod
    def get_project_vendor_assignee(id: int):
        project_vendor_assign = ProjectVendorAssign.objects.get(id=id)
        if project_vendor_assign:
            return project_vendor_assign
        return ProjectVendorAssign()

    @staticmethod
    def get_project_vendor_assignee_by_vendor_project_id(vendor_id: int, project_id: int) -> ProjectVendorAssign:
        project_vendor_assign = None
        try:
            project_vendor_assign = ProjectVendorAssign.objects.get(vendor_id=vendor_id, project_id=project_id)
        except Exception:
            print('Exception occured in "get_project_vendor_assignee_by_vendor_project_id" method')
        finally:
            return project_vendor_assign
