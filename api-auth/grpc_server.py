import os
from concurrent import futures
import grpc
from django.conf import settings
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from authentication.AuthService import AuthService
import auth_pb2
import auth_pb2_grpc

class GrpcAuthService(auth_pb2_grpc.GrpcAuthServiceServicer):
    def verify_token(self, request, context):
        result = AuthService.validate_jwt(request.token)

        if result.get("is_valid"):
            return auth_pb2.UserResponse(
                id=result.get("id"),
                username=result.get("username"),
                email=result.get("email"),
                is_valid=True
            )
        return auth_pb2.UserResponse(is_valid=False)
    
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_GrpcAuthServiceServicer_to_server(GrpcAuthService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()