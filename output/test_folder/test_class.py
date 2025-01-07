class Products(models.Model):
    """
    Products model.
    
    Represents a product in the system.  This model stores information about a product's
    details, pricing, descriptions, and relationships to other models such as SubCategories
    and MerchantUsers.
    
    Attributes:
        id (AutoField): Primary key for the product.
        url_slug (CharField): URL-friendly slug for the product.
        subcategories_id (ForeignKey): Foreign key referencing the SubCategories model, indicating the product's subcategory.
        product_name (CharField): Name of the product.
        brand (CharField): Brand of the product.
        product_max_price (CharField): Maximum price of the product.
        product_discount_price (CharField): Discounted price of the product.
        product_description (TextField): Short description of the product.
        product_long_description (TextField): Detailed description of the product.
        created_at (DateTimeField): Timestamp indicating when the product was created.
        added_by_merchant (ForeignKey): Foreign key referencing the MerchantUser model, indicating the merchant who added the product.
        in_stock_total (IntegerField): Number of units currently in stock.
        is_active (IntegerField): Flag indicating whether the product is currently active (1 for active, 0 for inactive).
    """
    """
    Products model.
    
    Represents a product in the system.  Each product belongs to a subcategory and a merchant.
    
    Attributes:
        id (AutoField): Primary key.
        url_slug (CharField): URL slug for the product.
        subcategories_id (ForeignKey): Foreign key to the SubCategories model, representing the product's subcategory.
        product_name (CharField): Name of the product.
        brand (CharField): Brand of the product.
        product_max_price (CharField): Maximum price of the product.
        product_discount_price (CharField): Discounted price of the product.
        product_description (TextField): Short description of the product.
        product_long_description (TextField): Long description of the product.
        created_at (DateTimeField): Timestamp indicating when the product was created.
        added_by_merchant (ForeignKey): Foreign key to the MerchantUser model, indicating the merchant who added the product.
        in_stock_total (IntegerField): Number of units currently in stock.
        is_active (IntegerField): Flag indicating whether the product is currently active (1 for active, 0 for inactive).
    """
    id=models.AutoField(primary_key=True)
    url_slug=models.CharField(max_length=255)
    subcategories_id=models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    product_max_price=models.CharField(max_length=255)
    product_discount_price=models.CharField(max_length=255)
    product_description=models.TextField()
    product_long_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    added_by_merchant=models.ForeignKey(MerchantUser,on_delete=models.CASCADE)
    in_stock_total=models.IntegerField(default=1)
    is_active=models.IntegerField(default=1)