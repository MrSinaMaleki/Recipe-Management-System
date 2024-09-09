
### HW: Recipe Management System

یک برنامه جنگو از شما خواسته شده که دستورالعمل پخت غذا رو بتونید مدیریت کنید. صاحب رستوران از شما میخواهد عملیات CRUD را برای او انجام دهید. اما نکته‌ای که وجود داره اینه که باید با استفاده از جاوااسکریپت اطلاعات رو از جنگو بگیریم و به فرانت (که یک تمپلیت سادست که چون فعلا فرانت خاصی نداریم روی خود جنگو سرو میشه) بدیم. 
- استفاده از تمپلیت فقط در حدی مجازه که ویوهای مربوطه رو سرو کنه بقیه کار با جاوااسکریپت انجام میشه 
- از بین این چهار ویویی که از شما خواسته شده قفط دوتای اونها اجباری هستن و دوتای دیگه اختیاری محسوب میشن و نمره اضافه دارن
- دو ویو اجباری ویو ساخت دستورالعمل و نمایش لیست دستورالعمل ها می باشند
- دلیت و آپدیت کاملا اختیاری هستند
- تمرین بیشتر مرور بر جنگو و متمرکز بر ادغام جاوااسکریپت با بقیه اپلیکیشن است
#### Instructions:

1. **Set Up the Django Project and App**:
   - Create a new Django project named `recipe_manager`.
   - Inside the project, create a new app called `recipes`.
   - Make sure to add the `recipes` app to the `INSTALLED_APPS` list in `settings.py`.

2. **Define the Recipe Model**:
   - Create a model named `Recipe` with the following fields:
   - After defining the model, run the migrations to apply the changes to the database.

3. **Develop the Views for CRUD Operations**:
   - Create the following views in `views.py`:
     - **`recipe_list`**: Display all recipes.
     - **`recipe_create`**: Handle the creation of new recipes. Use AJAX to submit the form data and return a JSON response.
     - **`recipe_update`** (optional): Handle updating an existing recipe. Again, use AJAX to submit the form data.
     - **`recipe_delete`** (optional): Handle deleting a recipe. This should be triggered by an AJAX call.

   - **Hint**: Use `get_object_or_404` to retrieve the recipe instance in `recipe_update` and `recipe_delete` views.
   - **Hint**: Return a JSON response indicating success or failure in each view that handles AJAX requests.

   ```python
   from django.shortcuts import get_object_or_404, redirect
   from django.http import JsonResponse
   # Import Recipe model and RecipeForm here

   def recipe_list(request):
       # Retrieve and display all recipes
       pass

   def recipe_create(request):
       # Handle recipe creation with AJAX
       pass

   def recipe_update(request, pk): # OPTIONAL
       # Handle recipe update with AJAX
       # pass

    def recipe_delete(request, pk): # OPTIONAL
       # Handle recipe deletion with AJAX
       pass
   ```
