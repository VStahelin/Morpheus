from rest_framework import serializers

from api.tracker.models import Entries


class EntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = "__all__"


class GetProtocolEntriesByUserSerializer(serializers.Serializer):
    UserId = serializers.CharField()
    ProtocolId = serializers.CharField()
    DateFrom = serializers.DateField()
    DateTo = serializers.DateField()

    def validate(self, attrs):

        protocol_id = attrs.get("ProtocolId")
        date_from = attrs.get("DateFrom")
        date_to = attrs.get("DateTo")
        user_id = attrs.get("UserId")

        if not user_id:
            raise serializers.ValidationError("Must include 'user_id'.")
        if not protocol_id:
            raise serializers.ValidationError("Must include 'protocol_id'.")
        if not date_from and not date_to:
            raise serializers.ValidationError("Must include 'date_from' and 'date_to'.")
        if date_from > date_to:
            raise serializers.ValidationError("date_from must be less than date_to.")

        return {
            "user_id": user_id,
            "protocol_id": protocol_id,
            "date_from": date_from,
            "date_to": date_to,
        }
