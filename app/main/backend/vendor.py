from app.models import Vendor


class VendorService(object):
    def __init__(self):
        self.Vendor = Vendor

    @staticmethod
    def add_update_vendor(vendor: Vendor):
        vendor.save()

    @staticmethod
    def get_vendors():
        vendors_obj = Vendor.objects.all()
        return vendors_obj

    @staticmethod
    def get_total_vendor_count():
        vendors_obj = Vendor.objects.all().count()
        return vendors_obj

    @staticmethod
    def delete_vendor(vendor_id: int) -> None:
        Vendor.objects.filter(id=vendor_id).delete()
        return None

    @staticmethod
    def get_vendor(id: int):
        vendor = Vendor.objects.get(id=id)
        if vendor:
            return vendor
        return Vendor()

    @staticmethod
    def get_vendor_by_name(vendor_name: str):
        vendor = Vendor.objects.get(name=vendor_name)
        if vendor:
            return vendor
        return Vendor()
