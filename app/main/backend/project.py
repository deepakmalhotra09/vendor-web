from app.models import Project


class ProjectService(object):
    def __init__(self):
        self.Project = Project

    @staticmethod
    def add_update_project(project: Project):
        project.save()

    @staticmethod
    def get_projects():
        project_obj = Project.objects.all()
        return project_obj

    @staticmethod
    def get_total_project_count():
        project_obj = Project.objects.all().count()
        return project_obj


    @staticmethod
    def delete_project(project_id: int) -> None:
        Project.objects.filter(id=project_id).delete()
        return None

    @staticmethod
    def get_project(id: int):
        project = Project.objects.get(id=id)
        if project:
            return project
        return Project()

    @staticmethod
    def get_project_by_name(project_name: str):
        project = Project.objects.get(name=project_name)
        if project:
            return project
        return Project()
