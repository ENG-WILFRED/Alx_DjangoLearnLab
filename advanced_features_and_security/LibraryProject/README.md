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

## Security Measures

- **DEBUG** is set to `False` in production.
- **SECURE_BROWSER_XSS_FILTER**, **X_FRAME_OPTIONS**, and **SECURE_CONTENT_TYPE_NOSNIFF** are enabled for browser-side protections.
- **CSRF_COOKIE_SECURE** and **SESSION_COOKIE_SECURE** ensure cookies are sent only over HTTPS.
- **CSP** is enforced to restrict sources for scripts and styles.
- All forms include `{% csrf_token %}` for CSRF protection.
- All user input is validated using Django forms.
- All database access uses Django ORM to prevent SQL injection.

**Testing:**  
Test forms for CSRF protection (submitting without a token should fail).  
Try injecting scripts in form fields to check for XSS (should be escaped).  
Attempt to access views with insufficient permissions to verify access control.
