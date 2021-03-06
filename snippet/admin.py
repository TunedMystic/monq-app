from django.contrib import admin
from snippet.models import Snippet, SnippetExtras


@admin.register(SnippetExtras)
class SnippetExtrasAdmin(admin.ModelAdmin):
  """
  SnippetExtras model. Displays basic info.
  """
  # Editing a single instance.
  fieldsets = [
    ("General", {"fields": ["hits", "getLikes"]})
  ]
  readonly_fields = ("getLikes",)
  # Displaying all instances.
  list_display = ("__str__", "hits", "getLikes")


class SnippetExtrasInline(admin.StackedInline):
  """
  SnippetExtras info to be displayed along with a single Snippet instance.
  """
  model = SnippetExtras
  can_delete = False
  # Editing a single instance.
  fields = ("hits", "getLikes")
  readonly_fields = ("getLikes",)


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
  """
  Snippet model. Displays all attributes as well as the SnippetExtras instance.
  """
  fieldsets = [
    ("Snippet Info", {"fields": ["title", "language", "content"]}),
    ("Privacy", {"fields": ["visibility", "password"]}),
    ("General", {"fields": ["author", "url_code", "tags"]})
  ]
  readonly_fields = ("password",)
  list_display = ("title", "author", "language", "date_added_raw", "visibility")
  # Enable filtering.
  list_filter = ("date_added_raw",)
  # Results per page.
  list_per_page = 30
  # Enabling searching.
  search_fields = ["title", "language"]
  inlines = [
    SnippetExtrasInline
  ]
