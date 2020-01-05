from django.apps import AppConfig


class CategoryConfig(AppConfig):
    """
    アプリケーション構成クラス
    管理画面での表示名を指定する
    """
    name = 'category'
    verbose_name = 'カテゴリ管理'
