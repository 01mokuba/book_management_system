from django.db import models

from users.models import User
from category.models import Category


class Book(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 本の名前 文字列
    book_name = models.CharField(
        verbose_name='本の名前',
        max_length=20,
        blank=True,
        null=True,
    )

    # 著者 文字列
    author_name = models.CharField(
        verbose_name='著者',
        max_length=20,
        blank=True,
        null=True,
    )

    # ステータス 選択肢（固定）
    read_status_choice = (
        (1, '読んだけどまた読みたい'),
        (2, '読んだ'),
        (3, '読んでない'),
    )
    read_status = models.IntegerField(
        verbose_name='ステータス',
        choices=read_status_choice,
        blank=True,
        null=True,
    )

    # 読みたい理由 文字列
    read_reason = models.CharField(
        verbose_name='読みたい理由',
        max_length=20,
        blank=True,
        null=True,
    )

    # 関心 ブール値
    is_wonder = models.BooleanField(
        verbose_name='関心が高い',
    )

    # カテゴリ 選択肢（マスタ連動）
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        blank=True,
        null=True,
        related_name='category',
        on_delete=models.SET_NULL,
    )

    # 読み始め 日付
    start_date = models.DateField(
        verbose_name='読み始め',
        blank=True,
        null=True,
    )

    # 読み終わり 日付
    end_date = models.DateField(
        verbose_name='読み終わり',
        blank=True,
        null=True,
    )

    # 書評 メモ
    review = models.TextField(
        verbose_name='書評',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 登録ユーザー
    created_by = models.ForeignKey(
        User,
        verbose_name='登録ユーザー',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 登録時間
    created_at = models.DateTimeField(
        verbose_name='登録時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 最終更新ユーザー
    updated_by = models.ForeignKey(
        User,
        verbose_name='最終更新ユーザー',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 最終更新時間
    updated_at = models.DateTimeField(
        verbose_name='最終更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.book_name

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = '小園家蔵書トラン'
        verbose_name_plural = '小園家蔵書トラン'
