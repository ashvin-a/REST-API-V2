from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, unique_aano


class ProductSerializer(serializers.ModelSerializer):
    retail_price = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name="update_details", lookup_field="pk"
    )
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validate_title, unique_aano]
    )  # !put validators
    name = serializers.CharField(source="title", read_only=True)

    # !in models.
    class Meta:
        model = Product
        fields = [
            "id",
            # "user",
            "url",
            "edit_url",
            "title",
            "name",
            "email",
            "content",
            "price",
            "retail_price",
        ]

    """
    Try to put validators in a separate file
    """

    def create(self, validated_data):
        return super().create(validated_data)

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request:
            return reverse(
                "update_details", kwargs={"pk": obj.id}, request=request
            )

    def get_url(self, obj):
        request = self.context.get("request")
        if request:
            return reverse(
                "product_details", kwargs={"pk": obj.id}, request=request
            )
        else:
            return None

    def get_retail_price(self, obj):
        return obj.sale_price
