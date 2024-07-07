from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def dashboard(request):
    return render(request, 'dashboard.html')

def member_profile(request):
    return render(request, 'member_profile.html')

def message(request):
    return render(request, 'message.html')

def official(request):
    return render(request, 'official.html')

def project_profile(request):
    return render(request, 'project_profile.html')

def proyek(request):
    return render(request, 'proyek.html')

class SetProjectView(APIView):
    def post(self, request):
        project = request.data.get('project', {})
        # Simpan project ke database atau logika lainnya
        return Response({"message": "Project set successfully", "project": project}, status=status.HTTP_200_OK)

class SetReadyProjectView(APIView):
    def post(self, request):
        project = request.data.get('project', {})
        # Simpan project ke database atau logika lainnya
        return Response({"message": "Ready project set successfully", "project": project}, status=status.HTTP_200_OK)

class StatusCompletionIEView(APIView):
    def get(self, request):
        # Simulasi respons data dari API lain
        response_data = {
            "status": "success",
            "notes": "Elemen sistem cerdas berhasil ditentukan!"
        }
        return Response(response_data, status=status.HTTP_200_OK)

class StatusCompletionICView(APIView):
    def get(self, request):
        # Simulasi respons data dari API lain
        response_data = {
            "status": "success",
            "notes": "Modul KNN Classifier dengan akurasi 95 %"
        }
        return Response(response_data, status=status.HTTP_200_OK)

class StatusCompletionIMPView(APIView):
    def get(self, request):
        # Simulasi respons data dari API lain
        response_data = {
            "status": "success",
            "notes": "Project berhasil diterima dan siap untuk diimplementasikan"
        }
        return Response(response_data, status=status.HTTP_200_OK)
