from .models import Mattress, Products, Telephones, CompanyInfo


# her to get data for Header to All Views
def header_context(request):
    first_mattress = Mattress.objects.first()
    first_product = Products.objects.first()

    if first_mattress:
        first_mattress = first_mattress.pk
    else:
        first_mattress = 0

    if first_product:
        first_product = first_product.pk
    else:
        first_product = 0

    try:
        sales_phone = Telephones.objects.get(title='المبيعات').number
    except Telephones.DoesNotExist:
        sales_phone = ''

    return {
        'first_mattress_pk': first_mattress,
        'first_product_pk': first_product,
        'header_phone': sales_phone,
    }


# het to get data for FOOTer to all Views
def footer_context(request):
    info = CompanyInfo.objects.first()
    if info:
        return {
            'facebook_link': info.facebook,
            'instagram_link': info.instagram,
        }
    else:
        return {
            'facebook_link': '',
            'instagram_link': '',
        }
