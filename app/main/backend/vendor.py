from app.models import Vendor


class VendorService(object):
    def __init__(self):
        self.Vendor = Vendor

    @staticmethod
    def add_vendor(vendor: Vendor):
        vendor.save()

    @staticmethod
    def get_vendors():
        vendors_obj = Vendor.objects.all()
        return vendors_obj

    @staticmethod
    def delete_vendor(vendor_id: int) -> None:
        Vendor.objects.filter(id=vendor_id).delete()
        return None
