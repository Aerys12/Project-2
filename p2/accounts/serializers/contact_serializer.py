from rest_framework import serializers
from accounts.models.contact import Contact

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.

    This serializer is used to convert Contact model instances into JSON
    representations and vice versa. It specifies the fields to be included
    in the serialized output and provides validation for the input data.

    Attributes:
        model (class): The Contact model class.
        fields (str): A string specifying the fields to be included in the
            serialized output. The value "__all__" indicates that all fields
            should be included.

    """
    class Meta:
        model = Contact
        fields = "__all__"