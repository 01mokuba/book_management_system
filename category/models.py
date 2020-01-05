from django.db import models

class Category(models.Model):
    """
    本のカテゴリ データ定義クラス
    """

    # カテゴリ名 文字列
    category_name = models.CharField(
        verbose_name='カテゴリ名',
        max_length=20,
        blank=True,
        null=True,
    )

    # 選択リストでの表示
    def __str__(self):
        return self.category_name
