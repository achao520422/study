# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"调用函数: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def say_hello():
#     print("Hello!")
#
# say_hello()

# def check_permission(role: str):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(args,kwargs)
#             # 假设当前用户角色为 admin
#             current_user_role = "admin"
#             if current_user_role != role:
#                 raise PermissionError(f"需要 {role} 权限")
#             return func()
#         return wrapper
#     return decorator
#
# @check_permission("admin")
# def delete_data():
#     print("数据已删除")
#
# delete_data(('你好',''),{'s':4},age=25, name="Charlie")
