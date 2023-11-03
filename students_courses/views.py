# from rest_framework.generics import RetrieveUpdateAPIView
# from accounts.models import Account
# from students_courses.permission import IsSuperUser
# from .serializers import StudentCourseSerializer
# from .models import StudentCourse
# from rest_framework_simplejwt.authentication import JWTAuthentication


# class StudentsCoursesView(RetrieveUpdateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsSuperUser]
#     serializer_class = StudentCourseSerializer
#     queryset = StudentCourse.objects.all()
#     lookup_url_kwarg = "course_id"
    
#     def perform_update(self, serializer):
#         try:
#           student = Account.objects.get(email=student_email).exists()
#           student_id = Account.id
#           student_username = Account.username
#         except Account.DoesNotExist:
#            ...
           

    # pegar o email e verificar se existe, caso exista relacione o estudante com o curso 
    # caso não exista retornar mensagem de erro
    # lembrar de relacionar os dados na tabela pivo

    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     student_email = data.get('student_email')
    #     try:
    #         account = Account.objects.get(email=student_email)
    #         # Se existir, atualize os campos no dicionário de dados
    #         data['student_id'] = account.id
    #         data['student_username'] = account.username
    #     except Account.DoesNotExist:
    #         # Se o email não existir, adicione-o à lista de emails inválidos
    #         data['student_id'] = None
    #         data['student_username'] = None

    #     return data
