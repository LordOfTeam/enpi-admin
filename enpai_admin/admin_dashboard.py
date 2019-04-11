from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard


class BackendDashboard(Dashboard):
    """
    后台管理Dashboard定制类
    """

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        self.children.append(modules.ModelList(
            _('系统用户管理(仅限超级管理员使用)'),
            collapsible=True,
            column=2,
            # exclude=('django.contrib.*',),
            models=('django.contrib.*',
                    )
        ))
        self.children.append(modules.LinkList(
            _('图片/文件管理'),
            column=2,
            children=[
                {
                    'title': _('浏览管理器'),
                    'url': '/backend/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        self.children.append(modules.ModelList(
            _('场地管理'),
            column=1,
            collapsible=True,
            models=(
                'backend.models.PlaceInfo',
                'backend.models.HallInfo',
                'backend.models.ImageInfo',
                'backend.models.GuestRoom'
            ),
        ))
        self.children.append(modules.RecentActions(
            _('最近历史'),
            limit=5,
            collapsible=False,
            column=3,
        ))
