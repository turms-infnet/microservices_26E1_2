import auth_pb2_grpc
import auth_pb2
import grpc

def validate_token(token):
    channel = grpc.insecure_channel('localhost:50051')
    stub = auth_pb2_grpc.GrpcAuthServiceStub(channel)
    return stub.verify_token(auth_pb2.VerifyTokenRequest(token=token))