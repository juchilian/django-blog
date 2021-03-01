from import_export import resources

from .models import BlogPost


class BlogPostResource(resources.ModelResource):

    class Meta:
        model = BlogPost
        skip_unchanged = True
        report_skipped = False
        # import_id_fields = ('name', )