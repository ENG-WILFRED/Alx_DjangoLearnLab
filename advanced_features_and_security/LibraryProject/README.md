# LibraryProject

This is the initial Django project setup for ALX Django learning tasks.  
It includes basic Django configuration and runs the server at http://127.0.0.1:8000.

## Permissions and Groups Setup

- **Custom Permissions:**  
  The `Book` model defines `can_view`, `can_create`, `can_edit`, and `can_delete` permissions in its `Meta` class.

- **Groups:**  
  Use the Django admin to create groups: Editors, Viewers, Admins.  
  Assign the relevant permissions to each group.

- **Enforcing Permissions:**  
  Views that create, edit, delete, or list books are protected using the `@permission_required` decorator with the appropriate permission codename.

- **Testing:**  
  Assign users to groups via the admin. Log in as different users to verify access is correctly restricted.

- **Example:**  
  Only users in the Editors or Admins group can add or edit books. Only Viewers, Editors, or Admins can view books. Only Admins can delete books.
