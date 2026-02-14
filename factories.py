class ProductFactory(factory.Factory):
   class Meta:
       model = Product
   id = factory.Sequence(lambda n: n)
   name = factory.Faker('word')
   category = factory.Faker('word')
   price = factory.Faker('random_number', digits=5)
   available = factory.Faker('boolean')
