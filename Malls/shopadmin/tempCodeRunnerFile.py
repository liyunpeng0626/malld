class PmsBrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsBrand
        fields='__all__'
        # fields=("name") 