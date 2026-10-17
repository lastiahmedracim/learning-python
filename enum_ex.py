from enum import Enum


# class OrderStatus(Enum):
#     PENDING = "pending"
#     PROCESSING = "processing"
#     SHIPPED = "shipped"
#     DELIVERED = "delivered"
#     CANCELLED = "cancelled"


# def show_status(status: OrderStatus) -> None:
#     if status == OrderStatus.PENDING:
#         print("Your order is waiting.")
#     elif status == OrderStatus.PROCESSING:
#         print("Your order is being processed.")
#     elif status == OrderStatus.SHIPPED:
#         print("Your order has been shipped.")
#     elif status == OrderStatus.DELIVERED:
#         print("Your order has been delivered.")
#     elif status == OrderStatus.CANCELLED:
#         print("Your order has been cancelled.")


# status = OrderStatus.SHIPPED

# show_status(status)





# class UserRole(Enum):
#     ADMIN = "admin"
#     MODERATOR = "moderator"
#     USER = "user"


# class User:
#     def __init__(self, name: str, role: UserRole):
#         self.name = name
#         self.role = role

#     def show_permissions(self) -> None:
#         if self.role == UserRole.ADMIN:
#             print(f"{self.name}: Can manage everything")

#         elif self.role == UserRole.MODERATOR:
#             print(f"{self.name}: Can manage content")

#         elif self.role == UserRole.USER:
#             print(f"{self.name}: Can view content")


# hunter = User("Hunter", UserRole.ADMIN)
# alice = User("Alice", UserRole.MODERATOR)
# bob = User("Bob", UserRole.USER)

# hunter.show_permissions()
# alice.show_permissions()
# bob.show_permissions()


