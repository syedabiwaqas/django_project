from rest_framework import serializers
from .models import Books,Author



class BookSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    author = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=1000)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = Books
        fields = ['id','name','description','author','price','quantity','pulished_on']
    

class BookUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(max_length=1000)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    quantity = serializers.IntegerField(required=True)
    
    class Meta:
        model = Books
        fields = ['id','name','description','author','price','quantity','pulished_on']
        read_only_fields = ('id',)
        depth=1
         #depth=1 is use full if we have foreign key refrences so we dont have to itterate over them 
        # django serializer does for us 1 defines the level of refrences you want to carry on

    #this method will get called when we use patch or put method corresonding to this method.
    def update(self, instance, validated_data):
         # validated_data.get('name', instance.name) means to update the 
        # new value if it comes or keep the existing one
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantiy = validated_data.get('quantiy', instance.price)
        instance.save()
        return instance


class AuthorUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100)  #validating lenght and required true
    username = serializers.CharField(required=True,max_length=100)
    
    class Meta:
        model = Author
        fields = ['id','name','username','createdat']
        read_only_fields = ('id',)
        depth=1 
        #depth=1 is use full if we have foreign key refrences so we dont have to itterate over them 
        # django serializer does for us 1 defines the level of refrences you want to carry on
    
    #this method will get called when we use patch or put method corresonding to this method.
    def update(self, instance, validated_data):
        # validated_data.get('name', instance.name) means to pudate the 
        # new value if it comes or keep the existing one
        instance.name = validated_data.get('name', instance.name) 
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantiy = validated_data.get('quantiy', instance.price)
        instance.save()
        return instance

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=100) #validating lenght and required true
    username = serializers.CharField(required=True,max_length=225)

    class Meta:
        model = Author
        fields = ['id','name','username','createdat']