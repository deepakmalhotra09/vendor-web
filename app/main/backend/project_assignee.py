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
    def delete_project_project_vendor_assignee(project_vendor_assign_id: int) -> None:
        ProjectVendorAssign.objects.filter(id=project_vendor_assign_id).delete()
        return None

    @staticmethod
    def get_project_vendor_assignee(id: int):
        project_vendor_assign_id = ProjectVendorAssign.objects.get(id=id)
        if project_vendor_assign_id:
            return project_vendor_assign_id
        return ProjectVendorAssign()

