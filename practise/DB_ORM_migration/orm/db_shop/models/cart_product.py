from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint

from practise.DB_ORM_migration.orm.db_shop.models import Base


class CartProduct(Base):
    __tablename__ = "cart_product"
    __table_args__ = (
        PrimaryKeyConstraint('cart_id', 'product_id'),
    )

    cart_id = Column(Integer, ForeignKey("cart.id"))
    product_id = Column(Integer, ForeignKey("product.id"))

    def __str__(self):
        return f"{self.__class__.__name__}(cart_id={self.cart_id}, product.id={self.product_id})"

    def __repr__(self):
        return str(self)